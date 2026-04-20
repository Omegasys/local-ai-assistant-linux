#!/bin/bash

# setup_environment.sh
# This script sets up the environment for the AI Assistant project.

echo "Setting up the environment..."

# Create a virtual environment if not already created
if [ ! -d "venv" ]; then
    echo "Creating a virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source venv/bin/activate

# Install the required Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Environment setup complete!"
