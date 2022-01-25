def fibonacci(n):
    f0 = 0
    f1 = 1
    
    for i in range(1,n+1):
        print(f0)
        f2 = f0 + f1
        f0 = f1
        f1 = f2
    

fibonacci(10)