# Step 1: create list of integers
numbers = [5, 3, 8, 1]
print("Original list:", numbers)

#Step 2: add element to list
# append() para magdagdag ng number sa dulo ng list
numbers.append(6)
print("List after adding an element:", numbers)

# Step 3: remove an element from the list
# remove() para tanggalin ang unang occurrence ng number 8
numbers.remove(8) # 8 will be removed
print("List after removing an element:", numbers)

# Step 4: Sort the list in ascending order
# sort() list from smallest to biggest
numbers.sort()
print("List after sorting:", numbers)


# trying with user input
print("\nTry it with your own numbers")

user_input = input("Enter numbers separated by spaces (e.g. 10 3 5 7): ")

# input string to a list of integers
user_numbers = list(map(int, user_input.split()))

print("Your original list:", user_numbers)

# number to add
add_num = int(input("Enter one number to add to the list: "))
user_numbers.append(add_num)
print("List after adding an element:", user_numbers)

# number to remove
remove_num = int(input("Enter a number to remove from the list: "))

# try to remove the number (with error handling in case it's not in the list)
if remove_num in user_numbers:
    user_numbers.remove(remove_num)
    print("List after removing an element (if one number repeats, only the first one in the list will be removed):", user_numbers)
else:
    print(f"Number {remove_num} is not in the list, so nothing was removed.")

# to sort user's list
user_numbers.sort()
print("List after sorting:", user_numbers)