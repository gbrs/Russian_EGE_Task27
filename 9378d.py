'''
Положительные целые числа раз в минуту.
Необходимо вычислить «бета-значение» – минимальное чётное произведение двух показаний,
между моментами передачи которых прошло не менее 6 минут.
Если получить такое произведение не удаётся, ответ считается равным –1.
'''

'''
Создаем очередь queue, в которой будут храниться последние 5 чисел. 
Среди остальных, уже прочитанных чисел ("куча") всегда ищем четное минимальное
    и абсолютно минимальное (они могут совпадать).
Каждое вновь вводимое число проверяем на минимальность его произведения
    с текущим соответствующим минимальным числом (нечетное число - 
    с четным минимальным, четное - с абсолютным минимальным).
Затем вновь введенное число добавляем в очередь. А крайнее левое число очереди 
    извлекаем из нее в кучу. Проверяем не является ли оно минимальным.
'''

# создаем очередь
queue = []

# Минимальные значения и произведение инициализируем невозможным значением 1001.
mn = mn2 = 1001
minimult = mn * mn

with open('9378_data.txt') as f:
    # количество вводимых значений
    N = int(f.readline())

    # в очередь кладем первые 5 чисел
    for i in range(5):
        queue.append(int(f.readline()))

    # для каждого последующего числа
    for i in range(5, N):
        current = int(f.readline())

        # проверяем не является ли минимальным произведением
        # произведение текущего числа с соответствующим минимумом
        if current % 2 == 0:
            minimult = min(minimult, current * mn)
        else:
            minimult = min(minimult, current * mn2)

        # Извлекаем крайний левый элемент очереди и кладем в кучу,
        # проверяя не является ли он минимумом.
        # Добавляем текущее число в очередь.
        left = queue.pop(0)
        mn = min(mn, left)
        if left % 2 == 0:
            mn2 = min(mn2, left)
        queue.append(current)

print(minimult)

