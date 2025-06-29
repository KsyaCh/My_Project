import pytest
from src.widget import mask_account_card


@pytest.mark.parametrize("number, masks", [("Maestro 1596837868705199", "1596 83** **** 5199"),
                                           ("Счет 64686473678894779589", "**9589"),
                                           ("MasterCard 7158300734726758", "7158 30** **** 6758"),
                                           ("Счет 35383033474447895560", "**5560"),
                                           ("Visa Classic 6831982476737658", "6831 98** **** 7658"),
                                           ("Visa Platinum 8990922113665229", "8990 92** **** 5229"),
                                           ("Visa Gold 5999414228426353", "5999 41** **** 6353"),
                                           ("Счет 73654108430135874305", "**4305")])
def test_mask_account_card(number, masks):
    assert mask_account_card(number) == masks
