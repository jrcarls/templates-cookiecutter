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

Organizada por domínio — cada domínio concentra suas próprias rotas, schemas, serviço e modelo.

```
app/
├── core/
│   ├── config.py       # Settings via pydantic-settings
│   └── exceptions.py
├── db/
│   └── session.py      # Engine e sessão SQLAlchemy
├── health/             # Domínio de exemplo
│   ├── router.py
│   ├── schemas.py
│   └── service.py
└── main.py             # Entrypoint FastAPI
scaffold.py             # Gerador de novos domínios
```

## Adicionar um novo domínio

```bash
uv run python scaffold.py pedido
```

Cria `app/pedido/` com `router.py`, `schemas.py`, `service.py` e `models.py` (quando banco habilitado).

Após gerar, registre o router em `app/main.py`:

```python
from app.pedido.router import router as pedido_router

app.include_router(pedido_router, prefix="/api/v1/pedido", tags=["pedido"])
```
