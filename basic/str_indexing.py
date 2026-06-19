number: str = "1234-5678-9012-3456" # Example phone number
print(number[0]) # Print the first character in the string
print(number[1]) # Print the second character in the string
print(number[:4]) # Print the first four characters in the string
print(number[5:9]) # Print characters from index 5 to 8
print(number[10:14]) # Print characters from index 10 to 13
print(number[-4]) # Print the fourth character from the end
print(number[-4:]) # Print the last four characters in the string
print(number[::2]) # Print every second character in the string = number[:-1] # Reverse the string
last_digits = number[-4:] # Get the last four digits of the string
print(f"XXXX-XXXX-XXXX-{last_digits}") # Print the reversed string