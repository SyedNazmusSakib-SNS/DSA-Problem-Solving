l1 = [1,2,3,4]
l2 = [1,2,1,2]

l = []
sum = 0
for i in range(len(l1)):
    for j in range(len(l2)):
        sum = l1[i] + l2[j]
        l.append(sum)

print(l)
print(len(l))