#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Create reports directory if it doesn't exist
mkdir -p reports

echo "Setup complete! To activate the environment, run: source venv/bin/activate"