#!/bin/sh

# Get the directory where the script is located
SCRIPT_DIR=$(dirname "$0")

# Full path to the plist file in the project
PROJECT_PATH="$SCRIPT_DIR/launchd/pyhotkey.plist"

# Copy the plist file
cp "$PROJECT_PATH" "$HOME/Library/LaunchAgents/pyhotkey.plist"

# Load the service
launchctl load "$HOME/Library/LaunchAgents/pyhotkey.plist"

