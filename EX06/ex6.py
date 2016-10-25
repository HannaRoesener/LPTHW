x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
# two statements - or defined variables

print x
print y
# display both variables

print "I said: %r." % x
print "I also said: '%s'." % y
# display them again, embedded into a different context

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e 