# creating dictionary
# it is called a dictionary since like a real worl dictionary, they use key and a value
# example in this code: key = name, value = Sparky
person = {'name': 'Sparky', 'age': 25}
print("Original dictionary:", person)

# update
# add new key-value pair
person['city'] = 'New York'
print("Dictionary after adding an item:", person)

# update value of 'age' from 25 to 26
# update the exisitng key-value pair
person['age'] = 26
print("Dictionary after updating an item:", person)

# del statement to remove key value 'age'
# remove a key-value pair
del person['age']
print("Dictionary after removing an item:", person)