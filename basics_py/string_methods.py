name: str = input("Enter your name: ")
phone_number: str = str(input("Enter your phone number: "))
name_length = len(name) # Get the length of the name
name_reversed = name[::-1] # Reverse the name
name_isdigit = name.isdigit() # Check if the name consists only of digits
name_upper = name.upper() # Convert the name to uppercase
name_lower = name.lower() # Convert the name to lowercase
name_capitalize = name.capitalize() # Capitalize the first letter of the name
name_isalpha = name.isalpha() # Check if the name consists only of alphabetic characters
phone_number_count = phone_number.count("-") # Count the occurrences of "-" in the phone number
phone_number_replace = phone_number.replace("-", ".") # Replace all occurrences of "-" with an empty string
print(phone_number_count) # Print the count of occurrences of "-" in the phone number
print(phone_number_replace) # Print the modified phone number