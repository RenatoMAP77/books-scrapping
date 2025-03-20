# books-scrapping
Aplicação de web scrapping que coleta os dados filtrados de livros do site [Books to Scrape](http://books.toscrape.com/) e salva em um arquivo json.



## Tecnologias 
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Scrapy](https://img.shields.io/badge/scrapy-%2360a839.svg?style=for-the-badge&logo=scrapy&logoColor=d1d2d3)

## Funcionalidades
- Coletar título, preço e avaliação dos livros
- Filtrar os livros apenas por livros na faixa de preço selecionada (<£50.00), e com a avaliação mínima de 3 estrelas.
- Salvar os dados coletados em um arquivo json.

Exemplo de resposta json:
Exemplo de resposta:
```json
[
    {
        "title": "Bleach, Vol. 1: Strawberry and the Soul Reapers (Bleach #1)",
        "price": "£34.65",
        "stars": "Five"
    },
    {
        "title": "A Spy's Devotion (The Regency Spies of London #1)",
        "price": "£16.97",
        "stars": "Five"
    }
]
```

## Dependências

Este projeto utiliza as seguintes bibliotecas:

- `scrapy`

As dependências do projeto podem ser instaladas utilizando pip com o seguinte comando:

```bash
pip install scrapy
```

## Executando o projeto

### Criando um ambiente virtual

Para criar um ambiente virtual, execute o seguinte comando:

```bash
python3 -m venv .venv
```
### Ativando o ambiente virtual
Para ativar o ambiente virtual use o seguinte comando:

MAC/LINUX:

```bash
source .venv/bin/activate
```

WINDOWS:

```bash
.venv\Scripts\activate
```
### Executar o projeto

Para executar o projeto, execute o seguinte comando:

```bash
python books.py
```

# Obrigado!

