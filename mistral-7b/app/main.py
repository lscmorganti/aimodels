# 3-Cria uma API com FastAPI para rodar inferências no modelo
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import generate

app = FastAPI()

class Prompt(BaseModel):
    prompt: str
    max_tokens: int = 200

@app.post("/generate")
def infer(prompt: Prompt):
    result = generate(prompt.prompt, prompt.max_tokens)
    if result is None:
        raise HTTPException(status_code=500, detail="Falha na geração do texto.")
    return {"response": result}
