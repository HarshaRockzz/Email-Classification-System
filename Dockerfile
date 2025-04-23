# Stage 1: Build dependencies
FROM python:3.8-slim AS builder

# Install required build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

# Stage 2: Runtime
FROM python:3.8-slim

# Install runtime dependencies (curl for health checks)
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /root/.spacy /root/.spacy

# Copy the project code
COPY . .

# Set environment variables
ENV MODEL_PATH=/app/models/bert_model
ENV TOKENIZER_PATH=/app/models/tokenizer
ENV TRANSFORMERS_CACHE=/app/cache/huggingface
ENV HF_HOME=/app/cache/huggingface

# Create the cache directory
RUN mkdir -p /app/cache/huggingface

# Expose the port
EXPOSE 7860

# Run FastAPI with Uvicorn on port 7860
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "7860"]
