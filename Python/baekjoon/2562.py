a = []

for i in range (9):
    a.append(eval(input()))

print(max(a))
print(a.index(max(a))+1)
