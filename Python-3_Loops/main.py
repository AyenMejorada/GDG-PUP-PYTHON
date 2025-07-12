# Loops – For and While Assignment

# Part 1: For Loop - Printing a list of favorite foods
favorite_foods = ['fries', 'dinuguan', 'avocado', 'mango', 'salad']

print("My Favorite Foods:")

for food in favorite_foods:
    print("- " + food)  # print each food item with dash/bullet

print()  # blank line before next section

# Part 2: While Loop - Countdown from a number
# ask user
user_input = input("Enter a starting number for the countdown: ")

try:
    start_number = int(user_input)

    # validation
    if start_number <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        # start countdown
        print("Countdown begins!")
        while start_number >= 1:
            print(start_number)
            start_number -= 1 

        print("Countdown complete!")  # message after countdown ends

except ValueError:
    # handle case when the input is not a valid number
    print("Invalid input: Please enter a positive integer.")
