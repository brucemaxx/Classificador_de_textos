# Onde a API será definida

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model import load_model
from app.utils import preprocess_text

# Carrega o modelo quando a API é iniciada
model = load_model()

app = FastAPI(
    title="Classificador de Texto",
    description="API para detectar linguagem ofensiva ou spam em textos.",
    version="1.0.0"
)

# Definir o modelo de dados para a entrada da API
class TextPayLoad(BaseModel):
    text: str
    
@app.get("/")
def home():
    """Endpoint de boas-vindas da API."""
    return {"message": "Bem-vindo à API de Classificação de Texto. Acesse /docs para ver a documentação."}

@app.post("/predict/")
async def predict(payload: TextPayLoad):
    """
    Endpoint para classificar um texto e retornar uma mensagem amigável.
    """
    if not payload.text:
        raise HTTPException(status_code=400, detail="O campo 'text' não pode estar vazio.")
        
    # Pré-processa o texto de entrada
    processed_text = preprocess_text(payload.text)

    # Faz a predição
    prediction = model.predict([processed_text])[0]

    # Lógica para formatar a mensagem de retorno
    response_message = ""
    is_offensive_or_spam = False

    if prediction == 'ofensivo':
        response_message = "Atenção: O texto pode conter linguagem ofensiva."
        is_offensive_or_spam = True
    elif prediction == 'spam':
        response_message = "Atenção: Este texto foi classificado como spam."
        is_offensive_or_spam = True
    else:
        response_message = "Nenhuma ameaça ou conteúdo ofensivo foi detectado neste texto."
        
    return {
        "original_text": payload.text,
        "classification": prediction,
        "is_offensive_or_spam": is_offensive_or_spam,
        "response_message": response_message
    }