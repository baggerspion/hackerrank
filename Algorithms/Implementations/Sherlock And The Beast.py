def beast(n):
    if (n < 3):
        return "-1"
     
    three = n//3
    five = 0
     
    while three >= 0:
        rem = N - three * 3
        if rem % 5 == 0:
            five = rem / 5
            break
        three -= 1
         
    if three <= 0 and five == 0:
        return "-1"
     
    return "555" * three + "33333" * five
 

t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    print beast(n)
