def factorial(n, result):
    if n == 1: return result
    else: return factorial(n - 1, n * result)

n = int(raw_input().strip())
print factorial(n, 1)
