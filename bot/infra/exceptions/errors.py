from dataclasses import dataclass


@dataclass(eq=False, order=False, unsafe_hash=False)
class AppExceptions(Exception):
    @property
    def message(self):
        return 'Ошибка приложения!'
    

@dataclass(eq=False, order=False, unsafe_hash=False)
class HTTPError(AppExceptions):
    @property
    def message(self):
        return 'Не удалось отправить запрос!'
    
