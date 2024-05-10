def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
celsius_input = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius_input))

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit_input))
