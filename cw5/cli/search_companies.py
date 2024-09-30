from cw5.api_clients import HHApiClient, client
from prettytable import PrettyTable

hh_client = HHApiClient()


# функция для поиска компаний по ключевому слову с выводом в виде таблицы
def searching_companies():
    print('Введите ключевое слово для поиска работодателя: ')
    search = input()

    employers = hh_client.search_employers(search)

    if not employers:
        print('По вашему запросу не удалось ничего найти :(')
        return

    table = PrettyTable(field_names=['ID', 'company name', 'link', 'number of vacancies'])
    table.sortby = 'number of vacancies'
    table.reversesort = True

    for emp in employers:
        table.add_row([emp.id, emp.name, emp.url, emp.open_vacancies])

    print(f'Нашли {len(employers)} работодателей по вашему запросу:')
    print(table)


if __name__ == '__main__':
    searching_companies()