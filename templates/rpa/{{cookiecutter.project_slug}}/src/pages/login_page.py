import logging
from src.pages.base_page import BasePage
from src.core.exceptions import LoginError
from config.settings import BASE_URL

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    URL = f"{BASE_URL}/login"

    def open(self):
        logger.info("Abrindo página de login: %s", self.URL)
        # TODO: self.driver.get(self.URL)

    def do_login(self, username: str, password: str):
        logger.info("Autenticando usuário: %s", username)
        try:
            self.type_text("#username", username)
            self.type_text("#password", password)
            self.click("#btn-login")
        except Exception as exc:
            raise LoginError("Falha ao realizar login") from exc
