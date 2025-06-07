#!/bin/sh

"""
I made this to document how I get this up and runnning for when I do something else and I need to come back to the webapp
"""

# Setting up the environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Running the application
# Visit the webapp at 127.0.0.1:8050
python src/app.py

# Cleaning up after the run
deactivate
rm -rf .venv