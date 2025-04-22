import re
import spacy
from typing import Tuple, List, Dict
from src.logging_config import logger

nlp = spacy.load("en_core_web_sm")

def mask_pii(email: str) -> Tuple[str, List[Dict]]:
    """
    Mask PII in the email and return masked email with entity details.
    
    Args:
        email: Input email text
    
    Returns:
        Tuple of masked email and list of entities
    """
    logger.info("Masking PII in email...")
    entities = []
    masked_email = email
    
    # Regex patterns for structured PII
    patterns = {
        "email": (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', "[email]"),
        "phone_number": (r'\+?\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,4}', "[phone_number]"),
        "credit_debit_no": (r'\d{4}[-.\s]?\d{4}[-.\s]?\d{4}[-.\s]?\d{4}', "[credit_debit_no]"),
        "cvv_no": (r'\b\d{3,4}\b', "[cvv_no]"),
        "expiry_no": (r'\b(0[1-9]|1[0-2])/(\d{2}|\d{4})\b', "[expiry_no]"),
        "aadhar_num": (r'\d{4}\s?\d{4}\s?\d{4}', "[aadhar_num]"),
        "dob": (r'\b(\d{1,2}[-/\s]\d{1,2}[-/\s]\d{2,4})\b', "[dob]")
    }
    
    # Apply Regex masking
    for entity_type, (pattern, placeholder) in patterns.items():
        matches = re.finditer(pattern, masked_email)
        for match in matches:
            start, end = match.start(), match.end()
            original = match.group()
            entities.append({
                "position": [start, end],
                "classification": entity_type,
                "entity": original
            })
            masked_email = masked_email[:start] + placeholder + masked_email[end:]
    
    # Apply SpaCy for names
    doc = nlp(masked_email)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            start, end = ent.start_char, ent.end_char
            original = ent.text
            entities.append({
                "position": [start, end],
                "classification": "full_name",
                "entity": original
            })
            masked_email = masked_email[:start] + "[full_name]" + masked_email[end:]
    
    # Sort entities by position
    entities.sort(key=lambda x: x["position"][0])
    logger.info(f"Found {len(entities)} PII entities")
    return masked_email, entities

def demask_email(masked_email: str, entities: List[Dict]) -> str:
    """
    Restore the original email by replacing masked entities.
    
    Args:
        masked_email: Email with PII masked
        entities: List of PII entities
    
    Returns:
        Demasked email
    """
    logger.info("Demasking email...")
    demasked_email = masked_email
    for entity in reversed(entities):
        start, end = entity["position"]
        placeholder = f"[{entity['classification']}]"
        demasked_email = demasked_email[:start] + entity["entity"] + demasked_email[end:]
    return demasked_email