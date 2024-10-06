#!/bin/bash

# Create a virtual environment named 'env'
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install required packages
pip install -r requirements.txt

echo "Virtual environment setup complete. To activate it, use: source env/bin/activate"
