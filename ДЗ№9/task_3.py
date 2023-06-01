# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
sum_purchases = [0, 0, 0]
summa = 0
three_most_expensive_purchases = 0
with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:
    # Цикл проходит по строкам и суммирует все до первой пустой строки.
    for price in file:
        if len(price) > 1:
            summa += int(price[:-1])
        elif summa > min(sum_purchases):
            index = sum_purchases.index(min(sum_purchases))
            sum_purchases[index] = summa
            summa = 0
        else:
            summa = 0

    three_most_expensive_purchases = sum(sum_purchases)

assert three_most_expensive_purchases == 202346
