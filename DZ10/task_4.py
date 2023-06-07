# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


class PersonInfo:
    def all_division(*arg1):
        division = arg1[0]
        for i in arg1[1:]:
            division /= i
        return division


class Testexamle:
    def test_1bat(self, summa_2x):
        assert PersonInfo.all_division(summa_2x, 2) == 2.5

    def test_2bat(self, summa_2x):
        assert PersonInfo.all_division(summa_2x, 2, 5, 10) == 1

    def test_3bat(self, float_arg):
        assert PersonInfo.all_division(float_arg) == 1

    def test_4bat(self, float_arg):
        assert PersonInfo.all_division(float_arg) == 1

