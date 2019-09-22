#!/usr/bin/env python3
# ./sully.py
# affichage d'une liste d'une classe

class Person():
    def __init__(self, name, age, parent=None):
        self.name = name
        self.age = age
        self.child = []

    def __repr__(self):
        return "I'm %s and I am %d years old" % (self.name, self.age)

    def addchild(self, name, age):
        self.child.append(Person(name, age, parent=self))
        print("Add %s's child's %s %d years old" % (self.name, name, age))

    def displayChild(self):
        if len(self.child) > 0:
            print("%s has children : " % self.name)
            for c in self.child:
                print("%s %d years old" % (c.name, c.age))
        else:
            print("%s has no children")


########################## TEST ##########################
####################################################
# Instancie une nouvelle person
tom = Person("Tom", 45)

# Print tom
print(tom)
# Add Tom childs
tom.addchild("Tony", 5)
tom.addchild("Steve", 15)

# Affiche les enfants de Tom
tom.displayChild()
