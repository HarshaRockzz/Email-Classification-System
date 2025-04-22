from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = os.getenv("MODEL_PATH", str(BASE_DIR / "models/bert_model"))
TOKENIZER_PATH = os.getenv("TOKENIZER_PATH", str(BASE_DIR / "models/tokenizer"))
DATA_PATH = str(BASE_DIR / "data/combined_emails_with_natural_pii.csv")