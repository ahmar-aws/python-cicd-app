#!/bin/bash

# Update system
apt-get update

# Install Python and pip if not installed
apt-get install -y python3 python3-pip python3-venv

# Create virtual environment
cd /home/ubuntu/python-app
python3 -m venv venv

# Activate virtual environment and install dependencies
source venv/bin/activate
pip install -r requirements.txt

# Set proper permissions
chown -R ubuntu:ubuntu /home/ubuntu/python-app
