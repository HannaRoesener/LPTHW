from sys import argv

script, user_name = argv
help = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(help)

print "Where do you live %s?" % user_name
lives = raw_input(help)

print "What kind of computer do you have?"
computer = raw_input(help)

print "Are you a computer freak?"
freak = raw_input(help)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Oh that's funny. So you are a freak? - %r. Just like me.
""" % (likes, lives, computer, freak)