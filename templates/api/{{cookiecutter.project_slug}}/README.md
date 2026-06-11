# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setup

```bash
uv sync
cp .env.example .env
```

Edite o `.env` com as credenciais do banco e a `SECRET_KEY` antes de rodar.

## Executar

```bash
uv run uvicorn app.main:app --reload
```

- API: `http://localhost:8000`
- Docs (Swagger): `http://localhost:8000/api/v1/docs`
- Health check: `http://localhost:8000/api/v1/health`

## Testes

```bash
uv run pytest
uv run pytest --cov=app --cov-report=term-missing  # com cobertura
```

## Variáveis de ambiente

| Variável       | Padrão               | Descrição                  |
|----------------|----------------------|----------------------------|
| `DEBUG`        | `false`              | Modo debug                 |
| `SECRET_KEY`   | —                    | Chave secreta da aplicação |
| `DATABASE_URL` | `sqlite:///./dev.db` | URL de conexão com o banco |

## Estrutura

Organizada por domínio — cada domínio concentra suas próprias rotas, schemas, serviço, modelo e repositório.

```
{{ cookiecutter.project_slug }}/
├── app/
│   ├── core/
│   │   ├── config.py       # Settings via pydantic-settings
│   │   └── exceptions.py   # Exceções customizadas
│   ├── db/
│   │   └── session.py      # Engine, sessão e get_db (SQLAlchemy)
│   ├── health/             # Domínio mínimo de exemplo (sem banco)
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── service.py
│   └── main.py             # Entrypoint FastAPI
├── tests/
│   └── test_health.py
├── .env.example
├── scaffold.py             # Gerador de novos domínios
└── pyproject.toml
```

Domínios que interagem com o banco seguem o padrão completo:

```
app/<dominio>/
├── router.py       # rotas HTTP + injeção de Session via Depends
├── schemas.py      # DTOs Pydantic (request/response)
├── service.py      # regras de negócio
├── models.py       # modelo ORM (SQLAlchemy)
└── repository.py   # acesso ao banco (queries)
```

## Adicionar um novo domínio

```bash
uv run python scaffold.py pedido
```

Detecta se `app/db/` existe e gera os arquivos correspondentes:

- **Sem banco:** `router.py`, `schemas.py`, `service.py`
- **Com banco:** todos acima + `models.py` + `repository.py`

Após gerar, registre o router em `app/main.py`:

```python
from app.pedido.router import router as pedido_router

app.include_router(pedido_router, prefix="/api/v1/pedido", tags=["pedido"])
```

## CI

O pipeline roda automaticamente nos pushes para `main`/`master` e pull requests via GitHub Actions (`.github/workflows/ci.yml`). Executa os testes com relatório de cobertura.
