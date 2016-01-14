s1 = raw_input().strip()
s2 = raw_input().strip()

print sum(1 for x in xrange(len(s1)) if s1[x:].startswith(s2))
