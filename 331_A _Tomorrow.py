M, D = map(int, input().split())

y, m, d = map(int, input().split())

if d == D:
    m += 1
    if m == M:
        y += 1
else:
    d += 1
    
print(y , m, d)