# This program checks the age and categorizes the person into different age groups.
# It also demonstrates exception handling using try and except.

try:
    # Input: Get age from the user
    user_input = input("Please enter your age: ")
    age = int(user_input)

    # Check if the age is negative
    if age < 0:
        print("Invalid input: Age cannot be negative.")
    else:
        # Check the age category
        if age < 13:
            print("You are categorized as: Child")
        elif 13 <= age <= 19:
            print("You are categorized as: Teenager")
        elif 20 <= age <= 59:
            print("You are categorized as: Adult")
        else:
            print("You are categorized as: Senior")
        
except ValueError:
    print("Invalid input: Age cannot be a non-number.")
