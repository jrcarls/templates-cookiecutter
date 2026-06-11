from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "{{ cookiecutter.project_name }}"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    secret_key: str = "change-me"
    database_url: str = "sqlite:///./dev.db"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
