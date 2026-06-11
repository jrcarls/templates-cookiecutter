import sys
from pathlib import Path


def create_domain(name: str) -> None:
    domain_path = Path("app") / name
    domain_path.mkdir(exist_ok=True)

    has_db = Path("app/db").exists()
    cap = name.capitalize()

    if has_db:
        router_content = f"""\
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.{name}.service import {cap}Service

router = APIRouter()


@router.get("")
def list_{name}s(db: Session = Depends(get_db)):
    return {cap}Service(db).get_all()
"""
        service_content = f"""\
from sqlalchemy.orm import Session
from app.{name}.repository import {cap}Repository
from app.{name}.schemas import {cap}Response


class {cap}Service:
    def __init__(self, db: Session):
        self.repository = {cap}Repository(db)

    def get_all(self) -> list[{cap}Response]:
        return self.repository.get_all()
"""
    else:
        router_content = f"""\
from fastapi import APIRouter
from app.{name}.service import {cap}Service

router = APIRouter()
service = {cap}Service()


@router.get("")
def list_{name}s():
    return service.get_all()
"""
        service_content = f"""\
from app.{name}.schemas import {cap}Response


class {cap}Service:
    def get_all(self) -> list[{cap}Response]:
        return []
"""

    files: dict[str, str] = {
        "__init__.py": "",
        "router.py": router_content,
        "schemas.py": f"""\
from pydantic import BaseModel


class {cap}Base(BaseModel):
    pass


class {cap}Create({cap}Base):
    pass


class {cap}Response({cap}Base):
    id: int

    model_config = {{"from_attributes": True}}
""",
        "service.py": service_content,
    }

    if has_db:
        files["models.py"] = f"""\
from app.db.session import Base
from sqlalchemy import Column, Integer, String


class {cap}(Base):
    __tablename__ = "{name}s"

    id = Column(Integer, primary_key=True, index=True)
"""
        files["repository.py"] = f"""\
from sqlalchemy.orm import Session
from app.{name}.models import {cap}


class {cap}Repository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[{cap}]:
        return self.db.query({cap}).all()

    def get_by_id(self, id: int) -> {cap} | None:
        return self.db.query({cap}).filter({cap}.id == id).first()

    def create(self, obj: {cap}) -> {cap}:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
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
