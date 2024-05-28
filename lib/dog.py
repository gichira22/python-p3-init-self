#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def sit(self):
        print(f"{self.name} is sitting.")
    
    def bark(self):
        print(f"{self.name} says woof!")
