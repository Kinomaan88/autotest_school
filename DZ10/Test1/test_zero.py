import pytest
from DZ10.task_2 import *


@pytest.mark.smoke
def test_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(5, 0)