FROM python:3.11-slim

WORKDIR /app

# Hermes Agent インストールに Node.js が必要
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    ca-certificates \
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Hermes Agent（Grok OAuth: hermes auth add xai-oauth --no-browser）
RUN node --version && npm --version \
    && curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

ENV PATH="/usr/local/bin:/root/.local/bin:/root/.hermes/bin:${PATH}"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p data/drafts data/approved data/state /root/.hermes

ENV PORT=8080
EXPOSE 8080

# Railway: Volume を /root/.hermes にマウント推奨（OAuth トークン保持）
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]
