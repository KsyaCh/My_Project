import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591}]


def test_filter_by_state(transactions):
    result = filter_by_state(transactions, 'EXECUTED')
    assert len(result) == 2


def test_filter_by_non_state(transactions):
    result = filter_by_state(transactions, 'CANCELED')
    assert len(result) == 1


@pytest.mark.parametrize("state, count", [("EXECUTED", 2),
                                          ("CANCELED", 1),
                                          ("PENDING", 0), ])
def test_filter_by_state_parametrize(transactions, state, count):
    result = filter_by_state(transactions, state)
    assert len(result) == count


def test_sort_by_date(transactions):
    result = sort_by_date(transactions)
    dates = []
    for d in result:
        if "date" in d:
            dates.append(d["date"])
    expected_dates = ['2019-07-03T18:35:29.512364', '2018-09-12T21:27:25.241689', '2018-06-30T02:08:58.425572']
    assert dates == expected_dates


def test_sort_by_date_reverse(transactions):
    result = sort_by_date(transactions, reverse=False)
    dates = []
    for d in result:
        if "date" in d:
            dates.append(d["date"])
    expected_dates = ['2018-06-30T02:08:58.425572', "2018-09-12T21:27:25.241689", "2019-07-03T18:35:29.512364"]
    assert dates == expected_dates
