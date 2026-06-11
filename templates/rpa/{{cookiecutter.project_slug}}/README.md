# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Setup

```bash
# Clone e entre no diretório
cd {{ cookiecutter.project_slug }}

# Crie o ambiente com uv
uv sync

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais
```

## Executar

```bash
uv run python main.py
```

## Testes

```bash
uv run pytest
```

## Estrutura

```
├── config/         # Configurações e constantes
├── src/
│   ├── core/       # Orquestração principal
│   ├── database/   # Conexão com banco de dados
│   ├── pages/      # Page Objects (UI)
│   ├── repositories/ # Queries SQL (apenas se use_database=yes)
│   ├── services/   # Excel, e-mail, APIs
│   └── utils/      # Utilitários genéricos
├── tests/
├── logs/           # Gerado em runtime
└── output/         # Gerado em runtime
```

## Banco de dados

A camada de banco separa responsabilidades: `database/connection.py` gerencia a conexão e `repositories/` concentra as queries SQL.

Para criar um repositório específico, herde de `BaseRepository`:

```python
# src/repositories/pedido_repository.py
from src.repositories import BaseRepository


class PedidoRepository(BaseRepository):
    def buscar_pendentes(self) -> list:
        return self.fetch_all(
            "SELECT id, cliente, valor FROM pedidos WHERE status = %s",
            ("pendente",),
        )

    def marcar_processado(self, pedido_id: int) -> None:
        self.execute(
            "UPDATE pedidos SET status = %s WHERE id = %s",
            ("processado", pedido_id),
        )
```

Uso na automação:

```python
from src.database.connection import DatabaseConnection
from src.repositories.pedido_repository import PedidoRepository

db = DatabaseConnection()
repo = PedidoRepository(db)

for pedido in repo.buscar_pendentes():
    # processar pedido...
    repo.marcar_processado(pedido["id"])
```
