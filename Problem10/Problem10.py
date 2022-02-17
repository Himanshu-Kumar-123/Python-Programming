s = "Hello world deseperate"
freq = {}

for x in s:
    if x in freq:
        freq[x] += 1
        
    else:
        freq[x] = 1

s2 = ''

for x in s:
    if freq[x] != 2:
        s2 += x
        
print(s2)