from logger import log


@log
def greatings():
    '''Вывод приветствия.'''

    print('Добро пожаловать в Справочник')
    pass


@log
def menu() -> int:
    """
    Вывод меню, запрос данных от пользователя.
    :return:
    0 - Выход
    1 - Загрузить из файла и вывести на экран
    2 - Добавить новую запись
    3 - Редактировать запись по id
    4 - Поиск по фамилии

    """
    print('Меню')
    return int(input(' 1 - Загрузить из файла и вывести на экран \n 2 - Добавить новую запись \n 3 - Редактировать запись по id \n 4 - Поиск по фамилии \n'))
    pass  


@log
def print_book(data: dict): # список
    """
    Вывод в консоль данных содержимого справочника
    """
    pass


@log
def add_record() -> dict: #введите фамили (ключ имя словарь)
    """
    Диалог добавления записи.
    :return Cловарь с данными записи.:
    """
    my_dict = {} 

    my_dict['name'] = input('Введите имя : ')
    my_dict['surname'] = input('Введите фамилию : ')
    my_dict['number_ph'] = input('Введите номер телефона : ')
    return my_dict
    pass


@log
def request_id() -> int: # ввидите id input 
    """
    Запрос id от пользователя
    :return id:
    """
    return int(input('Введите id: '))
    pass


@log
def editor(data: dict) -> dict: #входит справочник пройти по нему
    """
    :param data: Выбранная запись
    :return отредактированная запись:
    """
    pass


@log
def request_last_name() -> str: # input введите фамилию
    """
    Запрос фамилии от пользователя
    :return фамилия:
    """
    return input('Введите Фамилию: ')
    pass
