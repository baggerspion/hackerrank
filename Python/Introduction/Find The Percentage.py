# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(raw_input())
kids = {}

for row in range(a):
    data = raw_input().split(' ')
    kids[data[0]] = map(float, data[1:])
kid = raw_input()
    
print format(sum(kids[kid])/len(kids[kid]), '.2f')
