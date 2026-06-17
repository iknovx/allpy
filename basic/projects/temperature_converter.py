class TemperatureConverter:

    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5/9

    def celsius_to_kelvin(self):
        return self.temperature + 273.15

    def kelvin_to_celsius(self):
        return self.temperature - 273.15

    def fahrenheit_to_kelvin(self):
        return (self.temperature - 32) * 5/9 + 273.15

    def kelvin_to_fahrenheit(self):
        return (self.temperature - 273.15) * 9/5 + 32


def convert():

    print("Welcome to the temperature converter!")
    print("You can convert between Celsius, Fahrenheit, and Kelvin.")
    print("Enter 'Q' to quit the converter.")

    while True:

        unit = input("\nEnter the unit (C, F, K) or Q to quit: ").upper()

        if unit == "Q":
            print("Exiting the temperature converter.")
            break

        if unit not in ["C", "F", "K"]:
            print("Invalid unit. Please enter C, F, K or Q.")
            continue

        temperature = float(input("Enter the temperature: "))

        temp = TemperatureConverter(temperature, unit)

        if unit == "C":
            print(f"{temperature}°C = {temp.celsius_to_fahrenheit():.2f}°F")
            print(f"{temperature}°C = {temp.celsius_to_kelvin():.2f}K")

        elif unit == "F":
            print(f"{temperature}°F = {temp.fahrenheit_to_celsius():.2f}°C")
            print(f"{temperature}°F = {temp.fahrenheit_to_kelvin():.2f}K")

        elif unit == "K":
            print(f"{temperature}K = {temp.kelvin_to_celsius():.2f}°C")
            print(f"{temperature}K = {temp.kelvin_to_fahrenheit():.2f}°F")


convert()