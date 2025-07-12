
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 13:
        print("You are categorized as: Child")
    elif age >= 13 and age <= 19:
        print("You are categorized as: Teenager")
    elif age >= 20 and age <= 59:
        print("You are categorized as: Adult")
    else:
        print("You are categorized as: Senior")

except ValueError:
    print("Invalid input: Age cannot be a non-number.")