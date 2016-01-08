# Enter your code here. Read input from STDIN. Print output to STDOUT
# This works but is super-slow. Not sure about the faster solution.
import math

def is_square(x):
    sqrt = int(math.sqrt(x))
    return sqrt**2 == x

t = int(raw_input())
for _ in xrange(t):
    min, max = map(int, raw_input().split())
    print sum(1 for x in xrange(min, max + 1) if is_square(x))
