# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396

def zdacha1(letter=None):
    N = input(" Введите число: ")
    expression = [N, N + N, N + N + N]
    print(expression)
    summa = [int(letter) for letter in expression]
    print(sum(summa))


zdacha1()
