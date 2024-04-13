t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    if a<b and b<c:
        print("STAIR\n")

    elif a<b and c<b:
        print("PEAK\n")
    
    else:
        print("NONE\n")