# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    """
    Функция присваевает переменной msg значение 1
    :return:
    """
    msg = 1

    def local_function():
        """
        Функция переписывает переменую msg
        :return:
        """
        # Здесь нужно написать код
        nonlocal msg
        msg = 2
        return msg
    return local_function()


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
