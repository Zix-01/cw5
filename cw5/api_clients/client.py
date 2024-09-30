from .base import APIclient
from ..entities import ShortEmployerInfo, FullEmployerInfo, VacancyInfo, VacancyType


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

# функция получающая работодателей
    def _get_employer_info(self, employer_id: int) -> FullEmployerInfo:
        employers_info = self._get(f'/employers/{employer_id}')
        return FullEmployerInfo(
            id=employer_id,
            name=employers_info['name'],
            url=employers_info['alternate_url'],
            open_vacancies=employers_info['open_vacancies'],
            website=employers_info['site_url'],
            location=employers_info['area']['name']
        )

# функция получающая вакансии
    def _get_employer_vacancies(self, employer_id: int) -> list[VacancyInfo]:
        params = {
            'employer_id': employer_id,
            'only_with_salary': True,
        }
        vacancies = self._get_items('/vacancies', params=params)
        return [
            VacancyInfo(
                id=int(vac['id']),
                name=vac['name'],
                link=vac['alternate_url'],
                salary_from=vac['salary'].get('from'),
                salary_to=vac['salary'].get('to'),
                employer_id=employer_id,
                type=VacancyType[vac['type']['id']]
            )
            for vac in vacancies
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
