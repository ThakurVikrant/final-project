#Temperature program in python

temperature = float(input("Enter the temperature: "))
conversion_type = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ")

if conversion_type == "C":
    converted_temp = (temperature * 1.8) + 32
    original_unit = "Celsius"
    converted_unit = "Fahrenheit"
else:
    converted_temp = (temperature - 32) / 1.8
    original_unit = "Fahrenheit"
    converted_unit = "Celsius"


print(f"{temperature} degrees {original_unit} is {converted_temp:.1f} degrees {converted_unit}.")


