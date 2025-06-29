import pytest
from src.widget import mask_account_card, get_date


@pytest.fixture
def card_data():
    return [
        ("Visa Classic 1111222233334444", "1111 22** **** 4444"),
        ("MasterCard 9999888877776666", "9999 88** **** 6666"),
        ("Maestro 5099911122223333", "5099 91** **** 3333"),
        ("Счет 12345678901234567890", "**7890"),
        ("Тинькофф Банк 2200111122223333", "2200 11** **** 3333"),
        ("ABC123", "Неверный формат"),
    ]


def test_mask_account_card(card_data):
    for data, expected in card_data:
        result = mask_account_card(data)
        assert result == expected


@pytest.fixture
def dates():
    return [
        ("2024-03-11T12:34:56", "11.03.2024"),
        ("2022-12-31T23:59:59", "31.12.2022"),
        ("2020-01-01T00:00:00", "01.01.2020"),
        ("2023-05-05", "05.05.2023"),
        ("2021-09-07T10:10:10", "07.09.2021"),
        ("0001-01-01", "01.01.0001"),
        ("9999-12-31", "31.12.9999"),
    ]

def test_get_date(dates):
    for date, expected in dates:
        assert get_date(date) == expected