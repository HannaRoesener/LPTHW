class Parent(object):
# defines the parent class

    def override(self):
        print "PARENT override()"
    # the parent class overrides itself

    def implicit(self):
        print "PARENT implicit()"
    # the parent class implicits itself
    def altered(self):
        print "PARENT altered()"
    # the new parent class

class Child(Parent):
# the child class is-a sub of the parent class
    def override(self):
        print "CHILD override()"
    # if the childclass overrides itself
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        # the new child class (the one from the original parent class)
        super(Child, self).altered()
        # this is calling the new parent class (the altered parent class)
        # and is altering the Child class based on the altered parent class
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()
# this is to define who every class belongs to (gives names/ objects)

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
