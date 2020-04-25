a, b, c = map(int, input().split())
maxv = max(a, b, c)
minv = min(a, b, c)
print(a + b + c - maxv - minv)
