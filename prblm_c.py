t = int(input())

for _ in range(t):
    hh, mm = map(int, input().split(":"))
    
    if hh < 12:
        suffix = "AM"
        if hh == 0:
            hh = 12
    else:
        suffix = "PM"
        if hh != 12:
            hh -= 12
    
    print(f"{hh:02d}:{mm:02d} {suffix}")
