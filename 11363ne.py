'''
Задание А. Имеется набор данных, состоящий из 6 пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так,
чтобы сумма всех выбранных чисел не делилась на 3
и при этом была максимально возможной.
Если получить требуемую сумму невозможно, в качестве ответа нужно выдать 0.
'''

# формируем матрицу 6х2
a = [[0] * 6 for i in range(2)]

# заполняем матрицу
for i in range(6):
    a[0][i], a[1][i] = map(int, input().split())

sMax = 0

# перебираем все возможные варианты комплектов по 6 значений
for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                for i5 in range(2):
                    for i6 in range(2):
                        s = a[i1][0] + a[i2][1] + a[i3][2] + a[i4][3] + a[i5][4] + a[i6][5]
                        if (s % 3 != 0) and (s > sMax):
                            sMax = s

print(sMax)
