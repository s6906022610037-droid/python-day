def divide(a,b): 
    try: 
        return a/b 
    except Exception as e : 
        print("Error:  {e} ")
        return None 
    else : 
        return result

a,b = map (int, input("Enter two number separted by space : ").spilt())
print(divide(a,b))
print("End of program")
