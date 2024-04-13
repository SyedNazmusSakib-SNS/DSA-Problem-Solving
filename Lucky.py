t = int(input())

for _ in range(t):
    s = input()
    
    sum1 = sum(ord(c) - ord('0') for c in s[:3])
    sum2 = sum(ord(c) - ord('0') for c in s[3:])

    if sum1 == sum2:
        print("YES")
    else:
        print("NO")
