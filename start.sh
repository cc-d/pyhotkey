#!/bin/sh

# Check if the user is root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root"
    exit 1
fi

# Activate virtual environment if needed
if [ -f "venv/bin/activate" ]; then
    . venv/bin/activate
fi

# Run the Python script
python main.py

