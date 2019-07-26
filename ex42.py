## Animal is-a object (yes, sort of confusing) look at extra credit
class Animal(object):
    pass

#  dog is-a animal
class Dog(Animal):
# dog has-a name
    def __init__(self, name):
        self.name = name
#  cat is-a animal
class Cat(Animal):
# cat has-a name
    def __init__(self, name):
        self.name = name
# person is-a object
class Person(object):
# person has a name
    def __init__(self, name):
        self.name = name
        #person has-a pet, default is set to no pet
        self.pet = None 

# employee is-a person
class Employee(Person):
# class object within a class object, emplyee has-a name and salary, super has-a emplyee and salary
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 1200000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()