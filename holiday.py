n = int(input())
welfare = list(map(int, input().split()))

max_welfare = max(welfare)
total_expense = sum(max_welfare - w for w in welfare)

print(total_expense)
