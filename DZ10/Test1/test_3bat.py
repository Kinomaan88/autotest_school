import pytest
from DZ10.task_2 import *


@pytest.mark.smoke
def test_3bat():
    assert all_division(1) == 1