total = 0
for num in range(1, 1000001):
    if num % 3 != 0:
        total += num
print(total)