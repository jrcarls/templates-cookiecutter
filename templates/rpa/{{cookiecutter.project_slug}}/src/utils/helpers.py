import re
from datetime import datetime


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "_", text)


def today_str(fmt: str = "%Y-%m-%d") -> str:
    return datetime.now().strftime(fmt)


def now_str(fmt: str = "%Y-%m-%d_%H-%M-%S") -> str:
    return datetime.now().strftime(fmt)


def parse_br_date(date_str: str) -> datetime:
    """Converte 'dd/mm/yyyy' para datetime."""
    return datetime.strptime(date_str, "%d/%m/%Y")


def format_cpf(cpf: str) -> str:
    digits = re.sub(r"\D", "", cpf)
    return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"
