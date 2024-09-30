from .base import APIclient
from ..entities import ShortEmployerInfo


# класс для апи клиентов (компаний, работодателей)
class HHApiClient(APIclient):
    def __init__(self):
        self.__base_url = 'https://api.hh.ru'

# функция поиска работодателей и компаний
    def search_employers(self, search: str, *, only_with_vacancies: bool = True) -> list[ShortEmployerInfo]:
        params = {
            'text': search,
            'only_with_vacancies': only_with_vacancies
        }

        employers = self._get_items('/employers', params=params)
        return [
            ShortEmployerInfo(
                id=int(emp['id']),
                name=str(emp['name']),
                url=str(emp['alternate_url']),
                open_vacancies=int(emp['open_vacancies'])
            )
            for emp in employers
        ]

    @property
    def base_url(self) -> str:
        return self.__base_url

# функция настроек поиска
    def _get_items(self, url: str, params: dict) -> list[dict]:
        items = []
        params['page'] = 0
        params['per_page'] = 100
        while True:
            data = self._get(url, params)
            items.extend(data['items'])

            total_pages = (data['pages'])
            if total_pages == params['page']:
                break
            params['page'] += 1

            if len(items) == 200:
                break

        return items


