#!/bin/bash

# install_dependencies.sh
# This script installs the required system dependencies for the AI Assistant project.

echo "Updating package list..."
sudo apt-get update -y

echo "Installing Python3 and pip3..."
sudo apt-get install python3 python3-pip -y

echo "Installing system dependencies..."
sudo apt-get install -y python3-dev build-essential libssl-dev libffi-dev python3-setuptools libpython3-dev

echo "Installing dependencies for speech recognition..."
sudo apt-get install -y portaudio19-dev

echo "Installing required Python libraries..."
pip3 install -r requirements.txt

echo "Dependencies installed successfully!"
