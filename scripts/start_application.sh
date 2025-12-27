#!/bin/bash

cd /home/ubuntu/python-app

# Activate virtual environment
source venv/bin/activate

# Kill any existing gunicorn processes
pkill -f gunicorn || true

# Start the application with gunicorn in background
nohup gunicorn --bind 0.0.0.0:5000 app:app > /home/ubuntu/python-app/app.log 2>&1 &

# Wait a moment for the app to start
sleep 3

echo "Application started successfully"
