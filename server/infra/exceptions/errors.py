from dataclasses import dataclass


@dataclass(eq=False, order=False, unsafe_hash=False)
class AppExceptions(Exception):
    @property
    def message(self):
        return 'Ошибка приложения!'
    
    @property
    def status_code(self):
        return 400


@dataclass(eq=False, order=False, unsafe_hash=False)
class DataBaseException(AppExceptions):
    code: int

    @property
    def status_code(self):
        return self.code

    @property
    def message(self):
        return 'Не удалось записать, удалить, получить данные!'
    

@dataclass(eq=False, order=False, unsafe_hash=False)
class ProductNotFound(AppExceptions):
    code: int

    @property
    def status_code(self):
        return self.code
    
    @property
    def message(self):
        return 'Арбуз не найден!'
    

@dataclass(eq=False, order=False, unsafe_hash=False)
class ProductRemoveCartNotFound(AppExceptions):
    code: int

    @property
    def status_code(self):
        return self.code
    
    @property
    def message(self):
        return 'Арбуз для удаления не найден!'