#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "motor_crc_hg.h"
#include "rclcpp/rclcpp.hpp"
#include "unitree_hg/msg/low_cmd.hpp"
#include "unitree_hg/msg/low_state.hpp"
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
                topic_callback_cmd(message);
            });

        lowstate_subscription_ = this->create_subscription<unitree_hg::msg::LowState>(
            "/lowstate", 10,
            [this](const unitree_hg::msg::LowState::SharedPtr message)
            {
                topic_callback_state(message);
            });

        lowcmd_publisher_ =
            this->create_publisher<unitree_hg::msg::LowCmd>("/lowcmd", 10);

        timer_ = this->create_wall_timer(std::chrono::milliseconds(SAMPLING_TIME_MS),
                                         [this]
                                         { timer_callback(); });

        last_msg_time_ = std::chrono::steady_clock::now();
    }

private:
    void topic_callback_cmd(const unitree_hg::msg::LowCmd::SharedPtr &message)
    {
        last_msg_time_ = std::chrono::steady_clock::now(); // update timestamp

        low_command_.mode_pr = message->mode_pr;
        low_command_.mode_machine = message->mode_machine;
        for (int i = 0; i < MOTORS; i++)
        {
            low_command_.motor_cmd[i].mode = message->motor_cmd[i].mode;
            if (message->motor_cmd[i].mode != 0)
            {
                if (i < 12)
                {
                    if (!legs_on)
                    {
                        legs_on = true;
                        low_command_.motor_cmd[i].q = message->motor_cmd[i].q;
                    }
                    else
                    {
                        set_angle(i, message->motor_cmd[i].q, step_size);
                    }
                }
                else if (i < 15)
                {
                    if (!waist_on)
                    {
                        waist_on = true;
                        low_command_.motor_cmd[i].q = message->motor_cmd[i].q;
                    }
                    else
                    {
                        set_angle(i, message->motor_cmd[i].q, step_size);
                    }
                }
                else
                {
                    if (!arms_on)
                    {
                        arms_on = true;
                        low_command_.motor_cmd[i].q = message->motor_cmd[i].q;
                    }
                    else
                    {
                        set_angle(i, message->motor_cmd[i].q, step_size);
                    }
                }
            }

            low_command_.motor_cmd[i].dq = message->motor_cmd[i].dq;
            low_command_.motor_cmd[i].tau = message->motor_cmd[i].tau;
            low_command_.motor_cmd[i].kp = message->motor_cmd[i].kp;
            low_command_.motor_cmd[i].kd = message->motor_cmd[i].kd;
        }
    }

    void topic_callback_state(const unitree_hg::msg::LowState::SharedPtr &message)
    {
        for (int i = 0; i < MOTORS; i++)
        {
            low_state_.motor_state[i].q = message->motor_state[i].q;
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
            legs_on = false;
            waist_on = false;
            arms_on = false;
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
    rclcpp::Subscription<unitree_hg::msg::LowState>::SharedPtr lowstate_subscription_;
    rclcpp::Publisher<unitree_hg::msg::LowCmd>::SharedPtr lowcmd_publisher_;
    unitree_hg::msg::LowCmd low_command_;                 // Unitree hg lowcmd message
    unitree_hg::msg::LowState low_state_;                 // Unitree hg lowstate message
    std::chrono::steady_clock::time_point last_msg_time_; // last received message time
    bool legs_on = false;
    bool waist_on = false;
    bool arms_on = false;
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