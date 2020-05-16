n = int(input())

for i in range(n):
    a = input()
    score = 0
    cnt = 0
    for j in range(len(a)):
        if a[j] == 'O':
            cnt += 1
            score += cnt
        elif a[j] == 'X':
            score += 0
            cnt = 0
    print(score)
