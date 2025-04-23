---
title: Email Classifier
emoji: 📧
colorFrom: blue
colorTo: purple
sdk: docker
app_file: Dockerfile
pinned: false
---

# 📧 Email Classification System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![CI/CD](https://github.com/<your_username>/email-classification-system/actions/workflows/deploy.yml/badge.svg)

A production-grade **email classification API** for support teams, built using **DistilBERT**, **FastAPI**, and **Docker**. This system classifies incoming emails into _Incident_, _Request_, _Problem_, or _Change_ and securely masks sensitive user data using **SpaCy** and **Regex**. Deployed on **Hugging Face Spaces**, and integrated with **GitHub Actions** for seamless CI/CD.

---

## ✨ Features

### 🤖 Advanced Classification
- ⚡ Powered by **DistilBERT** for accurate NLP classification.
- 🎯 Supports four categories: `Incident`, `Request`, `Problem`, `Change`.

### 🛡️ Secure PII Masking
- 🔍 Uses **SpaCy** and **Regex** to identify and mask emails, names, phone numbers.
- ✅ Ensures compliance with privacy standards without relying on LLMs.

### 🚀 Production-Ready API
- ⚙️ Built with **FastAPI** and exposed via a clean `/classify` endpoint.
- 📦 Returns structured JSON responses for easy integration.

### 🐳 Containerized & Scalable
- 📦 Dockerized for consistent dev and prod environments.
- 🌐 Deployed on Hugging Face Spaces using Docker runtime.

### 🧪 Robust Testing
- ✔️ Comprehensive unit tests (model, masking, API) via **pytest**.
- 🧠 Covers edge cases, regressions, and failure modes.

### 🔄 Automated CI/CD
- ⚙️ Seamless deployments with **GitHub Actions**.
- 🔐 Hugging Face deployments triggered on push to `main`.

---

## 🛠️ Local Development Setup

### 🔧 Prerequisites
- Python 3.8+
- Docker
- Git

### 📦 Installation

```bash
git clone https://github.com/<your_username>/email-classification-system.git
cd email-classification-system

# Set up Python env
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
python -m spacy download en_core_web_sm
⚙️ Environment Configuration
Create a .env file in root:

env

MODEL_PATH=./models/bert_model
TOKENIZER_PATH=./models/tokenizer
📊 Prepare Dataset
Ensure data/combined_emails_with_natural_pii.csv is available.

🏋️‍♂️ Train the Model
bash

python scripts/train_model.py
▶️ Run the API Server
bash
uvicorn src.app:app --host 0.0.0.0 --port 8000
🧪 Example API Call
bash
curl -X POST http://localhost:8000/classify \
     -H "Content-Type: application/json" \
     -d '{"email_body": "Subject: Issue\nHello, my name is John Doe, contact me at john@example.com."}'
🐳 Docker Setup
📦 Build Image
bash
docker build -t email-classifier .
▶️ Run Container
bash
docker run -p 8000:8000 --env-file .env email-classifier
🚀 Deploying to Hugging Face Spaces
🔧 Prerequisites
 Hugging Face Account

 GitHub Account

 Hugging Face Space with Docker runtime

🚢 Deployment Instructions
Create a New Space:

Runtime: Docker

Note the URL: https://huggingface.co/spaces/<your_username>/email-classifier

Push Code to GitHub:

bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your_username>/email-classification-system.git
git push -u origin main
Set Up CI/CD:

Ensure .github/workflows/deploy.yml exists.

Add HF_TOKEN in GitHub Secrets:

Settings → Secrets → Actions → New Secret

Name: HF_TOKEN, Value: Your Hugging Face Token

Deploy:

Any push to main auto-triggers deployment.

🔍 API Specification
POST /classify

Request Body:

json
{
  "email_body": "string"
}
Response:

json
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
Run all tests using:
pytest tests/
Validates:

API endpoint

Classification accuracy

PII masking integrity

📊 Project Report
See docs/report.pdf for detailed analysis including:

🎯 Objectives: Automate email classification with privacy safeguards

🧠 Architecture: DistilBERT + SpaCy + Regex

📈 Metrics: Accuracy, F1-score, latency benchmarks

🚧 Challenges:

Multilingual support

Data scarcity

💡 Solutions:

Data augmentation

Transfer learning

💡 Technical Highlights

Area	Highlight
⚡ Performance	DistilBERT ensures high throughput & low-latency inference
🔐 Privacy	No-LLM PII masking using SpaCy + Regex
🧑‍💻 Code Quality	PEP8, type hints, modular design, Loguru for logging
🔁 DevOps	CI/CD via GitHub Actions, Dockerized deployment
