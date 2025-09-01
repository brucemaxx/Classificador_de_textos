# Funções de pré-processamento de texto.

import re
import string
import nltk
from nltk.corpus import stopwords

# Certifique-se de que as stopwords foram baixadas
try:
    nltk.data.find('corpora/stowords')
except nltk.downloader.DownloadError:
    nltk.download('stopwords')
    
stop_words = set(stopwords.words('portuguese'))  

def preprocess_text(text: str) -> str:
    """
    Função para pré-processar o texto.
    Remova URLs, menções, pontuação e stopwords.
    """
    
    text = text.lower() # Converter para minúsculas
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE) # Remove URLs
    text = re.sub(r'@[A-Za-z0-9_]+', '', text) # Remove menções
    text = text.translate(str.maketrans('', '', string.punctuation)) # Remove pontuação
    text = ' '.join([word for word in text.split() if word not in stop_words]) # Remove stopwords
    return text