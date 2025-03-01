number=10
for i in range(1,number+1):
    for j in range(1,number+1):
        print(f"{i} * {j} = {i * j}")

    print(" ")
print("Tables :  Done ")

# after long days of gap :

x=int(input("enter the number :"))
print("positive"if x>-1 else "Negetive")
print ("Even" if x%2==0 else "Odd")


# Strings in Python

name=input("Enter Your Name : ")

# length=len(name)
# length=name.find(" ")
# length=name.rfind("b")
# name=name.capitalize(); # ram => Ram
# name=name.upper();# ram => RAM
# name=name.lower();


print(name)