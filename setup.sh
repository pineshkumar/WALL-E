#!/bin/bash

echo "Updating Raspberry Pi..."
sudo apt update && sudo apt upgrade -y

echo "Installing dependencies..."
sudo apt install -y python3-pip python3-opencv libportaudio2

echo "Installing Python packages..."
pip3 install openai speechrecognition opencv-python numpy RPi.GPIO

echo "Setup completed!"
