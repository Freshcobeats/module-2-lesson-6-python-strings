while True:
    first_name = input("Please enter your first name:")
    last_name = input("please enter your last name:")

    
    if len(first_name) >=2 and len(last_name) >=2:
        print("username is valid")
        break
    else:
        print("first and last name must be at least 2 characters")