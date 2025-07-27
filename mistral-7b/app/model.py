# 3-Carrega o modelo Mistral 7B com quantização 4bit e GPU, autenticando via variável .env

from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from huggingface_hub import login
from dotenv import load_dotenv
import os
import torch

# 3-Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# 3-Lê o token da Hugging Face
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not token:
    raise RuntimeError("Variável de ambiente HUGGINGFACEHUB_API_TOKEN não encontrada. Crie um arquivo .env com essa variável.")

login(token)

model_id = "mistralai/Mistral-7B-Instruct-v0.2"

# 3-Configura a quantização 4-bit (ideal para RTX 3060 com 12GB VRAM)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    llm_int8_threshold=6.0
)

# 3-Carrega o tokenizer e o modelo na GPU (se disponível)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    quantization_config=bnb_config,
    device_map="auto"
)

# 3-Função para gerar texto a partir de um prompt, com logs e tratamento de erro
def generate(prompt: str, max_tokens: int = 200) -> str | None:
    print(f"[DEBUG] Prompt recebido: {prompt}")

    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        print(f"[DEBUG] Inputs preparados para o modelo")

        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.95
        )

        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        print(f"[DEBUG] Resultado gerado: {result[:120]}...")
        return result

    except Exception as e:
        print(f"[ERRO] Falha ao gerar texto: {e}")
        return None
