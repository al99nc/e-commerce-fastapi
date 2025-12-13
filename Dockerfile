FROM python:3.12.12 AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN python -m venv .venv
COPY requirements.txt ./
RUN .venv/bin/pip install -r requirements.txt

FROM python:3.12.12-slim

# Move ENV declarations HERE in the final stage
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DATABASE_URL="postgresql://postgres:UuZJvjmXBADnWpPwVqYYenGvuygjYlah@maglev.proxy.rlwy.net:11499/railway" \
    PORT=8080

WORKDIR /app

COPY --from=builder /app/.venv .venv/
COPY . .

CMD ["/app/.venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]