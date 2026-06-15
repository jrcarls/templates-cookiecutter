import secrets
import shutil

# Gera SECRET_KEY
secret_key = secrets.token_urlsafe(50)

# Cria .env a partir do .env.example
with open(".env.example") as f:
    env_content = f.read()

env_content = env_content.replace("your-secret-key-here", secret_key)

with open(".env", "w") as f:
    f.write(env_content)

print("✔ .env criado com SECRET_KEY gerada automaticamente.")
print("✔ Projeto '{{cookiecutter.project_name}}' pronto!")
print("")
print("Próximos passos:")
print("  uv sync")
print("  uv run python manage.py migrate")
print("  uv run python manage.py runserver")
