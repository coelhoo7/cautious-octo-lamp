# Starting by creating some inputs to collect information from users and store them in variables

name = str(input("Your Name: "))
age = int(input("Your Age: ")) 
house_num = int(input("Your House Number: "))
street_name = str(input("Your Street Name: "))

print(f'This is {name}, has {age} years old. Lives at door number {house_num} on {street_name}.')
