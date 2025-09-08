

### **Classificador de Texto (NLP) para Conteúdo Ofensivo e Spam**

Este projeto é uma API de backend construída em Python que utiliza técnicas de Processamento de Linguagem Natural (NLP) e Machine Learning para classificar textos. A principal funcionalidade é identificar e sinalizar automaticamente textos que podem conter linguagem ofensiva ou ser classificados como spam.

#### **Funcionalidades Principais**

-   **Classificação de Texto**: Recebe um texto e o classifica em uma das seguintes categorias: `ofensivo`, `spam` ou `não-ofensivo`.
    
-   **API RESTful**: Uma API simples e robusta, desenvolvida com **FastAPI**, que permite a comunicação com outras aplicações.
    
-   **Modularização**: O código é organizado em módulos (`main.py`, `model.py`, `utils.py`), facilitando a manutenção e a escalabilidade.
    
-   **Mensagens Amigáveis**: A API retorna mensagens formatadas para o usuário, indicando claramente a natureza do texto analisado.
    

----------

### **Tecnologias Utilizadas**

-   **Python 3.8+**: Linguagem de programação principal.
    
-   **FastAPI**: Framework web para construção da API.
    
-   **Scikit-learn**: Biblioteca de Machine Learning para treinamento do modelo.
    
-   **NLTK (Natural Language Toolkit)**: Usado para pré-processamento de texto e remoção de _stopwords_.
    
-   **Pandas**: Manipulação e processamento de dados.
    
-   **Joblib**: Para salvar e carregar o modelo de Machine Learning.
    
-   **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
    

----------

### **Estrutura do Projeto**

O projeto segue uma estrutura modular para melhor organização.

-   **`/app`**: Contém toda a lógica da aplicação.
    
    -   `main.py`: O ponto de entrada da API. Define os _endpoints_ e lida com as requisições.
        
    -   `model.py`: Responsável pela lógica de Machine Learning, incluindo o treinamento, salvamento e carregamento do modelo.
        
    -   `utils.py`: Módulo de utilidades que contém a função de pré-processamento de texto.
        
-   **`/data`**: Diretório opcional para armazenar o dataset de treinamento.
    
-   `text_classifier_model.pkl`: O modelo de Machine Learning treinado, salvo no formato binário.
    
-   `requirements.txt`: Lista todas as bibliotecas e suas versões para reprodução do ambiente.
    

----------

### **Guia de Instalação e Uso**

Siga os passos abaixo para configurar e rodar o projeto em sua máquina.

1.  **Clone o Repositório**
    
    Bash
    
    ```
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    
    ```
    
2.  **Crie um Ambiente Virtual (Opcional, mas Recomendado)**
    
    Bash
    
    ```
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    
    ```
    
3.  **Instale as Dependências**
    
    Bash
    
    ```
    pip install -r requirements.txt
    
    ```
    
    _Se você ainda não tem o arquivo `requirements.txt`, pode criá-lo com as bibliotecas que instalamos antes:_
    
    Bash
    
    ```
    pip freeze > requirements.txt
    
    ```
    
4.  Baixe os Recursos do NLTK
    
    Abra o console Python e execute o seguinte comando uma vez para baixar as stopwords necessárias:
    
    Bash
    
    ```
    python -c "import nltk; nltk.download('stopwords')"
    
    ```
    
5.  Treine o Modelo (Obrigatório na primeira execução)
    
    O projeto já vem com um modelo pronto, mas você pode retreiná-lo caso queira usar um dataset diferente. Para isso, execute a função train_and_save_model() do arquivo model.py diretamente:
    
    Bash
    
    ```
    python -c "from app.model import train_and_save_model; train_and_save_model()"
    
    ```
    
    _Este comando irá gerar o arquivo `text_classifier_model.pkl` na raiz do projeto._
    
6.  **Inicie a API**
    
    Bash
    
    ```
    uvicorn app.main:app --reload
    
    ```
    
    A API estará rodando em `http://127.0.0.1:8000`.
    

----------

### **Exemplos de Uso**

A documentação interativa da API está disponível em `http://127.0.0.1:8000/docs`. Você pode usar o endpoint `POST /predict/` para testar a classificação de textos.

**Exemplo de requisição (usando o `curl`):**

Bash

```
curl -X POST "http://127.0.0.1:8000/predict/" -H "Content-Type: application/json" -d '{
  "text": "Você é um idiota"
}'

```

**Exemplo de resposta:**

JSON

```
{
  "original_text": "Você é um idiota",
  "classification": "ofensivo",
  "is_offensive_or_spam": true,
  "response_message": "Atenção: Este texto pode conter linguagem ofensiva."
}

```

----------

### **Como este Projeto pode ser Usado?**

Esta API pode ser facilmente integrada a diversas aplicações para melhorar a moderação de conteúdo.

-   **Redes Sociais e Fóruns**: Filtrar automaticamente comentários ofensivos ou _trolls_, mantendo um ambiente online mais seguro.
    
-   **Plataformas de E-commerce**: Analisar avaliações de produtos para identificar linguagem inapropriada ou spam.
    
-   **Sistemas de Mensagens**: Implementar uma camada de segurança que avisa os usuários sobre textos potencialmente maliciosos ou indesejados (spam).
    
-   **E-mail Marketing**: Rastrear e-mails que são propensos a serem marcados como spam.
    

----------
