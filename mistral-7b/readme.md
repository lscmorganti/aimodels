# 🧠 Mistral 7B com FastAPI + Docker + GPU

Projeto para rodar o modelo `Mistral-7B-Instruct-v0.2` localmente com aceleração por GPU (RTX 3060 ou superior), usando quantização 4-bit e servindo uma API com FastAPI.

---

## 🇧🇷 Instruções em Português

### ✅ Pré-requisitos

- Docker + NVIDIA Container Toolkit
- GPU com suporte a CUDA (ex: RTX 3060 com 12GB)
- Conta no [Hugging Face](https://huggingface.co/) com acesso ao repositório `mistralai/Mistral-7B-Instruct-v0.2`

### 🔧 Setup

1. Crie o arquivo `.env` com seu token Hugging Face:
   ```
   HUGGINGFACEHUB_API_TOKEN=hf_abc123...
   ```

2. Construa a imagem:
   ```bash
   make build
   ```

3. Suba o serviço:
   ```bash
   make up
   ```

4. Acesse a API:
   - Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Endpoint `/generate`

### 🧪 Exemplo de uso

```bash
http POST :8000/generate prompt="Seu prompt" max_tokens:=100
```

### 📦 Cache dos modelos

O modelo é baixado automaticamente e armazenado em:

```
/var/lib/docker/volumes/mistral_cache/_data
```

---

## 🇺🇸 English Instructions

### ✅ Requirements

- Docker + NVIDIA Container Toolkit installed
- GPU with CUDA support (e.g., RTX 3060 12GB)
- Hugging Face account with access to [`mistralai/Mistral-7B-Instruct-v0.2`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)

### 🔧 Setup

1. Create a `.env` file with your token:
   ```
   HUGGINGFACEHUB_API_TOKEN=hf_abc123...
   ```

2. Build the container:
   ```bash
   make build
   ```

3. Start the service:
   ```bash
   make up
   ```

4. Access the API:
   - Swagger docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Endpoint: `/generate`

### 🧪 Example request

```bash
http POST :8000/generate prompt="Your prompt" max_tokens:=100
```

### 📦 Model cache

Model files are downloaded and stored in the volume:

```
/var/lib/docker/volumes/mistral_cache/_data
```

---

## 📂 Estrutura do projeto

```
.
├── app/
│   ├── main.py         # FastAPI app
│   └── model.py        # Carrega e executa o modelo
├── Dockerfile
├── docker-compose.yaml
├── makefile
├── requirements.txt
├── .env
```

---

## 👨‍💻 Autor

Lucas Morganti — projeto local com uso de LLM acelerada por GPU com infraestrutura Docker.