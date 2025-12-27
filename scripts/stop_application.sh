#!/bin/bash

# Stop the application
pkill -f gunicorn || true

echo "Application stopped"
