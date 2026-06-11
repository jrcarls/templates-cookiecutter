import logging
from src.database.connection import DatabaseConnection

logger = logging.getLogger(__name__)


class BaseRepository:
    def __init__(self, db: DatabaseConnection):
        self._db = db

    def fetch_all(self, sql: str, params: tuple = None) -> list:
        with self._db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params or ())
            return cursor.fetchall()

    def fetch_one(self, sql: str, params: tuple = None) -> dict | None:
        with self._db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params or ())
            return cursor.fetchone()

    def execute(self, sql: str, params: tuple = None) -> None:
        with self._db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params or ())
            conn.commit()
            logger.info("Query executada com sucesso")
