t = int(raw_input().strip())
for _ in xrange(t):
    n, k = map(int, raw_input().strip().split())
    a = map(int,raw_input().strip().split())
    if sum(1 for x in a if x <= 0) < k: print 'YES'
    else: print 'NO'
