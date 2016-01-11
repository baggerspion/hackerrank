# Enter your code here. Read input from STDIN. Print output to STDOUT
# This works but is super-slow. Not sure about the faster solution.
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import ceil, floor, sqrt

t = int(raw_input())
for _ in xrange(t):
    min, max = map(int, raw_input().split()) 
    print int(floor(sqrt(max)) - ceil(sqrt(min))) + 1
