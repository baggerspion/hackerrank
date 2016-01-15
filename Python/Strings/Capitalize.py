s = raw_input().strip()
r = ""
for x in xrange(len(s)):
    if x == 0 or (s[x].isalpha() and s[x-1] == " "):
        r = r + s[x].upper()
    else:
        r = r + s[x]
print r
