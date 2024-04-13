x = int(input())


if x <= 5:
    step = 1
elif x > 5 and x%5 != 0:
    step = x//5 + 1
elif x > 5 and x % 5 == 0:
    step = x//5

print(step)