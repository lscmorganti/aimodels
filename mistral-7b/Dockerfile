# Dockerfile: Container com suporte a CUDA e FastAPI usando Mistral + uv

FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

# 1-Instala dependências básicas do sistema
RUN apt-get update && apt-get install -y \
    python3.10 python3.10-dev python3.10-venv python3-pip \
    git curl build-essential libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# 1-Cria alias para python
RUN ln -s /usr/bin/python3.10 /usr/bin/python

# 1-Cria diretório da aplicação
WORKDIR /app

# 1-Copia tudo do projeto
COPY . /app

# 1-Adiciona o uv ao PATH
ENV PATH="/root/.local/bin:$PATH"

# 1-Instala o uv e as dependências do projeto
RUN curl -Ls https://astral.sh/uv/install.sh | bash && \
    uv venv && \
    uv pip install --upgrade pip && \
    uv pip install -r requirements.txt

# 1-Expõe a porta da API
EXPOSE 8000

# 1-Inicia a API com uvicorn dentro do venv
CMD ["uv", "pip", "run", "uvicorn", "app.main:app", "--", "--host", "0.0.0.0", "--port", "8000"]
