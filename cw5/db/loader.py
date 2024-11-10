from cw5.api_clients import HHApiClient
from cw5.config import settings
from cw5.db import PostgresDBManager

api_client = HHApiClient()


def load_employers():
    employer_ids = settings.get_employer_ids()
    sql = """
        INSERT INTO employers(id, name, urls, site_url, region)
        VALUES(%s, %s, %s, %s, %s);
    """

    db_manager = PostgresDBManager()
    db_manager.connect()

    try:
        with db_manager.connection.cursor() as cursor:
            for employer_id in employer_ids:
                emp = api_client._get_employer_info(employer_id)
                cursor.execute(sql, (emp.id, emp.name, emp.url, emp.website, emp.region))

            db_manager.commit()
    finally:
        db_manager.disconnect()

def load_vacancies():
    employer_ids = settings.get_employer_ids()
    sql = """
        INSERT INTO vacancies(id, name, urls, type, salary_from, salary_to, employer_id)
        VALUES(%s, %s, %s, %s, %s, %s, %s);
    """

    db_manager = PostgresDBManager()
    db_manager.connect()

    try:
        with db_manager.connection.cursor() as cursor:
            for employer_id in employer_ids:
                vacancies = api_client._get_employer_vacancies(employer_id)
                data = (
                    (vac.id, vac.name, vac.link, vac.type.name, vac.salary_from, vac.salary_to, vac.employer_id)
                    for vac in vacancies
                )
                cursor.executemany(sql, data)

            db_manager.commit()
    finally:
        db_manager.disconnect()
