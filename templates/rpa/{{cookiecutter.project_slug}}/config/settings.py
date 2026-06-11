from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / "logs"
OUTPUT_DIR = BASE_DIR / "output"

LOGS_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Timeouts (segundos)
DEFAULT_TIMEOUT = 30
LONG_TIMEOUT = 120

# Credenciais (via .env)
USERNAME = os.getenv("APP_USERNAME", "")
PASSWORD = os.getenv("APP_PASSWORD", "")

# URLs
BASE_URL = os.getenv("BASE_URL", "https://example.com")
