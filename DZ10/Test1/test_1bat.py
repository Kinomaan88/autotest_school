import pytest


from DZ10.task_2 import *


@pytest.mark.parametrize('a, b, result', [(5, 2, 2.5), (4, 2, 2), (7, 7, 1)])
def test1_bat(a, b, result):
    assert all_division(a, b) == result
