# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
letter = 'abcdefghijklmnopqrstuvwxyz'


def generate_random_name():
    while True:
        one_string = ''.join(random.choice(letter) for i in range(random.randrange(1, 15)))
        two_string = ''.join(random.choice(letter) for i in range(random.randrange(1, 15)))
        string = f'{one_string} {two_string}'
        yield string


gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))