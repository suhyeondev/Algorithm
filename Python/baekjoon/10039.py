a = []

for i in range(5):
    score = int(input())
    if score >= 40:
        a.append(score)
    else:
        a.append(40)

print(int(sum(a)/5))
