from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("1234567891234567") == "1234 56** **** 4567"

    assert get_mask_card_number("") == "Не заданы параметры"

    assert get_mask_card_number(None) == "Не заданы параметры"

    assert get_mask_card_number("123456") == "Неверный формат"


def test_get_mask_account():
    assert get_mask_account("64686473678894779589") == "**9589"

    assert get_mask_account("") == "Не заданы параметры"

    assert get_mask_account(None) == "Не заданы параметры"

    assert get_mask_account("123456") == "Неверный формат"