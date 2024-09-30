from cw5.api_clients import HHApiClient, client
from prettytable import PrettyTable


def main():
    hh_client = HHApiClient()
    employers = hh_client.search_employers(search='VK')

    table = PrettyTable(field_names=['ID', 'company name', 'link', 'number of vacancies'])
    for emp in employers:
        table.add_row([emp.id, emp.name, emp.url, emp.open_vacancies])

    print(table)


if __name__ == '__main__':
    main()
