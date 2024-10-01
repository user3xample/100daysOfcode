#! /usr/bin/env python3


class Animal:
    def __init__(self):
        self.num_eyes =2

    def breathe(self):
        print("in, out , breathe")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):  # we dont need to do this if we dont want to add extra stuff.
        super().breathe()  # this means we inherit everything above and the added extra
        print("We are doing this underwater")

    def swim(self):
        print("moving in water")

# Above we have two classes Animal and Fish fish is inheriting the animal class.

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
