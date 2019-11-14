
class Car:
    def __init__(self):
        self.make = 'vw'
        self.name = 'gol'
        self.year = 2019
        self.color = 'blue'

    def drive(self):
        print(self.name + " started")

    @staticmethod
    def hello():
        print("hello world")