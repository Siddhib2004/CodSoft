#TASK 2
#Simple Calculator

def sum(a,b):
    sum = a+b
    return sum

def sub(a,b):
    subtraction = a - b
    return subtraction

def mul(a,b):
    product = a*b
    return product

def div(a,b):
    division = a/b
    return division

def power(a,b):
    power = a**b
    return power

def mod(a,b):
    modulo = a%b
    return modulo


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
operation_choice = input("Enter which number of operation you want to perform: \n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Power\n 6. Modulo\n")

if operation_choice == "1":
    sum(a,b)
    print("The sum is: ", sum(a,b))

elif operation_choice == "2":
    sub(a,b)
    print("The subtraction is: ", sub(a,b))

elif operation_choice == "3":
    mul(a,b)
    print("The multiplication is: ", mul(a,b))

elif operation_choice == "4":
    div(a,b)
    print("The division is: ", div(a,b))

elif operation_choice == "5":
    power(a,b)
    print("The power is: ", power(a,b))

elif operation_choice == "6":
    mod(a,b)
    print("The mod is: ", mod(a,b))


else:
    print("Invalid operation asked")



