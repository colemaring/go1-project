#include "unitree_legged_sdk/unitree_legged_sdk.h"
#include <iostream>
#include <fstream>
#include <unistd.h>
#include <string.h>

using namespace UNITREE_LEGGED_SDK;

class Custom {
public:
    Custom(uint8_t level) : safe(LeggedType::Go1),
                            udp(level, 8090, "192.168.12.1", 8082) {
        udp.InitCmdData(cmd);
    }
    void UDPRecv();
    void UDPSend();
    void RobotControl();
    void ReadCommand();  // New method to read command from file
    void ApplyLowPassFilter(float& target, float current, float alpha);  // Low-pass filter

    Safety safe;
    UDP udp;
    HighCmd cmd = {0};
    HighState state = {0};
    int motiontime = 0;
    float dt = 0.002;  // 0.001~0.01
    std::string current_command;
};

void Custom::UDPRecv() {
    udp.Recv();
}

void Custom::UDPSend() {
    udp.Send();
}

void Custom::ReadCommand() {
    std::ifstream command_file("/mnt/c/users/colem/Desktop/command.txt");
    if (command_file.is_open()) {
        std::getline(command_file, current_command);
        command_file.close();
    }
}

void Custom::ApplyLowPassFilter(float& target, float current, float alpha) {
    target = alpha * current + (1 - alpha) * target;
}

void Custom::RobotControl() {
    ReadCommand();  // Read command from file

    // Adjust robot mode based on the command read
    if (current_command == "pointing left") {
        cmd.mode = 1;
        ApplyLowPassFilter(cmd.euler[1], 0.4f, 0.1f);  // Apply low-pass filter to Euler angle
        std::cout << "pointing left (mode 1)" << std::endl;
    } else if (current_command == "pointing right") {
        cmd.mode = 1;
        ApplyLowPassFilter(cmd.euler[1], -0.4f, 0.1f);  // Apply low-pass filter to Euler angle
        std::cout << "pointing right (mode 2)" << std::endl;
    } else if (current_command == "thumbs right") {
        cmd.mode = 12;
        std::cout << "thumbs right (mode 12)" << std::endl;
    } else if (current_command == "peace") {
        cmd.mode = 11;
        std::cout << "peace (mode 11)" << std::endl;
    } else if (current_command == "hand open") {
        cmd.mode = 13;
        std::cout << "hand open (mode 13)" << std::endl;
    } 
    else if (current_command == "pointing up") {
        cmd.mode = 9;
        std::cout << "pointing up (mode 9)" << std::endl;
    }
    
     else {
        cmd.mode = 0;  // Default idle mode
        ApplyLowPassFilter(cmd.euler[0], 0.0f, 0.1f);  // Apply low-pass filter to Euler angle X
        ApplyLowPassFilter(cmd.euler[1], 0.0f, 0.1f);  // Apply low-pass filter to Euler angle Y
        ApplyLowPassFilter(cmd.euler[2], 0.0f, 0.1f);  // Apply low-pass filter to Euler angle Z
        std::cout << "Robot is in idle mode (mode 0)" << std::endl;
    }

    udp.GetRecv(state);

    // Rest of your control logic can remain as it is or be modified if needed

    udp.SetSend(cmd);
}

int main(void) {
    std::cout << "Communication level is set to HIGH-level." << std::endl
              << "WARNING: Make sure the robot is standing on the ground." << std::endl
              << "Press Enter to continue..." << std::endl;
    std::cin.ignore();

    Custom custom(HIGHLEVEL);
    LoopFunc loop_control("control_loop", custom.dt, boost::bind(&Custom::RobotControl, &custom));
    LoopFunc loop_udpSend("udp_send", custom.dt, 3, boost::bind(&Custom::UDPSend, &custom));
    LoopFunc loop_udpRecv("udp_recv", custom.dt, 3, boost::bind(&Custom::UDPRecv, &custom));

    loop_udpSend.start();
    loop_udpRecv.start();
    loop_control.start();

    while (1) {
        sleep(10);
    };

    return 0;
}
