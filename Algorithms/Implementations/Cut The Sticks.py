n = int(raw_input().strip())
arr = map(int, raw_input().strip().split())

while len(arr) != 0:
    print sum(1 for x in arr if min(arr) <= x)
    arr = ([x - min(arr) for x in arr if x - min(arr) != 0])
