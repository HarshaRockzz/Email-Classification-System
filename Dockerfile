FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

COPY . .

ENV MODEL_PATH=/app/models/bert_model
ENV TOKENIZER_PATH=/app/models/tokenizer

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
