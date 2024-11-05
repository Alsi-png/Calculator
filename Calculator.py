# we wamt to do next operations in this code:
# 1.-
# 2.+
# 3.*
# 4./
# 5.pi

import math

print("""Hello, What would you like to calculate here today?
What can calculator do:
1. You can use +
2. You can -
3. You can *
4. You can /
5. You can multiply with pi
""")

user_input = input("In order to use calculator, write 1-5: ")

try:
    user_input = int(user_input)
    if user_input > 5 or user_input < 1:
        raise Exception("Your input should be in a range of 1 to 5")
except ValueError:
    raise TypeError("No strings are allowed in the calculator")


def sum_function():
    print('Here we will summarise a and b together')
    a = int(input("Write number a: "))
    b = int(input(("Write number b: ")))
    print(a+b)


def sub_function():
    print('Here we will subtract b from a')
    a = int(input("Write number a: "))
    b = int(input(("Write number b: ")))
    print(a-b)


def multiply_function():
    print('Here we will multiply a with b')
    a = int(input("Write number a: "))
    b = int(input(("Write number b: ")))
    print(a*b)


def divide_function():
    print('Here we will divide a with b')
    a = int(input("Write number a: "))
    b = int(input(("Write number b: ")))
    print(a/b)


def multiply_function_pi():
    print('Here we will multiply a with pi')
    a = int(input("Write number a: "))
    print(a*math.pi)


if user_input == 1:
    sum_function()
elif user_input == 2:
    sub_function()
elif user_input == 3:
    multiply_function()
elif user_input == 4:
    divide_function()
elif user_input == 5:
    multiply_function_pi()


print("Thank you for computing with us :)")
