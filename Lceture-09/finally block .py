try : 
    numertor = float(input("Enter the nummerator: "))
    denominator = float(input("enter the denominator")) 
    
    result = numertor / denominator 
    print(f"The result is : {result}")
    
except ZeroDivisionError :
    print("Error : you cannot divide by zero .") 
finally:
    print("Exection completed, whet an excption occurred or not.")
print("End of program")