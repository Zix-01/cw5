from dataclasses import dataclass
from enum import Enum


# краткая базовая информация по работодателю
@dataclass
class ShortEmployerInfo:
    id: int
    name: str
    url: str
    open_vacancies: int


# полная информация о работодателе
@dataclass
class FullEmployerInfo:
    id: int
    name: str
    url: str
    open_vacancies: int
    website: str
    location: str


class VacancyType(Enum):
    open = 'Открытая'
    closed = 'Закрытая'
    anonymous = 'Анонимная'
    direct = 'Рекламная'


@dataclass
class VacancyInfo:
    id: int
    employer_id: int
    name: str
    link: str
    salary_to: (int | None)
    salary_from: int | None
    type: VacancyType
