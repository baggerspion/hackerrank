s = raw_input().strip()
pos, char = raw_input().strip().split()

l = list(s)
l[int(pos)] = char

print ''.join(l)
