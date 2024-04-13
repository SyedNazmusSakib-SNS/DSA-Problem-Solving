n = int(input())
colors = input()

count = 0

for i in range(1, n):
    if colors[i] == colors[i - 1]:
        count += 1


print(count)
