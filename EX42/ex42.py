## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a class related to the animal class (child of animal class)
class Dog(Animal):

    def __init__(self, name):
        ## self(Dog) has-a object (name) --> references to the name
        self.name = name

## Cat is-a class in relation to animal class
class Cat(Animal):

    def __init__(self, name):
        ## self(cat) has-a relation to animal (reference)

## Person is-a object wihtin a class
class Person(object):

    def __init__ (self, name):
        ## cat name is refering to name (has-a)
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Person is-a object in the class of employees
class Employee(Person):

    def __init__(self, name, salary):
        ## super class inherits employees class and has-a relation to them
        super(Employee, self).__init__(name)
        ## self.salary has-a relation to the actual salary

## Fish is-a object in a class
class Fish(object):
    pass

## Fish is-a object in the Salmon class
class Salmon(Fish):
    pass

## Fish is-a object within the class Halibut
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## Frank is an emplyee that earns 120000
frank = Employee("Frank", 120000)

## frank has-a pet called rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## salmon is-a course
course = Salmon()

## Halibut is-a harry
harry = Halibut()
