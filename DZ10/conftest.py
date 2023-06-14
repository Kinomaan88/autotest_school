import pytest
import datetime


@pytest.fixture(scope='class')
def summa_2x():
    date = datetime.datetime.today()
    sum_arg = 2 * int(date.strftime('%H'))
    yield sum_arg * 2
    return sum_arg * 3


@pytest.fixture()
def float_arg():
    res = float(5)
    yield res * 2
    return res * 3


