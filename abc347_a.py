n, k = map(int, input().split())

a = list(map(int, input().split()))

divisible = []

for i in range(0, n):
    if a[i] % k == 0:
        div = a[i] // k
        divisible.append(div)

print(divisible)