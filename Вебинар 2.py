# Задание 1
print('Задание 1')
side = 6
p = 4 * side  # периметр
print('P=', p, sep='')
s = side * side  # площадь
print('S=', s, sep='')
d = pow(2, 0.5) * side  # диагональ квадрата
print('D=', d, sep='')
# Задание 2
print('Задание 2')
# a * x ** 2 + b * x + c = 0
a = 2
b = 4
c = -7
d = pow(b, 2) - 4 * a * c  # D = b2−4ac - дискриминант
first_root = round((- b - pow(d, 0.5)) / (2 * a), 2)
second_root = round((- b + pow(d, 0.5)) / (2 * a), 2)
print('first_root = ', first_root, sep='')
print('second_root = ', second_root, sep='')

# Задание 3
print('Задание 3')
text1 = 'Ваня молодец'
text2 = 'Баня холодная'
print('first_decision = ', text2[:2] + text1[2:] + ' ' + text1[:2] + text2[2:], sep='')
print('second_decision = ', text1.replace(text1[:2], text2[:2]) + ' ' + text2.replace(text2[:2], text1[:2]), sep='')
# Задание 4
print('Задание 4')
path = r'C:\Users\id.balashov\Downloads\name.xlsx'
path = path.split('\\')
name = path[-1].split('.')  # отделяю имя от расширения
print('Диск: ' + path[0][:1], 'Папка: ' + path[1], 'Название файла: ' + name[0], sep='\n')

# Задание 5
print('Задание 5')
first_number = int(3)
second_number = int(2)
print('{}+{}='.format(first_number, second_number), first_number + second_number, sep='')
print('{}*{}='.format(first_number, second_number), first_number * second_number, sep='')
# Задание 6
print('Задание 6')
text = 'Люблю питон'
processed = (text[::2])
print(processed)
# Задание 7
print('Задание 7')
first_string = 'per'
second_string = 'View p the of professionals named'
a = second_string.find(first_string[:1])  # переменная для упрощения дальнейшей записи
b = second_string.find(first_string[1:2])  # переменная для упрощения дальнейшей записи
c = second_string.find(first_string[2:3])  # переменная для упрощения дальнейшей записи
print(second_string[min(a, b, c): (max(a, b, c)+1)])
