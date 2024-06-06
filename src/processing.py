def filter_by_state(my_dictionaries: list, my_state: str = "EXECUTED") -> list:
    """
    Функция, которая принимает на вход список словарей и значение для ключа
    state и возвращает новый список, содержащий только те словари, у которых ключ
    state содержит переданное в функцию значение
    """
    filtered_my_dictionaries = []
    for i in my_dictionaries:
        if i["state"] == my_state:
            filtered_my_dictionaries.append(i)

    return filtered_my_dictionaries


def sort_by_date(my_dictionaries: list, sorting_direction: bool = True) -> list:
    """
    Функция, которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты
    """
    sorted_my_dictionaries = sorted(
        my_dictionaries, key=lambda date_dict: date_dict.get("date"), reverse=sorting_direction
    )

    return sorted_my_dictionaries
