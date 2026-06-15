import platform
import secrets
import urllib.request
from pathlib import Path

# Gera SECRET_KEY e cria .env
secret_key = secrets.token_urlsafe(50)

with open(".env.example") as f:
    env_content = f.read()

env_content = env_content.replace("your-secret-key-here", secret_key)

with open(".env", "w") as f:
    f.write(env_content)

print("✔ .env criado com SECRET_KEY gerada automaticamente.")

# Baixa o binário do Tailwind CSS para a plataforma correta
TAILWIND_VERSION = "v4.3.1"

system = platform.system().lower()
machine = platform.machine().lower()

platform_map = {
    ("linux", "x86_64"): "tailwindcss-linux-x64",
    ("linux", "aarch64"): "tailwindcss-linux-arm64",
    ("darwin", "x86_64"): "tailwindcss-macos-x64",
    ("darwin", "arm64"): "tailwindcss-macos-arm64",
    ("windows", "amd64"): "tailwindcss-windows-x64.exe",
    ("windows", "x86_64"): "tailwindcss-windows-x64.exe",
}

binary_name = platform_map.get((system, machine))

if binary_name:
    url = f"https://github.com/tailwindlabs/tailwindcss/releases/download/{TAILWIND_VERSION}/{binary_name}"
    dest = Path("config/static/css/tailwindcss")

    print(f"  Baixando Tailwind CSS {TAILWIND_VERSION} para {system}/{machine}...")
    urllib.request.urlretrieve(url, dest)
    dest.chmod(0o755)
    print("✔ Tailwind CSS baixado.")
else:
    print(f"  Plataforma {system}/{machine} não reconhecida. Baixe o Tailwind manualmente:")
    print(f"  https://github.com/tailwindlabs/tailwindcss/releases/tag/{TAILWIND_VERSION}")

print("")
print(f"✔ Projeto '{{cookiecutter.project_name}}' pronto!")
print("")
print("Próximos passos:")
print("  uv sync")
print("  uv run python manage.py migrate")
print("  uv run python manage.py runserver")
