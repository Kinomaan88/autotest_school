# Напишите функцию segment
# На вход подается два кортежа с координатами точек (x1, y1), (x2, y2)

# В функции происходит проверка на корректность полученных данных.
# С помощью инструкции try/except as отлавливается исключение Exception. И если это исключение поймано,
# то функция возвращает текст исключения задом наперед (Нужно обратится к атрибуту экзепляра класса Exception)
# Если исключения не произошло, то функция возвращает сумму всех координат


# Здесь пишем код
def segment(coordinates_1, coordinates_2):
    """
    Функция возвращает сумму всех координат, при исключение функция возвращает текст исключения задом наперед
    :param coordinates_1:
    :param coordinates_2:
    :return:
    """
    try:
        x1 = coordinates_1[0]
        x2 = coordinates_2[0]
        y1 = coordinates_1[1]
        y2 = coordinates_2[1]
        return x1 + x2 + y1 + y2
    except Exception as err:
        return f'{err}'[::-1]  #

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    ((2, 3), (4, 5)),
    ((2, -3), (4, 5)),
    ((2, 3), ('4', 5)),
    (('a', 3), (4, 5)),
]

test_data = [
    14,
    8,
    "'rts' dna 'tni' :+ rof )s(epyt dnarepo detroppusnu",
    'rts ot )"tni" ton( rts etanetacnoc ylno nac']


for i, d in enumerate(data):
    assert segment(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
