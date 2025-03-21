# Wall-E Robot Project

## Overview
This project is a Raspberry Pi-based robot that can recognize voice commands, control motors, and use a camera for object detection and tracking. The robot can execute commands such as:
- "Follow me" (Moves forward)
- "Stop here" (Stops the motor)
- "Run slow" (Reduces speed)
- "Scan object" (Uses the camera for object detection)

## Project Structure
```
WallE_Robot/
│── main.py               # Main program that connects everything
│── motor_control.py      # Handles motor control (start, stop, slow, turn)
│── voice_recognition.py  # Captures voice input and processes commands
│── openai_api.py         # Uses OpenAI API to interpret commands
│── camera_follow.py      # Uses OpenCV for object detection & tracking
│── requirements.txt      # Required dependencies
└── config.py             # Stores API keys and configurations
```

## Installation
### 1️⃣ **Update Raspberry Pi**
```bash
sudo apt update && sudo apt upgrade -y
```

### 2️⃣ **Install Dependencies**
```bash
sudo apt install python3-pip python3-opencv libportaudio2 -y
pip install -r requirements.txt
```

### 3️⃣ **Create `requirements.txt`**
```txt
openai
speechrecognition
opencv-python
numpy
RPi.GPIO
```

## Configuration
### 4️⃣ **Set Up API Key**
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
| "Exit" | Stops the program |

## Future Enhancements
- Add **face tracking** to follow humans.
- Implement **WiFi remote control** via Flask.
- Upgrade **motors & sensors** for better navigation.

## Contributing
Feel free to submit pull requests to improve the project!

## License
This project is open-source under the MIT License.

