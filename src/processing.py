def filter_by_state(list_of_dict: list, state="EXECUTED") -> list:
    """функция, фильтрующая данные по ключу"""
    result = []
    for d in list_of_dict:
        current_state = d.get("state")
        if current_state == state:
            result.append(d)
    return result


def sort_by_date(list_of_dict: list, reverse=True) -> list:
    """функция, сортирующая данные в списке по дате"""
    new_list_of_dict = []
    for item in list_of_dict:
        if "date" in item:
            new_list_of_dict.append(item)
        sorted_list_of_dict = sorted(new_list_of_dict, key=lambda x: x["date"], reverse=reverse)
    return sorted_list_of_dict
