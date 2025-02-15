import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()  # Load environment variables from .env file

HF_TOKEN = os.getenv("HF_TOKEN")
if HF_TOKEN is None:
    raise ValueError("HF_TOKEN is not set. Please set it in your .env file.")

client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct", token=HF_TOKEN)

output = client.text_generation(
    "The capital of France is",
    max_new_tokens=100,
)

print(output) 