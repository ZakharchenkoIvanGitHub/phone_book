from logger import log


@log
def get_data(id: int = None) -> dict:
    """
    Выгружает данные из файла и возвращает словарь
    Если id существует, то возвращает только одну запись по id
    """
    pass


@log
def get_data_id(id: int) -> dict:
    """
    Возвращает только одну запись по id
    """
    pass


@log
def get_data_last_name(last_name: str) -> dict:
    """
    Возвращает только одну запись по фамилии
    """
    pass


@log
def add_data(data: dict):
    """
    Принимает словарь с записью и добавляет в файл.
    Если в принимаемом словаре имеется поле id, тогда сначала удаляет эту запись из словаря.
    :param data:
    """
    pass
