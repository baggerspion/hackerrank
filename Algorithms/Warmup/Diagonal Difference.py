n = int(raw_input().strip())
x = 0 
y = 0

for a_i in xrange(n):
   a_temp = map(int, raw_input().strip().split())
   x += a_temp[a_i]
   y += a_temp[n - a_i - 1]

print abs(x - y)
