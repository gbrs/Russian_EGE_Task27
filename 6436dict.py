'''
sms-голосование за (максимум) 16 пар.
Результаты голосования получены в виде номеров пар.
Вывести список всех пар в порядке невозрастания количества голосов
с указанием количества отданных за них голосов (кроме пар с нулевыми результатами)
'''

'''
Подсчитываем голоса в счетчики в массиве на 16 элементов. 
После ввода одновременная сортировка массивов номеров пар и количества голосов. 
Затем выводится список пар с указанием количества голосов
'''

dct = {}

with open('6436_data.txt') as f:
    # количество вводимых значений
    N = int(f.readline())

    # считываем номер пары из sms-ок и увеличиваем соответствующие счетчики
    for i in range(N):
        t = int(f.readline())
        dct[t] = dct.setdefault(t, 0) + 1

dct = sorted(dct.items(), key=lambda item: item[1], reverse=True)

for key, value in dct:
    print(key, value)