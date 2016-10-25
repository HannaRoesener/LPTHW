
print "What is your name?",
name = raw_input()
print "How old are you?",
age = raw_input()
print "Are you a man or a female?", 
gender = raw_input()

from sys import argv

script, name, age, gender = argv

print "The script you are working with is called:", script
print "The person using Python is called:", name
print "The person using this is", age
print "The person using this is a", gender
