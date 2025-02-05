import math

# math module :

x=int (input("Enter the value of X :"))
y=float(input("Enter the Float value Y : "))

print(math.pi)
print(math.e)
print(math.sqrt(x))
print("Ceil of your float !!",math.ceil(y))
print("floar of your float !!",math.floor(y))

# usage of round for float

x=float(input("enter the Radius of the circle : "))
circumference = 2 * math.pi * x;
area=math.pi * pow(x,2)

print(f"circumference of the circle is {round(circumference  , 2)}")
print(f"Area of the circle if {round(area ,2)}")


# Python Caluculator

a =int(input("enter the value of First :"))
b =int(input("Enter the value of secound :"))

op=int(input("enter 1.add ,2 to subtract ,3 to multiply ,4 to dived " ))

if op==1:
    print(f"{a} + {b} = {a+b}")
elif op==2:
    print(f"{a} - {b} = { a-b}")
elif op==3:
    print(f"{a} * {b} = { a*b}")
elif op == 4:
    print(f"{a} / {b} = {a / b}")
else:
    print("enter the correct operator : ")