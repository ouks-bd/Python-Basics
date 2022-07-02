#on =True

def add():

    a=float(input("Enter a number."))
    b=float(input("enter seconed number."))

    print(a+b)

def Subtraction():
    a=float(input("Enter a number."))
    b=float(input("enter seconed number."))

    print(a-b)

def Multiply():
    a=float(input("Enter a number."))
    b=float(input("enter seconed number."))

    print(a*b)

def devide():

    a=float(input("Enter a number."))
    b=float(input("enter seconed number."))

    print(a/b)
#while on:
operation = input("Please input +,-, *,/ or O")

if operation == '+':
    add()
elif operation == '-':
    Subtraction()
elif operation == '*':
    Multiply()
elif operation == '/':
    devide()
#elif operation == 'O':
 #   on=False
else:
    print("That Operation Not Avilable")

add()
Subtraction()
Multiply()
devide()
