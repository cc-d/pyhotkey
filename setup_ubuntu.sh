#!/bin/sh

# Get the directory where the script is located
SCRIPT_DIR=$(dirname "$0")

# Full path to the systemd service file in the project
PROJECT_PATH="$SCRIPT_DIR/systemd/pyhotkey.service"

# Copy the systemd service file
sudo cp "$PROJECT_PATH" /etc/systemd/system/pyhotkey.service

# Reload the systemd daemon
sudo systemctl daemon-reload

# Enable the service
sudo systemctl enable pyhotkey.service

# Start the service
sudo systemctl start pyhotkey.service

