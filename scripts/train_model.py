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

if __name__ == "__main__":
    logger.info("Starting model training script...")
    train_model(DATA_PATH)
    logger.info("Training script completed.")