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
Искомое количество пар q подсчитываем на ходу, исходя из четности очередного числа.
( Искомое количество пар можно посчитать и комбинаторно: 
{n2 * n31} + {n62 * (N – n62)} + {n62 * (n62 – 1) / 2}. )
'''

n62 = n31 = n2 = q = 0  # счетчики инициализируем

with open('18096_data.txt') as f:
    # считываем количество данных чисел
    N = int(f.readline())

    # для каждого числа
    for i in range(N):
        # считываем очередное число
        current = int(f.readline())

        # подсчитываем количество новых пар
        # в зависимости от четности текущего числа
        if current % 62 == 0:
            q += n62 + n31 + n2
            n62 += 1
        elif current % 31 == 0:
            q += n62 + n2
            n31 += 1
        elif current % 2 == 0:
            q += n62 + n31
            n2 += 1

print(q)
