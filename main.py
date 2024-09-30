from cw5.api_clients import HHApiClient, client
from prettytable import PrettyTable


def main():
    hh_client: HHApiClient = HHApiClient()
    data = hh_client._get_employer_info(1740)

    print(data)


if __name__ == '__main__':
    main()
