#!/bin/bash

# Create a virtual environment
python3 -m venv ./aienv

# Activate the virtual environment
source ./aienv/bin/activate

# Install dependencies
pip3 install -r requirements.txt


