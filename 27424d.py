sm = 0
mn_difference = 10001
with open('27424_data.txt') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(int, f.readline().strip().split())
        sm += max(a, b)
        difference = abs(a - b)
        if difference % 3 != 0 and difference < mn_difference:
            mn_difference = difference
print(sm - mn_difference)
