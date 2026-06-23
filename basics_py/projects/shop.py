fruits = []
prices = []
total = 0
while True:
    fruit = input("Enter a food to buy (q to quit): ")
    if fruit == "q":
        break
    else:
        price = float(input(f"Enter the price of a {fruit}: "))
        prices.append(price)
        fruits.append(fruit)
        total += price          
        print(fruits, prices)
    while True:
            answer = input("Do you want to see prices and fruits? (y or n):")
            if answer == "y":
                for fruit in fruits:
                    print(fruit, end = " ")
            else:
                break

print(f"Total: {total}")  