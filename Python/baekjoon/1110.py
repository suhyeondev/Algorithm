n = m = int(input())
i = 0
while True:
    m = m % 10 * 10 + (m % 10 + m // 10) % 10
    i += 1
    if m == n:
        break
print(i)
