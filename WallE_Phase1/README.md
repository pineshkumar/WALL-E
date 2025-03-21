# Phase 1: Controlling a Motor with Raspberry Pi and OpenAI API

## 📌 Overview
This project demonstrates how to control a DC motor using a Raspberry Pi, a motor driver (L298N), and OpenAI's API for voice-based motor commands.

## 📝 Visual Flow
1. **Voice Command (User says "Start motor")**  
   ⬇  
2. **Raspberry Pi captures the voice**  
   ⬇  
3. **Send command to OpenAI API for understanding**  
   ⬇  
4. **Process response and control the motor via GPIO**  
   ⬇  
5. **Motor starts, stops, or slows down based on command**  

## 🔧 Required Setup
### 🛠 Hardware Components
- Raspberry Pi 4B  
- Motor Driver (L298N)  
- DC Motor  
- Power Supply  
- Jumper Wires  

### 📌 GPIO Pin Setup
| **Raspberry Pi Pin** | **Motor Driver (L298N) Pin** | **Purpose** |
|----------------------|-----------------------------|-------------|
| GPIO 17 (BCM)       | IN1                          | Motor Control 1 |
| GPIO 27 (BCM)       | IN2                          | Motor Control 2 |
| GPIO 22 (BCM)       | ENA                          | Speed Control (PWM) |

## 📜 Project Structure
```
WallE_Phase1/
│── main.py              # Main file that runs everything
│── motor_control.py     # Motor handling (start, stop, slow)
│── voice_recognition.py # Captures user command
│── openai_api.py        # Uses OpenAI API to understand commands
│── config.py            # Stores OpenAI API Key
│── requirements.txt     # Required dependencies
└── setup.sh             # Install dependencies
```

## 📥 Installation
### 1️⃣ Setup Raspberry Pi Dependencies
```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install openai speechrecognition RPi.GPIO
```

### 2️⃣ Run Setup Script
```bash
chmod +x setup.sh
./setup.sh
```

### 3️⃣ Set OpenAI API Key (`config.py`)
```python
OPENAI_API_KEY = "your_openai_api_key_here"
```

### 4️⃣ Start the Program
```bash
python3 main.py
```

## 📝 Expected Behavior
| **Voice Command** | **Motor Action** |
|------------------|----------------|
| "Start motor" | Motor runs at full speed |
| "Stop here" | Motor stops |
| "Run slow" | Motor runs at 50% speed |
| "Exit" | Stops the program |

## ✅ Next Steps (Phase 2)
- Add **Camera Object Detection**
- Implement **Battery Management**
- Integrate **AI-based Movement Control**
