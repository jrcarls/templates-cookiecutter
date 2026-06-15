# cookiecutter-django-htmx

Template Django com stack moderna de frontend, pronto para desenvolvimento e produção.

## Stack

### Backend
| Pacote | Versão |
|---|---|
| Python | >= 3.12 |
| Django | 6.0.6 |
| django-environ | 0.13.0 |
| django-allauth | 65.18.0 |
| django-htmx | 1.27.0 |
| django-cotton | 2.7.2 |
| django-browser-reload | 1.21.0 |
| django-debug-toolbar | 6.3.0 |
| whitenoise | 6.12.0 |
| pytest-django | 4.12.0 |

### Frontend
| Lib | Versão |
|---|---|
| Tailwind CSS | 4.3.1 |
| DaisyUI | 5.x |
| HTMX | 2.0.10 |
| Alpine.js | 3.15.12 |

## Funcionalidades

- **django-environ** — variáveis de ambiente via `.env`, sem expor `SECRET_KEY` no código
- **django-allauth** — autenticação completa (login, registro, recuperação de senha)
- **django-htmx** — integração HTMX com acesso a `request.htmx` nas views
- **django-cotton** — componentes reutilizáveis de template com sintaxe `<c-componente />`
- **django-browser-reload** — recarga automática do browser em desenvolvimento
- **django-debug-toolbar** — painel de debug com queries SQL, cache e tempo de resposta
- **whitenoise** — serve arquivos estáticos em produção com compressão e cache
- **pytest-django** — testes com pytest
- **Tailwind CSS + DaisyUI** — utilitários CSS + componentes prontos
- **HTMX** — interatividade sem escrever JavaScript
- **Alpine.js** — reatividade leve no frontend

## Requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recomendado) ou pip
- cookiecutter

```bash
pip install cookiecutter
```

## Uso

### A partir do GitHub
```bash
cookiecutter gh:seu-usuario/cookiecutter-django-htmx
```

### A partir do caminho local
```bash
cookiecutter /caminho/para/cookiecutter-django-htmx
```

O cookiecutter vai perguntar:
```
project_name [My Project]: Meu Projeto
project_slug [meu_projeto]:
```

## Primeiros passos após gerar o projeto

```bash
cd nome-do-projeto

# Instalar dependências
uv sync

# Rodar migrations
uv run python manage.py migrate

# Criar superusuário (opcional)
uv run python manage.py createsuperuser

# Iniciar servidor
uv run python manage.py runserver
```

O arquivo `.env` é gerado automaticamente com uma `SECRET_KEY` segura.

## Estrutura do projeto

```
meu_projeto/
├── config/
│   ├── static/
│   │   ├── css/
│   │   │   ├── input.css       # entrada do Tailwind
│   │   │   ├── output.css      # CSS compilado (Tailwind + DaisyUI)
│   │   │   ├── tailwindcss     # binário do Tailwind
│   │   │   ├── daisyui.mjs
│   │   │   └── daisyui-theme.mjs
│   │   └── js/
│   │       ├── htmx.min.js
│   │       └── alpine.min.js
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│   └── asgi.py
├── templates/
│   ├── cotton/             # componentes django-cotton
│   └── index.html
├── .env                    # gerado automaticamente
├── .env.example
├── .gitignore
├── manage.py
└── pyproject.toml
```

## Recompilar o CSS

Quando adicionar novas classes Tailwind ou alterar o `input.css`:

```bash
./config/static/css/tailwindcss -i config/static/css/input.css -o config/static/css/output.css --watch
```

## Variáveis de ambiente

| Variável | Descrição | Padrão |
|---|---|---|
| `SECRET_KEY` | Chave secreta do Django | gerada automaticamente |
| `DEBUG` | Modo debug | `True` |
| `ALLOWED_HOSTS` | Hosts permitidos (separados por vírgula) | `localhost,127.0.0.1` |

## Autenticação

As rotas do django-allauth ficam disponíveis em `/accounts/`:

| Rota | Descrição |
|---|---|
| `/accounts/login/` | Login |
| `/accounts/logout/` | Logout |
| `/accounts/signup/` | Registro |
| `/accounts/password/reset/` | Recuperação de senha |

## Testes

```bash
uv run pytest
```

## Produção

Antes de subir para produção:

1. Definir `DEBUG=False` no `.env`
2. Definir `ALLOWED_HOSTS` com o domínio real
3. Rodar `uv run python manage.py collectstatic`
