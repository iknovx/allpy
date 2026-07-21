import time


class TemperatureConverter:

    def __init__(self, temperature, unit):
        unit = unit.upper()
        if unit not in ("C", "F", "K"):
            raise ValueError(f"Unknown unit: {unit}. Use C, F, or K.")
        self.temperature = temperature
        self.unit = unit

    def to_celsius(self):
        if self.unit == "C":
            return self.temperature
        elif self.unit == "F":
            return (self.temperature - 32) * 5/9
        elif self.unit == "K":
            return self.temperature - 273.15

    def to_fahrenheit(self):
        celsius = self.to_celsius()
        return (celsius * 9/5) + 32 # type: ignore

    def to_kelvin(self):
        celsius = self.to_celsius()
        return celsius + 273.15 # type: ignore

    def __repr__(self):
        return f"TemperatureConverter({self.temperature}, '{self.unit}')"

    def __str__(self):
        return f"{self.temperature}°{self.unit}"


def convert():

    print("Welcome to the temperature converter!")
    print("You can convert between Celsius, Fahrenheit, and Kelvin.")
    print("Enter 'Q' to quit.")

    while True:

        unit = input("\nEnter the unit (C, F, K) or Q to quit: ").upper()

        if unit == "Q":
            print("Exiting the temperature converter.")
            time.sleep(1)
            break

        if unit not in ["C", "F", "K"]:
            print("Invalid unit. Please enter C, F, K or Q.")
            continue

        try:
            temperature = float(input("Enter the temperature: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if unit == "K" and temperature < 0:
            print("Kelvin can't be negative. Absolute zero is 0K.")
            continue

        try:
            temp = TemperatureConverter(temperature, unit)
        except ValueError as e:
            print(e)
            continue

        print(f"\nInput: {temperature}°{unit}")
        print(f"Celsius: {temp.to_celsius():.1f}°C")
        print(f"Fahrenheit: {temp.to_fahrenheit():.1f}°F")
        print(f"Kelvin: {temp.to_kelvin():.1f}K")


if __name__ == "__main__":
    convert()