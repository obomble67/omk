//input = input("Enter something: ")
//print("You entered:", input)
//print("Google cloud API")
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    Formula: (°C × 9/5) + 32 = °F
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    Formula: (°F − 32) × 5/9 = °C
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example usage
celsius_input = float(input("Enter temperature in Celsius: "))
converted_fahrenheit = celsius_to_fahrenheit(celsius_input)
print("Temperature in Fahrenheit:", converted_fahrenheit)

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
converted_celsius = fahrenheit_to_celsius(fahrenheit_input)
print("Temperature in Celsius:", converted_celsius)
