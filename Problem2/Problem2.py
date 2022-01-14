def fact(n):
    x = 1
    for i in range(n,0,-1):
        x*=i

    return x    

print(fact(0))