Randset = {"airplane", "best", "chopstick", "drinks"}

# Add an element to the set
Randset.add("elephant")

# Remove an element from the set
Randset.remove("airplane")

# Check if an element is in the set
contains_airplane = "airplane" in Randset
contains_best = "best" in Randset

# Iterate through the set
print("Random Set:")
for iteration in Randset:
    print(iteration)

# Create another set
beverages = {"coke", "sprite", "orange"}

# Perform set operations
union_fruits_citrus = Randset.union(beverages)
intersection_fruits_citrus = Randset.intersection(beverages)
difference_fruits_citrus = Randset.difference(beverages)

# Print the results
print("Contains 'best'? ", contains_best)
print("Contains 'airplane'? ", contains_airplane)
print("Union of Random set and beverages:", union_fruits_citrus)
print("Intersection of Random set and beverages:", intersection_fruits_citrus)
print("Difference between Random set and beverages:", difference_fruits_citrus)
