N, S, K = map(int, input().split())

total_cost = 0
for i in range(N):
    Pi, Qi = map(int, input().split())
    total_cost += Pi * Qi
    
if total_cost < S:
    total_cost += K
    print(total_cost)
else:
    print(total_cost)