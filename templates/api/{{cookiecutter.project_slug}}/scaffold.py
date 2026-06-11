import sys
from pathlib import Path


def create_domain(name: str) -> None:
    domain_path = Path("app") / name
    domain_path.mkdir(exist_ok=True)

    has_db = Path("app/db").exists()

    files: dict[str, str] = {
        "__init__.py": "",
        "router.py": f"""\
from fastapi import APIRouter
from app.{name}.service import {name.capitalize()}Service

router = APIRouter()
service = {name.capitalize()}Service()


@router.get("")
def list_{name}s():
    return service.get_all()
""",
        "schemas.py": f"""\
from pydantic import BaseModel


class {name.capitalize()}Base(BaseModel):
    pass


class {name.capitalize()}Create({name.capitalize()}Base):
    pass


class {name.capitalize()}Response({name.capitalize()}Base):
    id: int

    model_config = {{"from_attributes": True}}
""",
        "service.py": f"""\
from app.{name}.schemas import {name.capitalize()}Response


class {name.capitalize()}Service:
    def get_all(self) -> list[{name.capitalize()}Response]:
        return []
""",
    }

    if has_db:
        files["models.py"] = f"""\
from app.db.session import Base
from sqlalchemy import Column, Integer, String


class {name.capitalize()}(Base):
    __tablename__ = "{name}s"

    id = Column(Integer, primary_key=True, index=True)
"""

    for filename, content in files.items():
        file_path = domain_path / filename
        if not file_path.exists():
            file_path.write_text(content)
            print(f"  created  {file_path}")
        else:
            print(f"  skipped  {file_path} (já existe)")

    print(f"\nDomínio '{name}' criado. Registre o router em app/main.py:")
    print(f"  from app.{name}.router import router as {name}_router")
    print(f'  app.include_router({name}_router, prefix="/api/v1/{name}", tags=["{name}"])')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: uv run python scaffold.py <nome_do_dominio>")
        sys.exit(1)

    create_domain(sys.argv[1].lower())
