import logging
from src.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class HomePage(BasePage):
    def is_loaded(self) -> bool:
        # TODO: valide um elemento presente apenas na home
        return True
