# defines parameters and gives them values
people = 30
cars = 40
trucks = 15

# if there are more cars than people:
if cars > people:
    print "We should take the cars."

# other possibility: more people than cars.
elif cars < people:
    print "We should not take the cars."
# in case none of the above is true:
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still cannot decide."

if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
