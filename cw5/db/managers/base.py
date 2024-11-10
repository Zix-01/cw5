from abc import ABC, abstractmethod
from psycopg2 import extensions

from cw5.config import settings


class DBManager(ABC):

    def __init__(self, db_name: str = settings.DB_NAME):
        self.dbname = db_name
        self.user = settings.DB_USER
        self.password = settings.DB_USER
        self.host = settings.DB_USER
        self.port = settings.DB_USER
        self.connection: extensions.connection | None = None

    @abstractmethod
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass
