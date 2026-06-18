

class TemperatureConverter:

    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit.upper()

    def to_celsius(self):
        if self.unit == "C":
            return self.temperature
        elif self.unit == "F":
            return (self.temperature - 32) * 5/9
        elif self.unit == "K":
            return self.temperature - 273.15

    def to_fahrenheit(self):
        celsius = self.to_celsius()
        return (celsius * 9/5) + 32

    def to_kelvin(self):
        celsius = self.to_celsius()
        return celsius + 273.15


def convert():

    print("Welcome to the temperature converter!")
    print("You can convert between Celsius, Fahrenheit, and Kelvin.")
    print("Enter 'Q' to quit.")

    while True:

        unit = input("\nEnter the unit (C, F, K) or Q to quit: ").upper()

        if unit == "Q":
            print("Exiting the temperature converter.")
            break

        if unit not in ["C", "F", "K"]:
            print("Invalid unit. Please enter C, F, K or Q.")
            continue

        try:
            temperature = float(input("Enter the temperature: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        temp = TemperatureConverter(temperature, unit)

        print(f"\nInput: {temperature}°{unit}")
        print(f"Celsius: {temp.to_celsius():.2f}°C")
        print(f"Fahrenheit: {temp.to_fahrenheit():.2f}°F")
        print(f"Kelvin: {temp.to_kelvin():.2f}K")


if __name__ == "__main__":
    convert()