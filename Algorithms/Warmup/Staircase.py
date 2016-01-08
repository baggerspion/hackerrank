n = int(raw_input().strip())
for row in xrange(1, n + 1):
   print (' ' * (n - row)) + ('#' * row)
