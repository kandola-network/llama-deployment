#!/bin/bash

# Step 1: Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Step 2: Install necessary Python packages
pip install transformers fastapi uvicorn

# Step 3: Run the deploy script to download and save the model
python3 deploy-llama-3b.py

# Step 4: Build the Docker container
sudo docker compose up -d

# Step 5: Clean up (optional)
deactivate
