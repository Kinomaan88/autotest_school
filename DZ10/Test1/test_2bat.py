import pytest

from DZ10.task_2 import *


@pytest.mark.stop
def test_2bat():
    assert all_division(100, 2, 5, 10) == 1