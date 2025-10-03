import sys

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

opr = input("Enter Operator: ")


if opr == "+":
    output = num1+num2
    print("Your calculation is: ", output)

elif opr == "-":
    output = num1-num2
    print("Your calculation is: ", output)

elif opr == "*":
    output = num1*num2
    print("Your calculation is: ", output)

elif opr == "%":
    output = num1%num2
    print("Your calculation is: ", output)

else:
    sys.exit("********Invalid input detected*******")
