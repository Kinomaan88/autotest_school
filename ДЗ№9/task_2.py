# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


from datetime import datetime
import time

# Здесь пишем код


def func_log(file_log='log.txt'):
    def decorator(func):
        """
        Декоратор который дозаписывает в файл имя вызываемой функции, дату и время вызова
        :param file_log:
        :return:
        """
        def wrapper(*args, **kwargs):
            dt = datetime.now()  # Получаю текущую дату
            with open(file_log, 'a+', encoding='utf-8') as file:
                file.write(f'{func.__name__} вызвана {dt.strftime("%d.%m %H:%M:%S")}\n')
            res = func(*args, **kwargs)
            return res
        # сохраняю информацию об исходной функции
        wrapper.__module__ = func.__module__
        wrapper.__name__ = func.__name__
        wrapper.__qualname__ = func.__qualname__
        wrapper.__doc__ = func.__doc__
        wrapper.__annotations__ = func.__annotations__
        return wrapper
    return decorator


@func_log()
def func1(*args):
    """
    Что то делает
    """
    time.sleep(3)
    return 5

@func_log(file_log='func2.txt')
def func2(param=4, *args):
    """
    Что то делает
    """
    time.sleep(5)
    return param

func1()
func2()
func1()

