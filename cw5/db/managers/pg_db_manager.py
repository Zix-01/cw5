from cw5.db.managers.base import DBManager
import psycopg2


class PostgresDBManager(DBManager):

    def connect(self) -> None:
        if self.connection is None:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )

    def disconnect(self) -> None:
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_companies_and_vacancies_count(self):
        sql = """
            SELECT e.name, COUNT(*) as vacancies.count
            FROM employers as e
            LEFT JOIN vacancies as v ON e.id = v.employer_id
            GROUP BY e.name
        """
        self.connect()
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_avg_salary(self):
        sql = f"""
        SELECT AVG(v.salary_from), AVG(v.salary_to) FROM vacancies as v; 
        """
