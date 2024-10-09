from huggingface_hub import HfApi, login
import os

# Set your Hugging Face token (replace with your actual token)
hf_token = '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'

# Login with your token (this is how authentication is done now)
login(token=hf_token)

# Specify the model path
model_path = 'meta-llama/Llama-3.2-3B-Instruct'

# Instantiate the API
api = HfApi()

# Download the model
api.snapshot_download(model_path)

print("Model downloaded to ./llama_3_2_3bi directory.")