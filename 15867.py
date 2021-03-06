'''
Произведение НЕ кратно...
N целых положительных чисел, все числа различны. Рассматриваются все пары различных элементов
(элементы пары не обязаны стоять рядом, порядок элементов в паре неважен). Необходимо определить
количество пар, для которых произведение элементов НЕ кратно 14
'''

'''
Произведение двух чисел делится на 14, если: хотя бы один сомножитель делится на 14 или 
один сомножитель делится на 2, а другой — на 7.
Надо подсчитывать количество чисел кратных этим значениям: n14; n7 и n2 (исключив кратные 14)
Общее количество возможных пар: N * (N - 1) / 2
Количество пар кратных 14: {n2 * n7} + {n14 * (N – n14)} + {n14 * (n14 – 1)/2}
Отняв это количество от общего {N * (N - 1) / 2} получим искомое.
'''

N = int(input())  # количество чисел вводим

n14 = n7 = n2 = 0  # счетчики инициализируем

# вводим число и считаем кратные 2, 7 и 14
for i in range(N):
    a = int(input())
    if a % 14 == 0:
        n14 += 1
    elif a % 7 == 0:
        n7 += 1
    elif a % 2 == 0:
        n2 += 1

# всего пар НЕ кратных 14:
n = N * (N - 1) / 2 - n2 * n7 - n14 * (N - n14) - n14 * (n14 - 1) / 2
print(int(n))
