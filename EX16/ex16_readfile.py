from sys import argv

script, filename = argv

print "Hurray, you just edited a file by using your Terminal only."
print "Kind of magic, isn't it?"
print "Now we are going to see into that new file."
print "Just to remind you, the file you just changed is: %r." % filename

print "Opening the file..."
target = open(filename, 'r')

# target.read()

print "Hit ENTER when you want to close file."
raw_input("> ")

target.close()