# Python Project Templates

Coleção de templates [Cookiecutter](https://cookiecutter.readthedocs.io) para projetos Python, gerenciados com [uv](https://docs.astral.sh/uv/).

## Templates disponíveis

| Template | Descrição |
|----------|-----------|
| [rpa](templates/rpa/) | Automação RPA com Playwright/Selenium |
| [api](templates/api/) | API REST com FastAPI |

## Requisitos

```bash
pip install cookiecutter
```

## Como usar

### RPA

```bash
cookiecutter https://github.com/jeanreis/templates-cookiecutter --directory templates/rpa
```

### API

```bash
cookiecutter https://github.com/jeanreis/templates-cookiecutter --directory templates/api
```

## Estrutura do repositório

```
templates/
├── rpa/        # Automação RPA
└── api/        # API com FastAPI
```
# templates-cookiecutter
