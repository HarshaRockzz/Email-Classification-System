from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from src.api import classify_email
from src.logging_config import logger
import uvicorn

app = FastAPI(
    title="Email Classification API",
    description="Classifies support emails and masks PII",
    version="1.0.0"
)

class EmailInput(BaseModel):
    email_body: str

@app.post("/classify", response_model=Dict)
async def classify(email_input: EmailInput):
    try:
        logger.info(f"Received email for classification: {email_input.email_body[:50]}...")
        result = classify_email(email_input.email_body)
        logger.info(f"Email classified as {result['category_of_the_email']}")
        return result
    except Exception as e:
        logger.error(f"Error processing email: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)