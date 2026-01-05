#!/bin/bash
# This runs AFTER files are copied to /home/ubuntu/python-app

# Set correct ownership
chown -R ubuntu:ubuntu /home/ubuntu/python-app

# Switch to app directory
cd /home/ubuntu/python-app

# Create virtual environment as ubuntu user
su - ubuntu -c "cd /home/ubuntu/python-app && python3 -m venv venv"

# Install Python dependencies as ubuntu user
su - ubuntu -c "cd /home/ubuntu/python-app && source venv/bin/activate && pip install -r requirements.txt"
