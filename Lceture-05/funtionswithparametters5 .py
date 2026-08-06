def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
display_info(name="Kwang", age=19, city="New York", )