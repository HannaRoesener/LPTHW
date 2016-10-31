def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Let's do some math with just function!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# begin in the last bracket --> ((((IQ/2)*Weight)-heigth)+age)

print "That becomes: ", what, "Can you do it by hand?"

print "After I worked out how the formula works, here is what I wanted to calculate."
what_two = add(height, subtract( weight, multiply(age, 5)))
print "That becomes:", what_two, "Can you see why?"
print "Here is what I wrote down by hand:"
print "(((age*5)- weight)+ height)"
