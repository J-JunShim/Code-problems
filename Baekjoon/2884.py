# ěë ěęł
a, b = map(int, input().split())
a, b = divmod(a * 60 + b - 45, 60)
print(a % 24, b)
