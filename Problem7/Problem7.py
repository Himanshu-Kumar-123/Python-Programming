def leap(year):
   return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))
        
    
if leap(2100):
    print("Leap Year")
    
else:
    print("Not a Leap Year")