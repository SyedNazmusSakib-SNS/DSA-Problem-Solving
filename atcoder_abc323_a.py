s = input()

cnt = 0
for i in range(1, len(s), 2):
    if s[i] == '0':
        cnt += 1

if cnt == 8:
    print("Yes")
else:
    print("No")
