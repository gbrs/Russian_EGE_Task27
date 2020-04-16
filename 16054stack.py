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

# создаем стэк
stack = []

n = int(input())  # общее количество чисел

# вводим 4 первых элемента
for i in range(4):
    stack.append(int(input()))

count = 0  # счетчик количества пар делящихся на 29
n29 = 0  # счетчик количества чисел кратных 29

for i in range(4, n):

    # убирая левый элемент из стэка проверяем его на кратность 29
    if stack.pop(0) % 29 == 0:
        n29 += 1

    a = int(input())  # a - обозначение для нововводимого числа

    # если число кратно 29, то общее число пар увеличивается на количество чисел за вычетом четырех последних
    if a % 29 == 0:
        count += (i + 1) - 4
    # если число не кратно 29,
    # то общее число пар увеличивается на количество чисел кратных 29 (не учитывая четыре последних значения)
    else:
        count += n29

    stack.append(a)  # загоняем в стэк справа нововведенное число

print(count)
