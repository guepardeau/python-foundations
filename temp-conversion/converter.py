def convertToCelsius(temperature, unit):
    if unit == "f":
        temperature = ((temperature - 32)/1.8);
    elif unit == "k":
        temperature = temperature - 273.15;
    elif unit == "c":
        pass;
    else:
        print("Please choose a valid unit of temperature. Try again.");
        exit();
    return temperature;

def convertToSelected(temp_celsius, to_unit):
    if to_unit == "f":
        temp_celsius = ((temp_celsius * 1.8) + 32);
    elif to_unit == "k":
        temp_celsius = temp_celsius + 273.15;
    elif to_unit == "c":
        pass;
    else:
        print("Please choose a valid unit of temperature. Try again.");
        exit();
    return temp_celsius;


