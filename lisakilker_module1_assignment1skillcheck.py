def skillCheck():
    #gets user input
    input1 = input("Enter a number: ")
    input2 = input("Enter another number: ")

    value1 = float(input1)
    value2 = float(input2)

    return value1, value2

# Calls the function and get the values
value1, value2 = skillCheck()

# Prints the values
print("Your first value is: ", value1)
print("Your second value is: ", value2)
print("The numbers added together is: ", value1 + value2)
print("The first number minus the second number is: ", value1 - value2)
print("The numbers multiplied together is: ", value1 * value2)
print("The first number divided by the second number is: ", value1 / value2)
