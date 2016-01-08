# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(raw_input())
m = set(map(int, raw_input().split()))
N = int(raw_input())
n = set(map(int, raw_input().split()))

s1 = m.difference(n)
s2 = n.difference(m)

L = list(s1.union(s2))
L.sort()

for i in L: 
    print i
