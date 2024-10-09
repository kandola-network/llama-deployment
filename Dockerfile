# Use an official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip

# Copy the FastAPI script and model directory to the container
COPY deploy-llama-3b.py ./deploy-llama-3b.py
COPY llama-3b-api.py ./llama-3b-api.py

# Install necessary Python packages for model and API
RUN pip install transformers fastapi uvicorn torch sentencepiece protobuf

# Run the deploy script to download the model
RUN python3 deploy-llama-3b.py

# Expose the FastAPI port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "llama-3b-api:app", "--host", "0.0.0.0", "--port", "8000"]