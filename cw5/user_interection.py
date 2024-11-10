from prettytable import PrettyTable

from cw5.db import PostgresDBManager


def print_employers():
    db_manager = PostgresDBManager()

    try:
        res = db_manager.get_companies_and_vacancies_count()

    finally:
        db_manager.disconnect()

    table = PrettyTable(field_names=['название компании', 'количество вакансий'])
    for data in res:
        table.add_row([data[0], data[1]])

    print(table)


def run_interaction():
    while True:
        print(
            'Выберите действие',
            '1 - список компаний и их вакансий',
            '2 - назад',
            sep='\n'
        )

        user_input = input()

        if user_input == '0':
            break
        elif user_input == '1':
            print_employers()
