---
title: Email Classifier
emoji: 📧
colorFrom: blue
colorTo: purple
sdk: docker
app_file: Dockerfile
pinned: false
---

# Email Classification System
A cutting-edge email classification system designed for support teams to categorize emails into Incident, Request, Problem, or Change. Powered by DistilBERT for precise classification and SpaCy + Regex for secure PII masking, it ensures privacy compliance. Deployed on Hugging Face Spaces using FastAPI and Docker, this project leverages GitHub Actions for automated CI/CD, showcasing modern DevOps practices.

🌟 Key Features

Advanced Classification:
Utilizes DistilBERT for high-accuracy email categorization.
Supports four categories: Incident, Request, Problem, Change.


Secure PII Masking:
Masks sensitive data (emails, names, phone numbers) using SpaCy and Regex.
Non-LLM approach ensures compliance with privacy regulations.


Scalable API:
FastAPI powers a clean /classify POST endpoint.
Delivers structured JSON output for seamless integration.


Production-Ready:
Dockerized for consistent development and deployment environments.
Hosted on Hugging Face Spaces for reliable access.


Robust Testing:
Comprehensive unit tests for API, model, and PII masking using pytest.
Ensures system reliability and maintainability.


Automated CI/CD:
GitHub Actions enables rapid, error-free deployments.
Streamlines updates to Hugging Face Spaces.


Code Excellence:
Adheres to PEP8 standards with type hints.
Well-documented with structured logging via Loguru.




🛠️ Local Setup
🔧 Prerequisites

Python: 3.8 or higher
Docker: Recommended for containerized deployment
Git: For version control

📦 Installation Steps

Clone the Repository:
git clone https://github.com/HarshaRockzz/email-classification-system.git
cd email-classification-system


Set Up Virtual Environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt
python -m spacy download en_core_web_sm


Configure Environment:

Create a .env file in the root directory:
MODEL_PATH=./models/bert_model
TOKENIZER_PATH=./models/tokenizer




Prepare Dataset:

Ensure data/combined_emails_with_natural_pii.csv is available.


Train the Model:
python scripts/train_model.py


Run the API:
uvicorn src.app:app --host 0.0.0.0 --port 8000


Test the API:

Send a POST request to http://localhost:8000/classify:
{
  "email_body": "Subject: Issue\nHello, my name is John Doe, contact me at john@example.com."
}





🐳 Docker Setup

Build the Image:
docker build -t email-classifier .


Run the Container:
docker run -p 8000:8000 --env-file .env email-classifier


Access the API:

Navigate to http://localhost:8000.




🚀 Deployment on Hugging Face Spaces
🔧 Prerequisites

Hugging Face Account: For hosting the Space
GitHub Account: For version control and CI/CD
Hugging Face Space: Configured with Docker runtime

📤 Deployment Steps

Create a Space:

Visit Hugging Face Spaces.
Select Docker runtime.
Note the Space URL (e.g., https://huggingface.co/spaces/<your_username>/email-classifier).


Push Code to GitHub:
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your_username>/email-classification-system.git
git push -u origin main


Configure CI/CD:

Verify .github/workflows/deploy.yml exists.
Add HF_TOKEN in GitHub:
Go to Settings > Secrets and Variables > Actions > New Repository Secret.
Name: HF_TOKEN, Value: Your Hugging Face API token.




Trigger Deployment:

Push changes to the main branch.
Monitor progress in the GitHub Actions tab.


Verify Deployment:
curl -X POST https://<your_username>-email-classifier.hf.space/classify \
     -H "Content-Type: application/json" \
     -d '{"email_body": "Subject: Issue\nHello, my name is John Doe, contact me at john@example.com."}'




🔗 API Specification
POST /classify
Request
{
  "email_body": "string"
}

Response
{
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


🧪 Testing

Run Unit Tests:
pytest tests/


Purpose: Validates API functionality, model accuracy, and PII masking logic.

Coverage: Includes edge cases and error scenarios.



📈 Project Report
Explore docs/report.pdf for a detailed analysis, including:

Problem Statement: Objectives and use case.
Architecture: DistilBERT for classification, SpaCy + Regex for PII masking.
Metrics: Accuracy, F1-score, and performance benchmarks.
Challenges:
Handling multilingual emails.
Limited training data.


Solutions:
Data augmentation techniques.
Transfer learning with DistilBERT.




💡 Technical Highlights

Performance Optimization:
DistilBERT delivers fast, accurate classification.
Lightweight model for low-latency inference.


Privacy Compliance:
Non-LLM PII masking ensures regulatory adherence.
Secure handling of sensitive data.


Code Quality:
PEP8-compliant with type hints for maintainability.
Extensive documentation for collaboration.


Logging:
Structured logs via Loguru for debugging and monitoring.


