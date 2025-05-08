import masks


def mask_account_card(data: str) -> str:
    """функция, маскирующая данные о номерах карт и счетов"""
    if "Счет" in data:
        account_number = ""
        for symbol in data:
            if symbol.isdigit():
                account_number += symbol
        mask_result = masks.get_mask_account(account_number)
    else:
        card_number = ""
        for symbol in data:
            if symbol.isdigit():
                card_number += symbol
        mask_result = masks.get_mask_card_number(card_number)
    return mask_result


def get_date(date: str) -> str:
    """Форматирует дату"""
    date_split = date.split("T")
    only_date = date_split[0]
    result_date = only_date.split("-")
    return f"{result_date[2]}.{result_date[1]}.{result_date[0]}"
