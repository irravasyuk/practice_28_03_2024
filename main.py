# Завдання 2
class Weels:
    def __init__(self, count):
        self.count = count

    def rotate(self):
        print('the wheels are turning')


class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print('the engine started')

    def stop(self):
        print('the engine stopped')


class Door:
    def __init__(self, num):
        self.num = num

    def open(self):
        print('the door is open')

    def close(self):
        print('the door is closed')


class Car(Weels, Engine, Door):
    def __init__(self, brand, model, year, count, capacity, num):
        Weels.__init__(self, count)
        Engine.__init__(self, capacity)
        Door.__init__(self, num)
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        print('the car is going.')


car = Car('Mazda', 'CX - 7', 2017, 4, 2.2, 4)
car.start()
car.drive()
car.rotate()
car.stop()
car.open()
car.close()


# Завдання 3
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def show(self):
        print(f'\nName: {self.name}')

    def type(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print('Woof')

    def type(self):
        print('type: dog')


class Cat(Animal):
    def __init__(self, name, fluffiness):
        super().__init__(name)
        self.fluffiness = fluffiness

    def sound(self):
        print('Meow')

    def type(self):
        print('type: cat')

class Parrot(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print('Squawk')

    def type(self):
        print('type: parrot')

class Hamster(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def sound(self):
        print('Squeak')

    def type(self):
        print('type: hamster')

dog = Dog('Bunny', 'dalmatian')
cat = Cat('Rick', 'fluffy')
parrot = Parrot('Morty', 'Yellow')
hamster = Hamster('Fill', 'Orange')

dog.show()
dog.sound()
dog.type()

cat.show()
cat.sound()
cat.type()

parrot.show()
parrot.sound()
parrot.type()

hamster.show()
hamster.sound()
hamster.type()


# Завдання 4 - 5
class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Print(self):
        print('\nThis is Employer class')

    def __str__(self):
        return f'Name: {self.name}\nAge: {self.age}'

    def __int__(self):
        return self.age

class President(Employer):
    def Print(self):
        print('\nThis is President class')

    def __str__(self):
        return f'President: {self.name}\nAge: {self.age}'

class Manager(Employer):
    def Print(self):
        print('\nThis is Manager class')

    def __str__(self):
        return f'Manager: {self.name}\nAge: {self.age}'

class Worker(Employer):
    def Print(self):
        print('\nThis is Worker class')

    def __str__(self):
        return f'Worker: {self.name}\nAge: {self.age}'

employer = Employer('Oleg', 28)
president = President('Lesya', 22)
manager = Manager('Ivan', 29)
worker = Worker('Bogdan', 21)

employer.Print()
print(employer)
print(int(employer))

president.Print()
print(president)
print(int(president))

manager.Print()
print(manager)
print(int(manager))

worker.Print()
print(worker)
print(int(worker))























