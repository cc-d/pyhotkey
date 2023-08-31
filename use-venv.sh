#!/bin/sh

# Assumes pyenv is installed, mainly for my own convenience.

func() {
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        eval "$(pyenv init -)"
        pyenv shell 3.11
        python -m venv venv
    else
        echo "Virtual environment already exists."
    fi
}

func

if [ -f ".default-choice-use-venv" ]; then
    default_choice=$(cat .default-choice-use-venv)
    if [ "$default_choice" = "y" ] || [ "$default_choice" = "Y" ]; then
        pip_response="y"
    elif [ "$default_choice" = "n" ] || [ "$default_choice" = "N" ]; then
        pip_response="n"
    else
        echo "Invalid content in .default-choice-use-venv"
        exit 1
    fi
else
    echo "Install pip packages? y/n"
    read pip_response
fi

if [ "$pip_response" = "y" ] || [ "$pip_response" = "Y" ]; then
    . venv/bin/activate
    pip install .
fi

