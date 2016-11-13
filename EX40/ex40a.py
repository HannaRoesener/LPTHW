mystuff = {'apple': "I AM APPLES!"}
print mystuff['apple'] # get apple from dict (key is a string, syntax is [key])


import mystuff
mystuff.apple() # get apple from module (key is identfier, sythax is .key )
print mystuff.tangerine # same thing, it's just a variable


class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

thing = MyStuff() # instantiate operation
thing.apple()
print thing.tangerine

# dict style
mystuff['apples']

# module style
mystuff.apples()
print mystuff.tangerine

# class style
thing = MyStuff()
thing.apples()
print thing.tangerine
