# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setup

```bash
uv sync
cp .env.example .env
```

## Executar

```bash
uv run uvicorn app.main:app --reload
```

Acesse a documentação em: `http://localhost:8000/api/v1/docs`

## Testes

```bash
uv run pytest
```

## Estrutura

```
app/
├── api/v1/
│   ├── endpoints/   # Rotas organizadas por recurso
│   └── router.py    # Agrega todos os endpoints
├── core/
│   ├── config.py    # Settings via pydantic-settings
│   └── exceptions.py
├── db/
│   └── session.py   # Engine e sessão SQLAlchemy
├── models/          # Modelos ORM
├── schemas/         # Schemas Pydantic (request/response)
├── services/        # Lógica de negócio
└── main.py          # Entrypoint FastAPI
```
