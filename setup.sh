#!/bin/bash

# Set up the frontend
cd frontend
npm install

# Set up the backend
cd ../backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "Setup completed!"
