'''
На вход программы поступает последовательность из n целых положительных чисел.
Рассматриваются все пары элементов последовательности ai и aj,
такие что i < j и ai > aj (первый элемент пары больше второго;
i и j — порядковые номера чисел в последовательности входных данных).
Среди пар, удовлетворяющих этому условию, необходимо найти и напечатать пару
с максимальной суммой элементов, которая делится на m = 120.
Если среди найденных пар максимальную сумму имеют несколько,
то можно напечатать любую из них.
'''

'''Сумма двух чисел (ai и aj) делится на m, если сумма остатков этих чисел 
от деления на m будет равна или m, или 0. Для каждой из 120 величин 
остатка от деления на m будем хранить максимальное число среди 
уже просмотренных элементов в массиве r длиной m. Изначально всем элементам 
массива r присвоим значение 0. Все значения при этом можно не хранить, 
только 120. Каждое очередное число a будем рассматривать как возможный 
правый элемент искомой пары. a % m = p. Находим в массиве r парный элемент r[m–p] 
(сумма с которым кратна m). Проверяем больше ли парное число, чем текущее ("ai > aj"). 
Если их сумма больше предыдущей запомненной пары left + right, то заменим эту пару 
на новонайденую. При этом если остаток от деления a на m равен 0, 
то рассматривать надо пару a и r[0]. По окончании обработки элемента a необходимо 
обновить элемент r[p] значением a, если a > r[p].
'''

# создание служебного массива для максимальных значений для каждого из остатков
remainder = [0] * 120
# обнуление переменных для записи пары наибольших чисел:
left = 0
right = 0
MX = left * right

with open('28131_data.txt') as f:
    # ввод количества элементов:
    N = int(f.readline())

    # ввод значений с одновременным поиском искомой пары:
    for i in range(N):
        current = int(f.readline())  # переменная для каждого текущего элемента последовательности
        p = current % 120  # остаток от деления текущего числа на 120
        if p == 0:
            p = 120
        if (remainder[120 - p] > current) and (remainder[120 - p] + current > MX):
            # обновление пары с максимальной суммой:
            left = remainder[120 - p]
            right = current
            MX = left + right
        # обновление элемента r для соответствующего остатка,
        # если текущий элемент наибольший из уже просмотренных
        # (с этаким остатком от деления)
        if current > remainder[p % 120]:
            remainder[p % 120] = current

print(left, right)

'''Красивый способ избавиться от проверки p == 0 (а значит целого блока if):

if r[(120 - p) % 120] > a and r[(120 - p) % 120] + a > left + right:
    left = r[(m - p) % m]

простой до элегантности способ:

if (p == 0):
    p = m
if r[m - p] > a ...
'''


