# tests/test_models.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.models import predict_email, load_model
import pytest

def test_predict_email():
    model, tokenizer = load_model()
    email = "Subject: Issue\nHello, my name is John Doe, contact me at john@example.com."
    category = predict_email(email, model, tokenizer)
    assert category in ["Incident", "Request", "Problem", "Change"]