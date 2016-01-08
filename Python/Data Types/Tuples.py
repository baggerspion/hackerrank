# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
t = tuple(map(int, raw_input().split()))
print hash(t)
