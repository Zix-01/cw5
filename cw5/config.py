import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings:
    DB_NAME = "cw5"
    DB_USER = os.environ["DB_USER"]
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_HOST = os.environ["DB_HOST"]
    DB_PORT = os.environ["DB_PORT"]
    EMPLOYEE_IDS_CONFIG_PATH = BASE_DIR.joinpath("employers_config.json")

    def get_employer_ids(self) -> list[int]:
        with self.EMPLOYEE_IDS_CONFIG_PATH.open() as f:
            data = json.load(f)

        return data['employers']['hh']


settings = Settings()
