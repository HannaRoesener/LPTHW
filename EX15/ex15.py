# imports argument variable from system
from sys import argv

# tells program which arguments to type in when running program
script, filename = argv

# tells program to open the listed txt doc 
txt = open(filename)

# fills in commands from above (filename) 
print "Here's your file %r:" % filename
# reads the txt doc out loud 
print txt.read()

# prints line
# print "Type the filename again:"
# asks you to type txt filename again ("> " signals typing area)
# file_again = raw_input("> ")

# same file, different command, so system can distinguish
# txt_again = open(file_again)

# prints out txt doc again 
# print txt_again.read()