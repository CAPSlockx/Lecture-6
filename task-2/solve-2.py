cnt = int(input())
summ = 0
for _ in range(cnt):
    n = int(input())
    if n % 10 == 4 and n % 3 == 0:
        summ += n
print(summ)

