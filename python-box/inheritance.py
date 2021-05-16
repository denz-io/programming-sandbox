class Mammal:
  def breathing(self):
    print('Breathing')

class Human(Mammal):
  def think(self):
    print('Thinking') 
class Dog(Mammal):
  def bark(self):
    print('Barking')

person = Human()
person.breathing()
person.think()

dog = Dog()
dog.breathing()
dog.bark()
