from huggingface_hub import HfApi, login
import os

# Set your Hugging Face token (replace with your actual token)
hf_token = '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'

# Login with your token
login(token=hf_token)

# Specify the model path
model_path = 'meta-llama/Llama-3.2-3B-Instruct'

# Instantiate the API
api = HfApi()

# Define the download directory
download_dir = os.path.join(os.getcwd(), 'llama_3_2_3bi')

# Ensure the download directory exists
os.makedirs(download_dir, exist_ok=True)

# Download the model to the specified directory
api.snapshot_download(repo_id=model_path, local_dir=download_dir)

print(f"Model downloaded to {download_dir} directory.")