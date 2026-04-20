#!/bin/bash

# start_assistant.sh
# This script launches the AI Assistant.

echo "Activating the virtual environment..."

# Activate the virtual environment
source venv/bin/activate

echo "Starting the AI Assistant..."

# Run the assistant (entry point to start the assistant process)
python3 src/core/assistant.py
