def get_mask_card_number(card_number: int) -> str:
    '''маскирует номер карты в формате ХХХ ХХ** **** ХХХХ'''
    str_card_number = str(card_number)
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    '''маскирует номер счета в формате **ХХХХ'''
    str_account_number = str(account_number)
    return f"**{str_account_number[-4:]}"
