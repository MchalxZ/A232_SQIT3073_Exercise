# Create a tuple
foods = ("chicken rice", "meat ball", "fried rice", "onion rings")

("a" , 1 , 2.3 , "b")

# Access elements by index
first_foods = foods[0]
second_foods = foods[1]

# Iterate through the tuple
print("foods:")
for food in foods:
    print(food)

# Check if an element is in the tuple
contains_pizza = "pizza" in foods

# Find the length of the tuple
num_foods = len(foods)

# Concatenate two tuples
more_foods = ("burger", "sausage")
all_foods = foods + more_foods

# Nested tuple
nested_tuple = ("red", ("green", "blue"))

# Print the results
print("First food:", first_foods)
print("Second food:", second_foods)
print("Does it contain 'pizza'? ", contains_pizza)
print("Number of foods:", num_foods)
print("All foods:", all_foods)
print("Nested tuple:", nested_tuple)
