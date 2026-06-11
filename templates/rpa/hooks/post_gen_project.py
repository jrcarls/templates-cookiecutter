import shutil
from pathlib import Path

PROJECT_DIR = Path.cwd()

if "{{ cookiecutter.use_database }}" == "no":
    shutil.rmtree(PROJECT_DIR / "src" / "database")
    shutil.rmtree(PROJECT_DIR / "src" / "repositories")
