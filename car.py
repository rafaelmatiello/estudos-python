
class Car:
    def __init__(self):
        self.make = 'vw'
        self.name = 'gol'
        self.year = 2019
        self.color = 'blue'

   ##def __init__(self,name, make, year, color ):
   ##     self.make = make
   ##     self.name = name
   ##     self.year = year
   ##     self.color = color

    def drive(self):
        print(self.name + " started")

    @staticmethod
    def hello():
        print("hello world")