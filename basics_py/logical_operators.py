# exempeles 



temp = float(input("Enter the temperature: "))
is_raining = input("Is it raining? (yes/no): ").lower() 


if temp > 10 and is_raining == "yes": # and = both conditions must be true
    print("It's warm and raining.")
elif temp > 10 or is_raining == "yes": # or = at least one condition must be true
    print("It's either warm or raining.")           
elif temp <= 10 and is_raining == "yes":
    print("It's cold and raining.")
elif temp <= 10 and is_raining == "no":
    print("It's cold and not raining.")
elif temp > 10 and is_raining == "no":
    print("It's warm and not raining.")
else:
    print("It's cold and not raining.")
