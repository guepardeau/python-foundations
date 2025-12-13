x = float(input("Please enter your first number: "));
y = float(input("Please enter your second number: "));
operator = (str(input("Please enter whether you would like to +,-,*,/ the first number to the second number: ")));
from calculator import add;
from calculator import subtract;
from calculator import multiply;
from calculator import divide;


if operator == "+":
    result = add(x,y)
    print(result);
elif operator == "-":
    result = subtract(x,y)
    print(result);
elif operator == "*":
    result = multiply(x,y)
    print(result);
elif operator == "/":
    result = divide(x,y)
    print(result);
else:
    print("You did not enter a valid operator.");