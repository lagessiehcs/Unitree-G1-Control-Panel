#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "motor_crc_hg.h"
#include "rclcpp/rclcpp.hpp"
#include "unitree_hg/msg/low_cmd.hpp"
#include "unitree_hg/msg/motor_cmd.hpp"

using namespace std::chrono_literals;

#define SAMPLING_TIME_MS 0
#define MOTORS 29
#define TIMEOUT_MS 100 // stop publishing if no message received for 100ms

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
            low_command_.motor_cmd[i].q = message->motor_cmd[i].q;
            low_command_.motor_cmd[i].dq = message->motor_cmd[i].dq;
            low_command_.motor_cmd[i].tau = message->motor_cmd[i].tau;
            low_command_.motor_cmd[i].kp = message->motor_cmd[i].kp;
            low_command_.motor_cmd[i].kd = message->motor_cmd[i].kd;
            low_command_.motor_cmd[i].reserve = message->motor_cmd[i].reserve;
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
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Subscription<unitree_hg::msg::LowCmd>::SharedPtr lowcmd_subscription_;
    rclcpp::Publisher<unitree_hg::msg::LowCmd>::SharedPtr lowcmd_publisher_;
    unitree_hg::msg::LowCmd low_command_;                 // Unitree hg lowcmd message
    std::chrono::steady_clock::time_point last_msg_time_; // last received message time
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