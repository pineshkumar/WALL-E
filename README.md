# Wall-E Robot Project

## Overview
This project is a Raspberry Pi-based robot that can recognize voice commands, control motors, and use a camera for object detection and tracking. The robot can execute commands such as:
- "Follow me" (Moves forward)
- "Stop here" (Stops the motor)
- "Run slow" (Reduces speed)
- "Scan object" (Uses the camera for object detection)

## Goals
- Develop a fully functional Wall-E-inspired robot with voice control.
- Enable real-time object detection and tracking using a camera.
- Implement AI-powered voice recognition for smooth interaction.
- Ensure seamless motor control for movement and speed adjustments.
- Provide an easy-to-install and modular codebase for future expansion.
- Establish real-time communication between the robot and the user.
- Automate farm monitoring and security checks with AI-driven analysis.
- Implement self-charging functionality based on battery conditions.
- Assist farmers in optimizing crop growth and increasing farm productivity.

## Features
- **Real-Time Communication:** Interacts with users through voice commands and AI responses.
- **Object Detection & Tracking:** Uses a camera to detect and follow objects or people.
- **Motor Control:** Executes precise movements based on user commands.
- **AI-Powered Voice Recognition:** Understands and executes natural language commands.
- **Secure Farm Rounding:** Patrols designated areas using AI vision.
- **Automated Farm Condition Monitoring:** AI checks soil quality, plant health, and weather conditions.
- **Automated Alerts & Notifications:** Sends email and SMS alerts for security concerns or necessary farm improvements.
- **Self-Charging System:** Monitors battery levels and moves to a charging station when needed.
- **AI-Driven Farming Assistance:** Analyzes soil, plant health, and weather conditions to provide recommendations.

## Future Planning
- **Farming Monitoring System:**
  - AI-powered camera for monitoring plant growth.
  - Sound-based alerts for detecting anomalies in farm conditions.
  - Object detection for identifying plant health and pests.
  - Automated reporting to the farm owner via email and messages.
- **Soil Analysis & Health Checking:**
  - Sensors to check soil moisture and nutrient levels.
  - AI-based recommendations for optimal farming.
- **Market Price Tracking:**
  - Real-time local area price checks using APIs.
  - Weather API integration for farming predictions.
- **Enhanced Farm Security:**
  - AI-driven surveillance to secure the entire farm.
  - Automated alerts for unauthorized movements.
  - Integration with security alarms and response mechanisms.
- **Self-Sustaining Energy Management:**
  - Solar panel integration for continuous charging.
  - Smart power management to optimize energy consumption.

## Project Structure
```
WallE_Robot/
│── main.py               # Main program that connects everything
│── motor_control.py      # Handles motor control (start, stop, slow, turn)
│── voice_recognition.py  # Captures voice input and processes commands
│── openai_api.py         # Uses OpenAI API to interpret commands
│── camera_follow.py      # Uses OpenCV for object detection & tracking
│── farm_monitor.py       # AI-driven farm condition analysis and notifications
│── battery_manager.py    # Manages power and self-charging
│── requirements.txt      # Required dependencies
│── config.py             # Stores API keys and configurations
└── setup.sh              # Script to install all dependencies
```

## Installation
### 1️⃣ **Run the Setup Script**
```bash
chmod +x setup.sh
./setup.sh
```

## Configuration
### 2️⃣ **Set Up API Key**
Edit `config.py` and add your OpenAI API key:
```python
OPENAI_API_KEY = "your_openai_api_key_here"
```

## Running the Project
```bash
python3 main.py
```

## Expected Behavior
| **Voice Command** | **Action** |
|------------------|-----------|
| "Follow me" | Robot moves forward |
| "Stop here" | Robot stops |
| "Run slow" | Robot moves slowly |
| "Scan object" | Robot scans using the camera |
| "Analyze farm" | AI scans farm conditions and reports issues |
| "Check battery" | AI reports battery level and charges if needed |
| "Exit" | Stops the program |

## Future Enhancements
- Add **face tracking** to follow humans.
- Implement **WiFi remote control** via Flask.
- Upgrade **motors & sensors** for better navigation.
- AI-powered **automated response system** for farm security threats.
- **Integration with smart irrigation systems** for automated water control.
- **Implement solar-powered charging for complete automation.**

## Contributing
Feel free to submit pull requests to improve the project!

## License
This project is open-source under the MIT License.

