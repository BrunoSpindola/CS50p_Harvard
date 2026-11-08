# CS50P — Introduction to Programming with Python

Resolução dos problem sets do curso **CS50's Introduction to Programming with Python** (Harvard / CS50), semanas 0 a 8.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)

## Sobre

Repositório de estudo com as minhas soluções dos problem sets do CS50P. O curso cobre os fundamentos de Python, desde funções e condicionais até testes automatizados, expressões regulares e programação orientada a objetos.

Cada problema foi validado com `check50` e enviado com `submit50`.

## Conteúdo

| Semana | Tema | Pasta |
|:------:|------|-------|
| 0 | Functions, Variables | [`week0`](./week0) |
| 1 | Conditionals | [`week1`](./week1) |
| 2 | Loops | [`week2`](./week2) |
| 3 | Exceptions | [`week3`](./week3) |
| 4 | Libraries | [`week4`](./week4) |
| 5 | Unit Tests | [`week5`](./week5) |
| 6 | File I/O | [`week6`](./week6) |
| 7 | Regular Expressions | [`week7`](./week7) |
| 8 | Object-Oriented Programming | [`week8`](./week8) |

## Estrutura

```
.
├── week0/
│   ├── indoor/
│   │   └── indoor.py
│   └── playback/
│       └── playback.py
├── week1/
├── ...
└── week8/
    ├── seasons/
    │   ├── seasons.py
    │   └── test_seasons.py
    └── ...
```

Cada problema fica em sua própria pasta, com o arquivo principal e, quando pedido, o arquivo de testes (`test_*.py`).

## Tópicos praticados

- Funções, variáveis e tipos de dados
- Condicionais e laços de repetição
- Tratamento de exceções
- Bibliotecas padrão e de terceiros (`random`, `sys`, `requests`, etc.)
- Testes unitários com `pytest`
- Leitura e escrita de arquivos (CSV, texto)
- Expressões regulares (`re`)
- Classes, objetos, herança e *dunder methods*

## Como executar

```bash
# clonar o repositório
git clone https://github.com/BrunoSpindola/CS50p_Harvard.git
cd CS50p_Harvard

# executar um problema
python week0/playback/playback.py

# rodar os testes de um problema
pip install pytest
pytest week8/seasons/test_seasons.py
```

## Aviso de honestidade acadêmica

Este repositório documenta meu aprendizado. Se você estiver cursando o CS50P, tente resolver os problemas por conta própria: copiar soluções vai contra a [política de honestidade acadêmica do CS50](https://cs50.harvard.edu/python/honesty/) e tira o objetivo do curso.

## Autor

**Bruno Spindola**
[LinkedIn](https://linkedin.com/in/bruno-spindola) · [GitHub](https://github.com/BrunoSpindola)

## Referências

- [CS50P — Harvard](https://cs50.harvard.edu/python/)
