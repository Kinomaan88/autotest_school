# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


# @pytest.mark.smoke
# def test_zero():
#     with pytest.raises(ZeroDivisionError):
#         all_division(5, 0)
#
#
# @pytest.mark.stop
# def test_1bat():
#     assert all_division(5, 2) == 2.5
#
#
# @pytest.mark.stop
# def test_2bat():
#     assert all_division(100, 2, 5, 10) == 1
#
#
# @pytest.mark.smoke
# def test_3bat():
#     assert all_division(1) == 1
#
#
# def test_4bat():
#     assert all_division('1')
