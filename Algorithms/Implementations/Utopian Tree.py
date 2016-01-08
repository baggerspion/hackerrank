t = int(raw_input().strip())
for _ in range(t):
    n = int(raw_input().strip())
    height = 1
    
    if n != 0:
        for x in range(1, n + 1):
            if x % 2 == 0: # Summer
                height = height + 1
            else: # Spring
                height = height * 2
                
    print height
