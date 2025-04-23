FROM python:3.8-slim

# ✅ Install required build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ✅ Set working directory
WORKDIR /app

# ✅ Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

# ✅ Copy the project code
COPY . .

# ✅ Set environment variables
ENV MODEL_PATH=/app/models/bert_model
ENV TOKENIZER_PATH=/app/models/tokenizer

# ✅ Run FastAPI with Uvicorn
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
