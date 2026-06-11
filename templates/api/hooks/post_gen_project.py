import shutil
from pathlib import Path

PROJECT_DIR = Path.cwd()

if "{{ cookiecutter.use_database }}" == "no":
    shutil.rmtree(PROJECT_DIR / "app" / "db")
    shutil.rmtree(PROJECT_DIR / "app" / "models")
