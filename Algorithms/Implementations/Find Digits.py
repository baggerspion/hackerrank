t = int(raw_input().strip())
for _ in xrange(t):
    n = raw_input().strip()
    d = int(n)
    count = 0

    for x in n:
        try:
            if d % int(x) == 0: count += 1
        except ZeroDivisionError:
            pass
        
    print count
