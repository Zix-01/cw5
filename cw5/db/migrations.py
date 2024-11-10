from pathlib import Path

from cw5.config import settings
from cw5.db import PostgresDBManager


def create_database(db_name: str):
    db_manager = PostgresDBManager(db_name='postgres')
    db_manager.connect()

    try:
        with db_manager.connection.cursor() as cursor:
            cursor.execute(f'DROP DATABASE IF EXISTS {db_name}')
            cursor.execute(f'CREATE DATABASE {db_name}')

        db_manager.connection.commit()
    finally:
        db_manager.disconnect()


def apply_migrations():
    db_manager = PostgresDBManager()
    db_manager.connect()

    try:
        with db_manager.connection.cursor() as cursor:
            for migration in sorted(settings.MIGRATIONS_DIR.glob('*.sql')):
                cursor.execute(_read_migration(migration))

        db_manager.commit()
    finally:
        db_manager.disconnect()


def _read_migration(file_path: Path) -> str:
    with file_path.open(encoding='utf=8') as f:
        return f.read()
