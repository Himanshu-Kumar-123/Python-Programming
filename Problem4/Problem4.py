def armstrong(n):
    
    temp = n
    dig_sum = 0
    
    while temp > 0:
        digit = temp % 10
        dig_sum += digit ** 3
        temp = temp//10
        
    if dig_sum == n:
        print(n, "is Armstrong")
        
    else:
        print(n, "is NOT Armstrong")
    

armstrong(153)