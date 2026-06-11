import pytest
from unittest.mock import patch, MagicMock
from src.core.automation import Automation


class TestAutomation:
    def test_run_calls_login_and_process(self):
        bot = Automation()
        with (
            patch.object(bot, "_login") as mock_login,
            patch.object(bot, "_process") as mock_process,
            patch.object(bot, "_teardown"),
        ):
            bot.run()
            mock_login.assert_called_once()
            mock_process.assert_called_once()

    def test_teardown_runs_even_on_error(self):
        bot = Automation()
        with (
            patch.object(bot, "_login", side_effect=Exception("falha")),
            patch.object(bot, "_teardown") as mock_teardown,
        ):
            with pytest.raises(Exception):
                bot.run()
            mock_teardown.assert_called_once()
