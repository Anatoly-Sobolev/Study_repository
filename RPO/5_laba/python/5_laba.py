"""- Реализовать функцию, которая возвращает через указатели одновременно сумму и произведение двух чисел.
- Написать функцию, которая получает строку и возвращает количество гласных и согласных букв (через параметры-указатели).
- Составить функцию, которая принимает массив и через параметры возвращает минимальный и максимальный элементы."""

from string import ascii_letters
alfa = ascii_letters[:26]


def sum_and_mult(a, b):
    return a + b, a * b


def get_number_wavals(line:str):
    while ' ' in line:
        line = line.replace(' ', '')
    line = line.lower()
    vaw = ['a', 'o', 'u', 'y', 'e', 'i']
    let = set(alfa) - set(vaw)
    for i in vaw:
        line = line.replace(i, 'a')
    for j in let:
        line = line.replace(j, 'b')

    return line.count('a'), line.count('b')


def get_min_max(line):
    return min(line), max(line)

a = 24
b = 12
lst = [1, 5, 6, 25, 2]
line = 'Hello  world!'
print(*sum_and_mult(a, b))
print(*get_number_wavals(line))
print(*get_min_max(lst))