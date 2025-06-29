def filter_by_currency(transactions:list, currency_code:str) -> list:
    """функция поочередно выдает транзакции согласно заданной валюте"""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions:list) -> str:
    """функция возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start:int, end:int) -> str:
    """функция генерирует номера карт"""
    for num in range(start, end + 1):
        num_str = str(num)
        beginning_num = '0' * (16 - len(num_str)) + num_str
        formatted_num = ' '.join([beginning_num[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_num
