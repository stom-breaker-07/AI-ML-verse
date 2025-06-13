# Overriding in the consept of OOPS

class Employe:
    def __init__(self , name,sal):
        self.name=name
        self.salary=sal
    def get_Salary(self):
        return self.salary
    def set_Salary(self,a):
        self.salary=a

class Sales_Manager(Employe):
    def __init__(self,name,sal,inc):
        super().__init__(name,sal)
        self.incentive=inc
    def get_Salary(self):
        return self.salary+self.incentive


e1=Sales_Manager('Charan',100000,25000)
print(f'{e1.name} would get {e1.get_Salary()} in this mounth ')