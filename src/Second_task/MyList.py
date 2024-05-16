# Create a list of String
foods_choice = ['chicken', 'sausage', 'bread', 'milk']

# Print the list
print("Original list:", foods_choice)

# Access elements by index
first_element = foods_choice[0]
print("The first element is:", first_element)

# Slice the list to get a subset
subset = foods_choice[2:4]
print("Subset of the list:", subset)

# Modify an element in the list
foods_choice[1] = 'burger'
print("Modified list:", foods_choice)

# Append an element to the end of the list
foods_choice.append('fried rice')
print("List after appending 6:", foods_choice)

# Remove an element by value
foods_choice.remove('chicken')
print("List after removing 3:", foods_choice)

# Find the index of an element
index_of_bread = foods_choice.index('bread')
print("Index of 2:", index_of_bread)

# Check if an element is in the list
contains_laksa = "laksa" in foods_choice
print("Does the list contain laksa?", contains_laksa)


# Reverse the list
foods_choice.reverse()
print("Reversed list:", foods_choice)

# Create a list of strings
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[2])
