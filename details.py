# Starting by creating some inputs to collect information from users and store them in variables

# Ask user for their name
name = str(input("Your Name: "))
# Ask user their age
age = int(input("Your Age: ")) 
# Ask user their house number
house_num = int(input("Your House Number: "))
# Ask user the street name
street_name = str(input("Your Street Name: "))
# Ask user their origin country
nationality = str(input("What country are you from: "))

# Print the user inputs
print(f'This is {name}, born in {nationality}, has {age} years old. Lives at door number {house_num} on {street_name}.')
