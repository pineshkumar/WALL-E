#!/bin/bash
echo "Installing dependencies..."
sudo apt update && sudo apt install python3-pip -y
pip3 install -r requirements.txt
echo "Setup complete."
