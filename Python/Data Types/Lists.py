# Enter your code here. Read input from STDIN. Print output to STDOUT
L = []
for _ in range(int(raw_input())):
    cmd = raw_input().split()
    cmd[1:] = map(int, cmd[1:])
    
    # Process the input
    if cmd[0] == "append":
        L.append(cmd[1])
    elif cmd[0] == "insert":
        L.insert(cmd[1], cmd[2])
    elif cmd[0] == "remove":
        L.remove(cmd[1])
    elif cmd[0] == "pop":
        L.pop()
    elif cmd[0] == "index":
        L.index(cmd[1])
    elif cmd[0] == "count":
        L.count(cmd[1])
    elif cmd[0] == "sort":
        L.sort()
    elif cmd[0] == "reverse":
        L.reverse()
    elif cmd[0] == "print":
        print L
