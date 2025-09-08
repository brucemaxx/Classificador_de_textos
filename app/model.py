# Lógica de treinamento e carregamento do modelo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib
from .utils import preprocess_text

def train_and_save_model():
    """
    Treina o modelo de classificação e o salva no disco.
    """
    # Dados de exemplo - SUBSTITUA POR UM DATASET REAL!
    data = {'text': [
        "Olá, como você está?",
        "Que dia lindo hoje!",
        "Você é um idiota",
        "Compre agora! Oferta especial!",
        "Reunião amanhã às 10h",
        "Isso é uma porcaria, não comprem!",
        "Mensagem de texto normal para testar"
    ], 'label': [
        'nao-ofensivo', 'nao-ofensivo', 'ofensivo', 'spam', 'nao-ofensivo', 'ofensivo', 'nao-ofensivo'
    ]}
    df = pd.DataFrame(data)

    # Pré-processa os textos antes de treinar
    df['text_processed'] = df['text'].apply(preprocess_text)

    X_train, X_test, y_train, y_test = train_test_split(
        df['text_processed'], df['label'], test_size=0.2, random_state=42
    )

    # Cria o pipeline do modelo
    text_classifier = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', MultinomialNB())
    ])

    # Treina o modelo
    text_classifier.fit(X_train, y_train)

    # Salva o modelo treinado
    joblib.dump(text_classifier, 'text_classifier_model.pkl')
    print("Modelo treinado e salvo como 'text_classifier_model.pkl'")

def load_model():
    """
    Carrega o modelo de classificação a partir do arquivo.
    """
    try:
        model = joblib.load('text_classifier_model.pkl')
        return model
    except FileNotFoundError:
        print("Modelo não encontrado. Treinando um novo modelo...")
        train_and_save_model()
        return joblib.load('text_classifier_model.pkl')