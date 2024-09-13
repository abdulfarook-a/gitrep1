# OOPS - Object Oriented program
# object - Every instance in python called an object 
# Class - bule pring for similar object 

"""
Object two types:
1} Attributes = data discribing object -- eg., cars
2} Behaviour - Methods of an object -- eg ., speed variation
"""
# Basic Class and object 

class cars():
    def __init__(self,model,speed) :
        self.model= model
        self.speed= speed
    def _speed(self):
        print("the speed of bmw is :", self.speed)
bmw=cars('bmw',135)
audi = cars('audi',300)
bmw._speed()
audi._speed()
#-------------------------------Inheritance -----------------------------------
'''    it is the mechanis, for a new class to use the feature of anothe class           '''


class car():
    def __init__(self,year,speed):
        self.year=year
        self.speed=speed
    def getspeed(self):
        print(f"Speed of car {self.speed} km/h")
bmw = car(2016,200)
bmw.getspeed()
class sedan(car):
    def accelation(self):
        print(137)
    def openTrunk(self):
        print('Trunckis open')
class suv(car):
    def accelation(self):
        print(125)
honda=sedan(2018,150)
bmw.getspeed()
honda.getspeed()
honda.openTrunk()

#-------------------- Encapsulation -----------------------------
''' The preventing data from direct access is call encapsulation '''
class car():
    def __init__(self,year,speed):
        self.year=year
        self.speed=speed
    def getspeed(self):
        print(f"Speed of car {self.speed} km/h")
bmw = car(2016,200)
bmw.getspeed()

# ---------------------- polymorphism ------------------------------
''' it is a feature of using the same function in multiple ways '''
class car():
    def __init__ (self,name):
        self.name=name
class sedan(car):
    def accelaration(self):
        print(150)
class suv(car):
    def accelaration(self):
        print('180')
obj=[sedan('camry'),suv('scorpio')]
for i in obj:
    print(i.name ,":", end="")
    i.accelaration()
