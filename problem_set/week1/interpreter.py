#  implement a program that prompts the user for an arithmetic expression and then calculates
#  and outputs the result as a floating-point value formatted to one decimal place.

expression = input("Expression: ").split()

x = float(expression[0])
y = expression[1]
z = float(expression[2])

if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/" :
    result = x / z 

print(f"{result:.1f}")

 

