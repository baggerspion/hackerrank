n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
crypto = ''

for x in s:
    k %= (ord('z') - ord('a') + 1)
    if x.isalpha():
        if x.islower():
            char = ord(x) + k
            if char > ord('z'): char = char - ord('z') + ord('a') - 1
        elif x.isupper():
            char = ord(x) + k
            if char > ord('Z'): char = char - ord('Z') + ord('A') - 1
    else:
        char = ord(x)
    crypto += chr(char)
        
print crypto
