from converter import convertToCelsius
from converter import convertToSelected

try:
    temperature = float(input("What's the temperature? (Numerical Value Only) "));
except ValueError:
    print("Please enter a valid Number.");
    exit();

from_unit = input("Is that in Celsius, Farenheit or Kelvin? ").strip().lower()[0];
to_unit = input("What unit of temperature would you like to convert to? (Celsius, Farenheit or Kelvin) ").strip().lower()[0];


temp_celsius = convertToCelsius(temperature,from_unit);
final_value = convertToSelected(temp_celsius, to_unit);

if to_unit == "c":
    print(f"The temperature is {round(final_value, 2)}°C");
elif to_unit == "f":
    print(f"The temperature is {round(final_value, 2)}°F");
elif to_unit == "k":
    print(f"The temperature is {round(final_value, 2)}K");
else:
    print("There has been an error.")
