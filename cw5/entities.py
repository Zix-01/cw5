from dataclasses import dataclass


# краткая базовая информация по работодателю
@dataclass
class ShortEmployerInfo:
    id: int
    name: str
    url: str
    open_vacancies: int