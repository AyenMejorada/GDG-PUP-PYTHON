# 1. creating dictionary
# it is called a dictionary since like a real worl dictionary, they use key and a value
# example in this code: key = name, value = Ayen
person = {'name': 'Ayen', 'age': 17}
print("Original dictionary:", person)

# 2. add new key-value pair
person['city'] = 'Muntinlupa City'
print("Dictionary after adding an item:", person)

# 3. update the exisitng key-value pair
# update value of 'age' from 17 to 18
person['age'] = 18
print("Dictionary after updating an item:", person)

# 4. remove a key-value pair
# del statement to remove key value 'age'
del person['age']
print("Dictionary after removing an item:", person)