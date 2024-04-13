t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    # Initialize the count of removals
    removals = 0
    
    # Check for consecutive elements that can be removed
    for i in range(1, n - 1):
        if a[i - 1] == a[i + 1]:
            removals += 1
    
    # If no removals needed, output -1
    if removals == 0:
        print(-1)
    else:
        print(removals)
