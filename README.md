Email Classification System
Overview
This project is an advanced email classification system designed for a support team. It classifies incoming support emails into categories (Incident, Request, Problem, Change) while masking personally identifiable information (PII) to ensure privacy. The system is built with modern technologies, including BERT for classification, FastAPI for the API, and Docker for deployment. It is deployed on Hugging Face Spaces and follows best practices for code quality, testing, and documentation.
Features

Advanced Classification: Uses DistilBERT for high-accuracy email categorization.
Robust PII Masking: Combines SpaCy and Regex to mask PII (e.g., names, emails, phone numbers) without LLMs.
FastAPI Endpoint: Exposes a POST /classify endpoint with strict JSON output format.
Error Handling: Comprehensive error handling with structured logging.
Testing: Unit tests for API, model, and PII masking using pytest.
Dockerized: Containerized for consistent local and production environments.
CI/CD: Automated testing and deployment via GitHub Actions to Hugging Face Spaces.

Project Structure
email-classification-system/
├── src/                           # Source code
│   ├── app.py                   # FastAPI application
│   ├── api.py                   # API endpoint logic
│   ├── models.py                # Model training and prediction
│   ├── utils.py                 # PII masking utilities
│   ├── config.py                # Configuration settings
│   └── logging_config.py        # Logging configuration
├── tests/                        # Unit tests
│   ├── test_api.py
│   ├── test_models.py
│   ├── test_utils.py
├── data/                         # Dataset
│   └── combined_emails_with_natural_pii.csv
├── models/                       # Trained model and tokenizer
├── scripts/                      # Utility scripts
│   └── train_model.py
├── Dockerfile                    # Docker configuration
├── requirements.txt              # Dependencies
├── README.md                     # This file
├── .gitignore                   # Git ignore file
├── .github/workflows/            # CI/CD workflows
└── setup.py                     # Package setup

Installation and Setup (Local)
Prerequisites

Python 3.8+
Docker (optional, for containerized setup)
Git

Steps

Clone the Repository:
git clone https://github.com/<your_username>/email-classification-system.git
cd email-classification-system


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt
python -m spacy download en_core_web_sm


Set Environment Variables:Create a .env file in the root directory:
MODEL_PATH=./models/bert_model
TOKENIZER_PATH=./models/tokenizer


Prepare Dataset:Ensure data/combined_emails_with_natural_pii.csv is in place.

Train the Model:
python scripts/train_model.py


Run the API:
uvicorn src.app:app --host 0.0.0.0 --port 8000


Test the API:Send a POST request to http://localhost:8000/classify using curl or Postman:
{
    "email_body": "Subject: Issue\nHello, my name is John Doe, contact me at john@example.com."
}



Docker Setup

Build the Docker Image:
docker build -t email-classifier .


Run the Container:
docker run -p 8000:8000 --env-file .env email-classifier


Access the API:The API will be available at http://localhost:8000.


Deployment (Hugging Face Spaces)
Prerequisites

Hugging Face account
GitHub account
Hugging Face Space with Docker support

Steps

Create a Hugging Face Space:

Go to Hugging Face Spaces.
Create a new Space with Docker as the runtime.
Note the Space URL (e.g., https://huggingface.co/spaces/<your_username>/email-classifier).


Push Code to GitHub:
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your_username>/email-classification-system.git
git push -u origin main


Configure GitHub Actions:

Ensure the .github/workflows/deploy.yml file is in the repository.
Add Hugging Face credentials (HF_TOKEN) as a GitHub Secret:
Go to your GitHub repository > Settings > Secrets and variables > Actions > New repository secret.
Add HF_TOKEN with your Hugging Face API token.




Trigger Deployment:

Push changes to the main branch to trigger the GitHub Actions workflow.
Monitor the deployment in the Actions tab of your GitHub repository.


Verify Deployment:

Access the Space URL and test the /classify endpoint.
Example curl command:curl -X POST https://<your_username>-email-classifier.hf.space/classify \
-H "Content-Type: application/json" \
-d '{"email_body": "Subject: Issue\nHello, my name is John Doe, contact me at john@example.com."}'





API Endpoint

POST /classify:
Input:{
    "email_body": "string"
}


Output:{
    "input_email_body": "string",
    "list_of_masked_entities": [
        {
            "position": [int, int],
            "classification": "string",
            "entity": "string"
        }
    ],
    "masked_email": "string",
    "category_of_the_email": "string"
}





Testing
Run unit tests to ensure reliability:
pytest tests/

Report
A 2-3 page report is included in the repository (docs/report.pdf) and covers:

Problem statement and objectives.
Approach (BERT for classification, SpaCy + Regex for PII masking).
Model training and evaluation (accuracy, F1-score).
Challenges (e.g., multilingual emails, small dataset) and solutions (e.g., robust PII detection, transfer learning).

Notes

The system is optimized for performance with DistilBERT, balancing accuracy and inference speed.
PII masking is non-LLM-based, ensuring compliance with assignment requirements.
Code follows PEP8 guidelines, with type hints and comprehensive comments.
Logging is implemented using Loguru for structured, debuggable output.

Contact
For issues or inquiries, contact <your_email> or open an issue on the GitHub repository.

Built with ❤️ by [Your Name]
