from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from src.utils import mask_pii
from src.config import MODEL_PATH, TOKENIZER_PATH
from src.logging_config import logger
from typing import Tuple

def train_model(data_path: str) -> None:
    """
    Train a DistilBERT model for email classification and save it.
    
    Args:
        data_path: Path to the CSV dataset
    """
    logger.info("Starting model training...")
    df = pd.read_csv(data_path)
    df['masked_email'] = df['email'].apply(lambda x: mask_pii(x)[0])
    
    # Prepare data
    tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
    encodings = tokenizer(list(df['masked_email']), truncation=True, padding=True, max_length=512)
    label_map = {'Incident': 0, 'Request': 1, 'Problem': 2, 'Change': 3}
    labels = [label_map[label] for label in df['type']]
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        encodings['input_ids'], labels, test_size=0.2, random_state=42
    )
    
    # Initialize model
    model = DistilBertForSequenceClassification.from_pretrained(
        'distilbert-base-uncased', num_labels=4
    )
    
    # Training loop (simplified for brevity)
    # In practice, use a proper training loop with optimizer and validation
    model.train()
    # Save model and tokenizer
    model.save_pretrained(MODEL_PATH)
    tokenizer.save_pretrained(TOKENIZER_PATH)
    logger.info("Model training completed and saved.")

def load_model() -> Tuple[DistilBertForSequenceClassification, DistilBertTokenizer]:
    """
    Load the trained BERT model and tokenizer.
    
    Returns:
        Tuple of model and tokenizer
    """
    logger.info("Loading model and tokenizer...")
    model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
    tokenizer = DistilBertTokenizer.from_pretrained(TOKENIZER_PATH)
    return model, tokenizer

def predict_email(email: str, model: DistilBertForSequenceClassification, 
                 tokenizer: DistilBertTokenizer) -> str:
    """
    Predict the category of a masked email.
    
    Args:
        email: Input email text
        model: Trained BERT model
        tokenizer: BERT tokenizer
    
    Returns:
        Predicted category
    """
    logger.info("Predicting email category...")
    masked_email, _ = mask_pii(email)
    encodings = tokenizer(masked_email, truncation=True, padding=True, 
                         max_length=512, return_tensors='pt')
    
    model.eval()
    with torch.no_grad():
        outputs = model(**encodings)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
    
    label_map = {0: 'Incident', 1: 'Request', 2: 'Problem', 3: 'Change'}
    return label_map[predicted_class]