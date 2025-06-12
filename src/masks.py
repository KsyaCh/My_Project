from typing import Optional


def get_mask_card_number(card_number: Optional[str]) -> str:
    """маскирует номер карты в формате ХХХ ХХ** **** ХХХХ"""

    if not card_number:
        return "Не заданы параметры"
    if len(card_number) != 16:
        return "Неверный формат"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: Optional[str]) -> str:
    """маскирует номер счета в формате **ХХХХ"""
    if not account_number:
        return "Не заданы параметры"
    if len(account_number) != 20:
        return "Неверный формат"
    return f"**{account_number[-4:]}"
