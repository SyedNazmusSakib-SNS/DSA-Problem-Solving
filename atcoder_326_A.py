x, y = map(int, input().split())

if x<y:
    if abs(x-y) <= 2:
        print("Yes")
    else:
        print("No")
elif x > y:
    if abs(x-y) <= 3:
        print("Yes")
    else:
        print("No")