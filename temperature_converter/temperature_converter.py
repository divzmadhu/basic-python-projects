"""
Mini Project Scenario: Temperature Converter (Real-Time Use Case)
Project Name:

Weather Station Helper – Temperature Converter

Real-Life Scenario:

You are helping a small community weather station that records temperature data.
The volunteers collect temperatures in Celsius, Fahrenheit, or Kelvin, depending on the sensor they use.

They need a simple Python program that:

Asks the user what type of temperature they have measured

Accepts the temperature value

Converts it into the other two temperature units

Prints a clean, friendly output that they can note down in their logbook

*****Sample input and output******
Event/Description	Input (°C)	Output (°F)	Output (K)
Absolute Zero	−273.15	−459.67	0.00
Water Freezing	0.00	32.00	273.15
Comfortable Room Temp	20.00	68.00	293.15
Human Body Temp	37.00	98.60	310.15
Water Boiling	100.00	212.00	373.15


"""
temperature = float(input("Enter the temperature you want to convert: "))

unit = input("Which unit do you want to convert from? (C/F/K): ").upper()


if unit == 'C':
    c_temperature = temperature
    f_temperature = (c_temperature * 9 / 5) + 32
    k_temperature = c_temperature + 273.15
elif unit == 'F':
    f_temperature = temperature
    c_temperature = (f_temperature - 32) * 5 / 9
    k_temperature = ((f_temperature - 32) * 5 / 9) + 273.15
elif unit == 'K':
    k_temperature = temperature
    c_temperature = k_temperature - 273.15
    f_temperature = (k_temperature - 273.15) * 9 / 5 + 32
print("\nCelcius      Fahrenheit     Kelvin")
print(f"\n{c_temperature:.2f}         {f_temperature:.2f}          {k_temperature:.2f} ")

