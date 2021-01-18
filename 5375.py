'''
N целых чисел (по абсолютной величине не превышающее 10^9). Все РАЗЛИЧНЫ.
Найти основное множество скоростей для которого произведение скоростей
является максимальным среди всех возможных множеств. Знак числа учитывается.
Если есть несколько таких множеств, то основным считается то,
которое содержит наибольшее количество элементов.
'''

'''
Основное множество состоит из всех значений скоростей, кроме нулевых;
и кроме минимальной по модулю отрицательной скорости, 
если отрицательных скоростей нечётное число.
Параллельно со вводом запоминаем номер 0, подсчитываем количество отрицательных значений 
и ищем минимальное по модулю отрицательное значение. 
В конце распечатываем все номера, кроме номера 0 и 
номера минимального по модулю отрицательного значения 
(в случае, если отрицательных чисел нечётное число).
'''

# количество вводимых значений
N = int(input())

# инициируем: счетчик количества отрицательных чисел
# минимальное по модулю отрицательное число
# ячейку для хранения позиции минимального по модулю отрицательного числа
# ячейку для хранения позиции нулевого значения
n_neg = 0  #
max_neg = -1000000001
index_max_neg = None
index0 = None

# загружая значения, запоминаем ячейку с нулевым значением,
# подсчитываем количество отрицательных отсчетов и
# запоминаем минимальное по модулю отрицательное число и его позицию
for i in range(N):
    a = int(input())
    if a == 0:
        index0 = i
    elif a < 0:
        n_neg += 1
        if a > max_neg:
            max_neg = a
            index_max_neg = i

# выводим на печать все номера отсчетов (учитывая что внутри Python нумерация с нуля),
# кроме позиций нулевого значения и минимального по модулю отрицательного числа
# (последнее если количество отрицательных отсчетов нечетное)
for i in range(N):
    if (i != index0) and ((n_neg % 2 == 0) or (i != index_max_neg)):
        print(i + 1, end=' ')