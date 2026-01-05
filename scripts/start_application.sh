#!/bin/bash
cd /home/ubuntu/python-app

# Activate virtual environment and start app
source venv/bin/activate

# Start your Python application (choose based on your framework)
nohup python3 app.py > app.log 2>&1 &

# Save the process ID
echo $! > app.pid
