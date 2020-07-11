class Dog:

    species = 'Mammal'

    @classmethod
    def name(cls):
        return cls.__name__

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def age(self):
        from random import randint
        return randint(1, 20)

    def intro(self):
        print(f"Woof! I'm a {self.name}, of {self.__class__.name()} and {self.__class__.species}. "
              f"My breed is {self.breed}. Nice to meet you!")


# INHERITANCE
class Pug(Dog):

    breed = "Pug"

    def __init__(self, name, age):
        super().__init__(self.breed, name)
        self.age = age

    # override the method of inherited class
    def age(self):
        print(f"I'm {self.age} years old")
        return self.age

    def intro(self):
        print(f"Woof! I'm a {self.name}, of {self.__class__.species}. "
              f"My breed is {self.breed}. Nice to meet you! WOOF WOOF")

    def favourite_bites(self):
        print("I'd like to eat crispy chips all day long! Yammyyy")


# POLYMORPHISM
class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says MEOW!")


# POLYMORPHISM
class Hamster:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " says ....")


sneaker = Cat("Sneaker")
sneaker.speak()

popper = Hamster('Popper')
popper.speak()

for pet in [popper, sneaker]:
    print(type(pet))
    print(type(pet.speak))


# POLYMORPHISM #2
# (on abstract classes)
class Animal:

    def __init__(self, name):
        self.name = name

    # abstract method
    def speak(self):
        raise NotImplemented("Subclass must implement this abstract method")

class Dog(Animal):

    def speak(self):
        return self.name + " says WOOF!"

class Cat(Animal):

    def speak(self):
        return self.name + " says MEOW!"


fin = Dog("Fin")
print(fin.speak())
isis = Cat("Isis")
print(isis.speak())

if __name__ == "__main__":
    rocky_the_pug = Pug(name="Doughnut", age=0.75)
    rocky_the_pug.intro()



