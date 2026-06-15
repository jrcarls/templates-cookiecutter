# Python Project Templates

Coleção de templates [Cookiecutter](https://cookiecutter.readthedocs.io) para projetos Python, gerenciados com [uv](https://docs.astral.sh/uv/).

## Templates disponíveis

| Template | Descrição |
|---|---|
| [rpa](templates/rpa/) | Automação RPA com Playwright/Selenium |
| [api](templates/api/) | API REST com FastAPI |
| [django-htmx](templates/django-htmx/) | Web app Django com HTMX, Alpine.js, Tailwind CSS e DaisyUI |

## Requisitos

```bash
pip install cookiecutter
```

## Como usar

### RPA

```bash
cookiecutter https://github.com/jeanreis/templates-cookiecutter --directory templates/rpa
```

### API

```bash
cookiecutter https://github.com/jeanreis/templates-cookiecutter --directory templates/api
```

### Django + HTMX

```bash
cookiecutter https://github.com/jeanreis/templates-cookiecutter --directory templates/django-htmx
```

## Estrutura do repositório

```
templates/
├── rpa/          # Automação RPA com Playwright/Selenium
├── api/          # API REST com FastAPI
└── django-htmx/  # Web app Django com HTMX, Alpine.js, Tailwind e DaisyUI
```

## Detalhes dos templates

### rpa
Template para automação de processos com Playwright ou Selenium. Inclui estrutura de páginas (Page Object Model), repositórios, serviços e configuração de ambiente via `.env`.

### api
Template para APIs REST com FastAPI. Inclui estrutura de rotas, schemas, serviços, banco de dados com SQLAlchemy, health check e CI com GitHub Actions.

### django-htmx
Template para aplicações web completas com Django. Inclui:

- **Django 6.0.6** com configuração de produção pronta
- **Tailwind CSS 4.3.1 + DaisyUI 5.x** para estilização
- **HTMX 2.0.10** para interatividade sem JavaScript complexo
- **Alpine.js 3.15.12** para reatividade leve no frontend
- **django-allauth** para autenticação completa
- **django-cotton** para componentes reutilizáveis de template
- **django-htmx** para integração com `request.htmx` nas views
- **whitenoise** para servir estáticos em produção
- **django-debug-toolbar** para debug em desenvolvimento
- **django-browser-reload** para recarga automática do browser
- **django-environ** para variáveis de ambiente via `.env`
- **pytest-django** para testes

Veja a [documentação completa do template](templates/django-htmx/README.md).
