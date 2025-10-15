# Personal Information Manager
# This program collects and displays personal information such as name, age, city, and hobbies.

# Get user's name (string)
name = input("Enter your name: ")

# Get user's age (integer)
# Convert input string to integer and handle invalid input
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid number for age.")

# Get user's city (string)
city = input("Enter your city: ")

# Get user's hobbies as a comma-separated string, then convert to a list
hobbies_input = input("Enter your hobbies (separate by commas): ")
# Split hobbies and strip extra spaces
hobbies = [hobby.strip() for hobby in hobbies_input.split(",")]



# Display formatted output with string concatenation and f-string
print("\n--- Personal Information ---")
print("Name: " + name)
print(f"Age: {age}")
print("City: " + city)
print("Hobbies: " + ", ".join(hobbies))



