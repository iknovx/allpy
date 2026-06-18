name: str = input("Enter your name: ")

name_length = len(name) # Get the length of the name
name_reversed = name[::-1] # Reverse the name
name_isdigit = name.isdigit() # Check if the name consists only of digits
name_upper = name.upper() # Convert the name to uppercase
name_lower = name.lower() # Convert the name to lowercase
name_capitalize = name.capitalize() # Capitalize the first letter of the name
name_isalpha = name.isalpha() # Check if the name consists only of alphabetic characters
print(name_isalpha) # Print the modified name