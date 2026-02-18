"""
class with init method
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("x",20)
p2 = Person("y",25)

print(p1.name,p1.age)
print(p2.name,p2.age)