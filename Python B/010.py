# inheritance Topic in OOPs

class Quadrilaterel:
    def __init__(self,a,b,c,d):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        self.side4 = d
    def perimeter(self):
        p=self.side1+self.side2+self.side3+self.side4
        print(f"Perimeter of Quad is {p}")

class Rectangle_Shape(Quadrilaterel):
    def __init__(self,a,b,c=None,d=None):
        super().__init__(a,b,c,d)
        self.side3=self.side1
        self.side4=self.side2

#Parent Class
Q1=Quadrilaterel(6,5,7,4)
Q1.perimeter()

#Child class
r1=Rectangle_Shape(4,5)
r1.perimeter()
