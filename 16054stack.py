'''
элементы находящиеся не ближе...
последовательность из N целых положительных чисел, все числа в последовательности различны.
Рассматриваются все пары различных элементов последовательности, находящихся на расстоянии не меньше чем 4
(порядок элементов в паре неважен). Необходимо определить количество таких пар, для которых произведение
элементов делится на 29

Произведение двух чисел делится на 29, если хотя бы один из сомножителей делится на 29.
При вводе чисел можно подсчитывать количество n29 чисел, кратных 29, не считая четырёх последних.
Сами числа, кроме четырёх последних, при этом можно не хранить.
Очередное считанное число будем рассматривать как возможный правый элемент искомой пары. Если
очередное считанное число делится на 29, то к ответу следует прибавить количество чисел до него
(не считая четырёх последних, включая считанное). Если очередное считанное число на 29 не делится,
то к ответу следует прибавить n29.
'''

'''
Проверка: 7; 58, 2, 3, 5, 4, 1, 29
Ответ: 5
'''

# создаем очередь
queue = []

with open('16054_data.txt') as f:
    n = int(f.readline())  # общее количество чисел

    # вводим 4 первых элемента
    for i in range(4):
        queue.append(int(f.readline()))

    count = 0  # счетчик количества пар делящихся на 29
    n29 = 0  # счетчик количества чисел кратных 29

    for i in range(4, n):

        # убирая левый элемент из очереди проверяем его на кратность 29
        if queue.pop(0) % 29 == 0:
            n29 += 1

        current = int(f.readline())  # нововведенное число

        # если число кратно 29, то общее число пар увеличивается на количество чисел за вычетом четырех последних
        if current % 29 == 0:
            count += (i + 1) - 4
        # если число не кратно 29,
        # то общее число пар увеличивается на количество чисел кратных 29 (не учитывая четыре последних значения)
        else:
            count += n29

        queue.append(current)  # загоняем в очередь справа нововведенное число

    print(count)
