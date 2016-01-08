from __future__ import division

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split())

print sum(1 for x in arr if x > 0) / n
print sum(1 for x in arr if x < 0) / n
print sum(1 for x in arr if x == 0) / n
