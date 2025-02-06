#Python Weight Convertor

w=float(input("Enter the weight : "))
unit=input("Enter the Unit Kilogram(k) or Pounds(p) : ")

if unit=="k" :
    w=w*2.205
    unit="Lbs"
    print(f"Weight is {round(w, 1)} {unit}")
elif unit == "p" :
    w=w/2.205
    unit="Kg"
    print(f"Weight is {round(w, 1)} {unit}")
else:
    print(f"{unit} is an invalid unit !!!")



#Python Tempreture Convertor

unit=input("Enter the unit Celsius or Fahrenheit (C/F) : ")
t=float(input("Enter the temperature : "))

if unit=="C":
    t=round((9 * t)/5+32,1)
    print(f"Temperature is {t}°F")
elif unit=="F":
    t=round((t - 32)*9/5,1)
    print(f"Temperature is {t}°C")
else:
    print(f'{unit} is an invalid unit !!')

#Python and ,or and not Opearator

temp=26
is_sunny=False

if temp>25 and not is_sunny:
    print("it's Too Hot but Not sunny outSide ")
if temp > 25 and is_sunny:
    print("it's Too Hot but Sunny outSide ")
elif temp<0 and is_sunny:
    print("it's Too Cold but Sunny outSide ")
else:
    print("it's Warm and Sunny outSide ")