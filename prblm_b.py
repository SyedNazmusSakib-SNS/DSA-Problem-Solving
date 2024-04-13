n = int(input())
s = t = ""
for i in range(0, n):
    if i % 2 == 1:
        s += "##"
    else:
        s += ".."

for j in range(0, n):
    if j % 2 == 1:
        t += '..'
    else:
        t += "##"

for k in range(0, n):
    if k % 2 == 1:
        print(s+'\n'+s)
    else:
        print(t+'\n'+t)


