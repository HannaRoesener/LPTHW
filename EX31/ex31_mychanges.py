print "You enter a dark room with two doors and a tunnel. Do you go through door #1 or door #2 or the tunnel #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your leg off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthuluh's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print "It is so dark you can barely see a thing."
    print "At the end of the tunnel you see something glowing. Something blue."
    print "Are you walking towards the blue?"

    blue = raw_input("> ")

    if blue == "Yes":
        print "A stormtuper comes out of nowhere, thinks you are an enemy and kills you."
    elif blue == "No":
        print "You find youself back in the room with two doors, #1 and #2, and one tunnel #3."
        print "Which way are you going?"

        door = raw_input("> ")

else:
    print "You stumble around and fall on a knife and die. Good job!"
