s = "Hello world deseperate"
freq = {}

for x in s:
    if x in freq:
        freq[x] += 1
        
    else:
        freq[x] = 1
        
print(freq)