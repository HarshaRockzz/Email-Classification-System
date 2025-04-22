# scripts/train_model.py
import sys
import os
from pathlib import Path

# Add project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.models import train_model
from src.config import DATA_PATH
from src.logging_config import logger
from safetensors.torch import save_file

if __name__ == "__main__":
    logger.info("Starting model training script...")
    # Capture the returned model
    model = train_model(DATA_PATH)
    logger.info("Model training completed and saved.")
    logger.info("Training script completed.")
    
    # Save the model with safetensors
    model.save_pretrained("models/bert_model", safe_serialization=True)