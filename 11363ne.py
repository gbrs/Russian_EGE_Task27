'''
Задание А. Имеется набор данных, состоящий из 6 пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так,
чтобы сумма всех выбранных чисел не делилась на 3
и при этом была максимально возможной.
Если получить требуемую сумму невозможно, в качестве ответа нужно выдать 0.
'''

a = [[[0] * 6] for i in range(2)]

for i in range(6):
    a, b = map(int, input().split())

sMax = 0

for i1 in range(2):
    for i2 in range(2):
        for i3 in range(2):
            for i4 in range(2):
                for i5 in range(2):
                    for i6 in range(2):
                        s:=a[1,i1]+a[2,i2]+a[3,i3]+a[4,i4]+a[5,i5]+a[6,i6];

if (s mod 3 <> 0) and (s > sMax) then sMax := s

writeln(sMax)

end.
