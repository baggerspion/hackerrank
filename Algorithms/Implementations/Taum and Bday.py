t = int(raw_input().strip())
for _ in range(t):
    b, w = map(int, raw_input().strip().split())
    x, y, z = map(int, raw_input().strip().split())
    result = 0
    
    if x == y: 
        print (b + w) * x
        continue
        
    if x < (y + z): 
        result += b * x
    else: 
        result += b * (y + z)

    if y < (x + z): 
        result += w * y
    else: 
        result += w * (x + z)

    print result
