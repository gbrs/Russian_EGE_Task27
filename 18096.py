'''
Произведение кратно...
N целых положительных чисел, все числа различны. Рассматриваются все пары различных элементов
(элементы пары не обязаны стоять рядом, порядок элементов в паре неважен). Необходимо определить
количество пар, для которых произведение элементов кратно 62
'''

'''
Произведение двух чисел делится на 62, если: хотя бы один сомножитель делится на 62 или 
один сомножитель делится на 2, а другой — на 31.
Надо подсчитывать количество чисел кратных этим значениям: n62; n31 и n2 (исключив кратные 62)
Искомое количество пар: {n2 * n31} + {n62 * (N – n62)} + {n62 * (n62 – 1)/2}.
'''

N = int(input())  # количество чисел вводим

n62 = n31 = n2 = 0  # счетчики инициализируем

# вводим число и считаем кратные 2, 31 и 62
for i in range(N):
    a = int(input())
    if a % 62 == 0:
        n62 += 1
    elif a % 31 == 0:
        n31 += 1
    elif a % 2 == 0:
        n2 += 1

# всего пар кратных 62:
n = n2 * n31 + n62 * (N - n62) + n62 * (n62 - 1) / 2
print(int(n))