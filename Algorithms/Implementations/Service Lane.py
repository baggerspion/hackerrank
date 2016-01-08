n, t = map(int, raw_input().strip().split())
width = map(int, raw_input().strip().split())

for _ in xrange(t):
    i, j = map(int, raw_input().strip().split())
    
    if 1 in width[i:j + 1]:
        print 1
    else:
        if 2 in width[i:j + 1]:
            print 2
        else:
            print 3
