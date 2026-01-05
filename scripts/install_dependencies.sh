#!/bin/bash
# Install system packages (runs BEFORE files are copied)
apt-get update
apt-get install -y python3 python3-pip python3-venv
