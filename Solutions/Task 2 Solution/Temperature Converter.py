def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_converter(value, from_unit):
    if from_unit == "Celsius":
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return f"{value} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit and {kelvin} degrees Kelvin."
    elif from_unit == "Fahrenheit":
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return f"{value} degrees Fahrenheit is equal to {celsius} degrees Celsius and {kelvin} degrees Kelvin."
    elif from_unit == "Kelvin":
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return f"{value} degrees Kelvin is equal to {celsius} degrees Celsius and {fahrenheit} degrees Fahrenheit."
    else:
        return "Unknown temperature unit."

# Example usage
input_value = 20
input_unit = "Celsius"
output_message = temperature_converter(input_value, input_unit)
print(output_message)
