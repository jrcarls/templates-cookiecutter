import os
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)


class DatabaseConnection:
    def __init__(self):
        self.connection_string = os.getenv("DATABASE_URL", "")
        self._conn = None

    def connect(self):
        # TODO: substitua pelo driver correto (psycopg2, pyodbc, etc.)
        logger.info("Conectando ao banco de dados")

    def disconnect(self):
        if self._conn:
            self._conn.close()
            logger.info("Conexão encerrada")

    @contextmanager
    def get_connection(self):
        self.connect()
        try:
            yield self._conn
        finally:
            self.disconnect()
