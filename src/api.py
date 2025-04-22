from src.models import predict_email, load_model
from src.utils import mask_pii
from src.logging_config import logger
from typing import Dict

def classify_email(email_body: str) -> Dict:
    """
    Classify an email and return the required JSON response.
    
    Args:
        email_body: Input email text
    
    Returns:
        Dictionary with classification results
    """
    logger.info("Processing email classification request...")
    try:
        # Load model and tokenizer
        model, tokenizer = load_model()
        
        # Mask PII
        masked_email, entities = mask_pii(email_body)
        
        # Classify email
        category = predict_email(masked_email, model, tokenizer)
        
        # Prepare response
        response = {
            "input_email_body": email_body,
            "list_of_masked_entities": entities,
            "masked_email": masked_email,
            "category_of_the_email": category
        }
        
        logger.info("Email classification completed successfully")
        return response
    except Exception as e:
        logger.error(f"Error in email classification: {str(e)}")
        raise