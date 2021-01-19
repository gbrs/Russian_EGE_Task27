'''
положительные целые числа, не превышающее 1000.
После передаётся контрольное значение — наибольшее число R:
1) R — произведение двух чисел, переданных в разные минуты;
2) R делится на 26.
Напечатать отчёт по следующей форме:
Вычисленное контрольное значение: …
Контроль пройден (или Контроль не пройден)
'''

'''
Динамически обрабатываем все входные данные.
Берем очередное число. 
Находим его кратность. Если оно самое большое среди таких чисел, то:
   а) проверяем не является ли его произведение с максимумами, с которыми
       он дает число кратное 26, максимальным. Если да, то записываем
       произведение в MX
   б) перезаписываем соответствующий mx_?_
'''

# максимумы кратные: 26, 13 и 2 (но не кратные 26).
# Максимум среди остальных чисел - max0.
# MX - максимальное произведение
max26 = max13 = max2 = max0 = 0
MX = 0

with open('13373_data.txt') as f:
    N = int(f.readline())

    for i in range(N):
        current = int(f.readline())

        if current % 26 == 0:
            if current > max26:
                if current * max(max0, max2, max13, max26) > MX:
                    MX = current * max(max0, max2, max13, max26)
                max26 = current

        elif current % 13 == 0:
            if current > max13:
                if current * max(max2, max26) > MX:
                    MX = current * max(max2, max26)
                max13 = current

        elif current % 2 == 0:
            if current > max2:
                if current * max(max13, max26) > MX:
                    MX = current * max(max13, max26)
                max2 = current

        else:
            if current > max0:
                if current * max26 > MX:
                    MX = current * max26
                max0 = current

print(MX)
