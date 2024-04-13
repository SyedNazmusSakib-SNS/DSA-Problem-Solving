n, k = map(int, input().split())  

a = list(map(int, input().split()))  
  
cnt = 0
for i in range(0, n):
    if a[i] >= a[k] and a[i] > 0:
        cnt += 1

print(cnt)

    