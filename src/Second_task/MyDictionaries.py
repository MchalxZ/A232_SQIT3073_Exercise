lecturer = {
    "name": "IKUN",
    "age": int(38),
    "highest_education": "PHD in information technology",
    "subject_group": {
        "SQIT1013":{'A','C'},
        "SQIT3073":{'B','E'},
        "SQIT3083":{'D','E'}
    }
}



# Access dictionary values by keys
student_name = lecturer["name"]
student_age = lecturer["age"]

# Modify dictionary values
lecturer["age"] = 21
lecturer["subject_group"]["SQIT1013"] = {'A','D'}

# Add a new key-value pair
lecturer["gender"] = "Female"

# Check if a key exists in the dictionary
has_major = "weight" in lecturer
has_height = "contact number" in lecturer

# Get the list of keys and values
keys = lecturer.keys()
values = lecturer.values()

# Iterate through the dictionary
print("Lecturer Information:")
for key, value in lecturer.items():
    print(f"{key}: {value}")

# Remove a key-value pair
del lecturer["subject_group"]

# Print the updated dictionary
print("\nLecturer Information after removing 'subject_group':")
for key, value in lecturer.items():
    print(f"{key}: {value}")