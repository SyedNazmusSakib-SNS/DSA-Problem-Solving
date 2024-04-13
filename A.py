t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    if 2*a[1] < a[2]:
        price = a[0] * a[1]
    else:
        price = (a[0]//2)*a[2] + (a[0]%2)*a[1]

    print(price)