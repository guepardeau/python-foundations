from converter import convertkilograms;
from converter import result;
weight = float(input("Please enter the value of weight numerically: "));
from_unit = input("Please enter a unit of measurement(g,kg,lbs or oz): ");
to_unit = str(input("Please enter the unit you would like to convert to (g,kg,lbs or oz): "))

output = convertkilograms(from_unit, weight);
final_value = result(output, to_unit);

if final_value is not None:
    print(f"The weight is {final_value}{to_unit}.");
else:
    print("There was an error.")






