def create_greeting(name):
    message = (
        f"Hello {name}, welcome to the GDG Web Development Team! "
        "You're doing great, and I truly believe that someday you'll be an amazing developer. "
        "Life may feel challenging right now, and programming can be overwhelming at times, "
        "but remember, all your hard work will pay off in the end. "
        "Keep pushing forward, you're on the right path! Padayon!"
    )
    return message


# ask the user to input their name
user_input = input("Enter your name: ")

# check if the input is a valid string (non-empty and alphabetic)
if user_input.strip().isalpha():
    # call the function and get the greeting message
    greeting = create_greeting(user_input.strip())
    
    # print the greeting message
    print("\nThe greeting message is:")
    print(greeting)
else:
    # if the input is not valid, show an error message
    print("Invalid input: Please enter a valid name.")
