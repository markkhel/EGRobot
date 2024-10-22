# EGRobot Project

The **EGRobot** is a collaborative project assigned to the Epsilon Gamma pledge class. Our goal is to build a robot capable of picking up and collecting trash, controlled via Bluetooth, and processing voice commands. This project leverages a **Raspberry Pi 4 B+** with 2GB RAM for processing all functionalities.

## Key Features
- **Bluetooth Control**: Operate the robot remotely using a Bluetooth controller.
- **Voice Recognition**: Enable voice commands to control the robot.
- **Robotic Arm**: Designed to pick up and store trash.

## Hardware & Software Setup
- **Hardware**: Raspberry Pi 4 B+ (2GB RAM), motor systems, robotic arm components.
- **Software**: Python-based development using the Thonny IDE and Linux virtual environments.
- **Testing Platform**: Raspberry Pi with SSH access for code testing and execution.

## Team Assignments
- **Motors**:  
  Brian, Tim, Mark, William, Ryan, Omir  
  Responsible for motor control, movement, and integration with the robotic arm.
  
- **Speech Recognition**:  
  Omir, Ryan, Tim, William, Mark  
  Working on voice command processing and integration.

- **Bluetooth Control**:  
  Luke, Alan, Shomaun
  Implementing Bluetooth connectivity to control the robot.

- **Robotic Arm (Trash Pickup)**:  
  **All Members**  
  Developing the robotic arm's ability to pick up and store trash.

## Development Guidelines
1. **Branching**: All development work should be done in the `dev` branch.  
   **Please do not push directly to `main`** until the code is fully tested and confirmed to work on the Raspberry Pi hardware.
2. **Development Environment**:  
   Developers can write and test code using Linux virtual environments with the Thonny IDE. Before starting a new development, pull the lastest code from `dev` branch to ensure you have the most recent changes. Once programming is complete, push    new code into the `dev` branch.
   After all development is complete, SSH into the Raspberry Pi to pull the latest code from the repository and test the functionality on the actual hardware.

## Contribution Workflow
- Make sure your code is properly tested in the virtual environment before pushing to the `dev` branch.
- Coordinate with team members when merging features or bug fixes.
- Testing and confirmation on Raspberry Pi are required before merging into the `main` branch.

For more details on the project setup, latest commits, and development progress, refer to the `dev` branch of the repository.

## Access to Raspberry Pi
- Pi is connected to wifi "eduroam" and requires the host computer to be on the same network in order to SSH into.
- To find IP address/hostname, run "hostname -I" in the terminal.
- Run the command "ssh alanlee@<IP_ADDRESS>" in the terminal
- Username - "alanlee"
- Password for SSH authentication - "6ft".
