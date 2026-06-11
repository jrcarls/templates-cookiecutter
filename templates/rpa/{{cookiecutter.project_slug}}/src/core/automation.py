import logging
from config.settings import USERNAME, PASSWORD
from src.pages.login_page import LoginPage
from src.pages.home_page import HomePage
from src.core.exceptions import AutomationError

logger = logging.getLogger(__name__)


class Automation:
    def __init__(self):
        self.login_page = LoginPage()
        self.home_page = HomePage()

    def run(self) -> None:
        logger.info("Iniciando automação")
        try:
            self._login()
            self._process()
        except AutomationError:
            logger.exception("Falha na execução da automação")
            raise
        finally:
            self._teardown()
        logger.info("Automação concluída")

    def _login(self) -> None:
        logger.info("Realizando login")
        self.login_page.open()
        self.login_page.do_login(USERNAME, PASSWORD)

    def _process(self) -> None:
        logger.info("Processando dados")
        # TODO: implemente a lógica de negócio aqui

    def _teardown(self) -> None:
        logger.info("Encerrando recursos")
        # TODO: feche drivers/conexões aqui
