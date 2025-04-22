# tests/test_utils.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))  # Add project root to path
from src.utils import mask_pii  # Import mask_pii function

import pytest

def test_mask_pii():
    email = "Subject: Issue\nHello, my name is John Doe, contact me at john@example.com."
    masked_email, entities = mask_pii(email)
    assert "[full_name]" in masked_email
    assert "[email]" in masked_email
    assert len(entities) == 2
    assert entities[0]["classification"] == "full_name"
    assert entities[0]["position"] == [33, 41]  # Adjust based on your response