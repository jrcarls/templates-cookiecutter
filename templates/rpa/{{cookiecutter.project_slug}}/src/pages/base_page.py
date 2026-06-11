import logging
from config.settings import DEFAULT_TIMEOUT

logger = logging.getLogger(__name__)


class BasePage:
    def __init__(self, driver=None):
        self.driver = driver
        self.timeout = DEFAULT_TIMEOUT

    def click(self, locator):
        logger.debug("Clicando em %s", locator)
        # TODO: implemente com seu framework (Selenium, Playwright, pywinauto)

    def type_text(self, locator, text: str):
        logger.debug("Digitando em %s", locator)

    def wait_for_element(self, locator):
        logger.debug("Aguardando elemento %s", locator)

    def take_screenshot(self, name: str = "screenshot"):
        from config.settings import OUTPUT_DIR
        path = OUTPUT_DIR / f"{name}.png"
        logger.info("Screenshot salvo em %s", path)
        # TODO: self.driver.save_screenshot(str(path))
        return path
