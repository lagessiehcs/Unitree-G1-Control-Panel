#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "motor_crc_hg.h"
#include "rclcpp/rclcpp.hpp"
#include "unitree_hg/msg/low_cmd.hpp"
#include "unitree_hg/msg/motor_cmd.hpp"

using namespace std::chrono_literals;

#define SAMPLING_TIME_MS 2
#define MOTORS 29
#define TIMEOUT_MS 50 // stop publishing if no message received for 100ms

class InterfacePubSub : public rclcpp::Node
{
public:
    InterfacePubSub()
        : Node("interface_pubsub")
    {
        lowcmd_subscription_ = this->create_subscription<unitree_hg::msg::LowCmd>(
            "/lowcmd_interface", 10,
            [this](const unitree_hg::msg::LowCmd::SharedPtr message)
            {
                topic_callback(message);
            });

        lowcmd_publisher_ =
            this->create_publisher<unitree_hg::msg::LowCmd>("/lowcmd", 10);

        timer_ = this->create_wall_timer(std::chrono::milliseconds(SAMPLING_TIME_MS),
                                         [this]
                                         { timer_callback(); });

        last_msg_time_ = std::chrono::steady_clock::now();
    }

private:
    void topic_callback(const unitree_hg::msg::LowCmd::SharedPtr &message)
    {
        last_msg_time_ = std::chrono::steady_clock::now(); // update timestamp

        low_command_.mode_pr = message->mode_pr;
        low_command_.mode_machine = message->mode_machine;
        for (int i = 0; i < MOTORS; i++)
        {
            low_command_.motor_cmd[i].mode = message->motor_cmd[i].mode;
            set_angle(i, message->motor_cmd[i].q, step_size);
            low_command_.motor_cmd[i].dq = message->motor_cmd[i].dq;
            low_command_.motor_cmd[i].tau = message->motor_cmd[i].tau;
            low_command_.motor_cmd[i].kp = message->motor_cmd[i].kp;
            low_command_.motor_cmd[i].kd = message->motor_cmd[i].kd;
        }
        for (int i = 0; i < 4; i++)
        {
            low_command_.reserve[i] = message->reserve[i];
        }
    }

    void timer_callback()
    {
        auto now = std::chrono::steady_clock::now();
        auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(now - last_msg_time_);

        if (elapsed < std::chrono::milliseconds(TIMEOUT_MS))
        {
            get_crc(low_command_);
            lowcmd_publisher_->publish(low_command_);
        }
        else
        {
            low_command_ = unitree_hg::msg::LowCmd();
        }
    }

    void set_angle(int motor_idx, float target, float step_size)
    {
        if (low_command_.motor_cmd[motor_idx].q <= target)
        {
            if (low_command_.motor_cmd[motor_idx].q + step_size < target)
            {
                low_command_.motor_cmd[motor_idx].q += step_size;
            }
            else
            {
                low_command_.motor_cmd[motor_idx].q = target;
            }
        }

        else if (low_command_.motor_cmd[motor_idx].q > target)
        {
            if (low_command_.motor_cmd[motor_idx].q - step_size > target)
            {
                low_command_.motor_cmd[motor_idx].q -= step_size;
            }
            else
            {
                low_command_.motor_cmd[motor_idx].q = target;
            }
        }
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Subscription<unitree_hg::msg::LowCmd>::SharedPtr lowcmd_subscription_;
    rclcpp::Publisher<unitree_hg::msg::LowCmd>::SharedPtr lowcmd_publisher_;
    unitree_hg::msg::LowCmd low_command_;                 // Unitree hg lowcmd message
    std::chrono::steady_clock::time_point last_msg_time_; // last received message time
    float step_size = 0.008;
};

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<InterfacePubSub>();
    rclcpp::executors::MultiThreadedExecutor executor;
    executor.add_node(node);
    executor.spin();

    rclcpp::shutdown();
    return 0;
}