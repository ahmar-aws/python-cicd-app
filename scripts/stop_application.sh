#!/bin/bash
# Stop the application if it's running
if [ -f /home/ubuntu/python-app/app.pid ]; then
    kill $(cat /home/ubuntu/python-app/app.pid) 2>/dev/null || true
    rm /home/ubuntu/python-app/app.pid
fi

# Fallback: kill any Python app processes
pkill -f "python.*app.py" || true
