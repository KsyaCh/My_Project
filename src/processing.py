def filter_by_state(list_of_dict: list, state='EXECUTED') -> list:
    """функция, фильтрующая данные по ключу"""
    result = []
    for d in list_of_dict:
        current_state = d.get("state")
        if current_state == state:
            result.append(d)
    return result


