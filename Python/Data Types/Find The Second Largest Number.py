# Enter your code here. Read input from STDIN. Print output to STDOUT
a = raw_input()
nums = map(int, raw_input().split())
uniq = {}
map(uniq.__setitem__, nums, [])
print sorted(uniq.keys(), reverse=True)[1]
