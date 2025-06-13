# class and Getter and setter Method

class Car:
    def __init__(self,a=40):
        self._speed=a         #_ (underScore) Makes the object private according to Data encapsulation
    def getSpeed(self):
        return self._speed
    def setSpeed(self,b):
        if b<=0 or b>=160:
            print("Speed needs to be in range of 0 to 160")
        else:
            self._speed=b
        return
    speed=property(getSpeed,setSpeed)

#Getter and Setter Method are used
Polo=Car()
print(Polo.getSpeed())
Polo.setSpeed(180)
print(Polo.getSpeed())

# After using property method
print("After the Property Func() ")
print(Polo.speed)
Polo.speed=50
print(Polo.speed)