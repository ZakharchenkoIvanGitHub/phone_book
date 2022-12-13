from logger import log


@log
def greatings():
    '''Вывод приветствия.'''
    pass


@log
def menu() -> int:
    """
    Вывод меню, запрос данных от пользователя.
    :return:
    0 - Загрузить из файла и вывести на экран
    1 - Добавить новую запись
    3 - Сохранить в файл
    4 - Редактировать запись по id
    5 - Поиск по фамилии
    """
    pass


@log
def print_book(data: dict):
    """
    Вывод в консоль данных содержимого справочника
    """
    pass


@log
def add_record() -> dict:
    """
    Диалог добавления записи.
    :return Cловарь с данными записи.:
    """
    pass


@log
def request_id() -> int:
    """
    Запрос id от пользователя
    :return id:
    """
    pass


@log
def editor(data: dict) -> dict:
    """
    :param data: Выбранная запись
    :return отредактированная запись:
    """
    pass


@log
def request_last_name() -> str:
    """
    Запрос фамилии от пользователя
    :return фамилия:
    """
    pass
