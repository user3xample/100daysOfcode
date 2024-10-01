#! /usr/bin/env python3

# unlimited positional arguments

def add(*args):  # we can call it anything other than args if wanted
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(1, 2, 2)) # prints 5

print(add(1,2,3,4,5,6,7,8,9))  # prints 45

print(add(11,12,13,14,15,16,17,18,19))  # prints 135

##########################################################################

# keyword unlimited arguments
def calculate(n,**kwargs):  # key word arguments
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():  # because we have creaded a dict
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
print(my_car.make, my_car.model)

# leave one off because we use get its all good.
my_car = Car(make="Nissan")
print(my_car.make, my_car.model)