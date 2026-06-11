import logging
import sys
from config.settings import LOGS_DIR
from src.core.automation import Automation
from src.utils.helpers import now_str

LOG_FILE = LOGS_DIR / f"run_{now_str()}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


def main():
    logger.info("=== Iniciando {{ cookiecutter.project_name }} ===")
    try:
        bot = Automation()
        bot.run()
    except Exception:
        logger.exception("Execução encerrada com erro")
        sys.exit(1)
    logger.info("=== Execução finalizada com sucesso ===")


if __name__ == "__main__":
    main()
