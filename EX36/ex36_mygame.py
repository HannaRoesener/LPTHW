print "\fBefore the game starts, please choose a name for your character."
name = raw_input("Name: ")

print "______________________________________"
print """
Please copy this URL and listen to the music while playing:
https://www.youtube.com/watch?v=Vxq_AnaB_tM
When you are done press ENTER."""

enter = raw_input("> ")

print """\nPicture this scene:
You are working as a police agent.

\t >>> Agent %s <<<

Today you have been called to a crime scene.
Someone has been murdered in an office.
You are the first to arrive at the building.
Reliable sources have confirmed that the bad guy is still inside somewhere.
Backup is on its way. For now you are on your own though.
You don't hesitate and rush into the building.
You look around and find youself in a huge foyer.
""" % name

def car_park():
    print "\nCAR PARK"
    print "There are big and expensive cars everywhere."
    print "Do you want to check the floor or go back upstairs?"
    choice = raw_input("\f'check' or 'lift' \n>> ")
    if choice == "check":
        print "Its very confusing down here. It takes you quit some time to search the car park."
        print "By the time you are done the murderer escaped through the foyer."
        print "Maybe you do better next time %s." % name

        print "\fDo you want to try again %s?" % name
        choice = raw_input(">> ")
        if choice == "yes":
            start()
        elif choice == "no":
            exit()
        else:
            print "It's a simple question that can only answered with 'yes' or 'no'."
            choice = raw_input(">> ")
            if choice == "yes":
                start()
            elif choice == "no":
                exit()
    elif choice == "lift":
        lift()
    else:
        print "\fWhat did you say you want to do?"
        choice = raw_input("'check' or 'lift' \n>> ")
        if choice == "check":
            print "Its very confusing down here. It takes you quit some time to search the car park."
            print "By the time you are done the murderer escaped through the foyer."
            print "Maybe you do better next time %s." % name

            print "\fDo you want to try again %s?" % name
            choice = raw_input(">> ")
            if choice == "yes":
                start()
            elif choice == "no":
                exit()
            else:
                print "It's a simple question that can only answered with 'yes' or 'no'."
                choice = raw_input(">> ")
                if choice == "yes":
                    start()
                elif choice == "no":
                    exit()
        elif choice == "lift":
            lift()
        else:
            print "\fOh dear, you better wait outide until help is coming."
            print "You really should slow down typing."
            print "\fDo you want to try again %s?" % name
            choice = raw_input(">> ")
            if choice == "yes":
                start()
            elif choice == "no":
                exit()
            else:
                print "It's a simple question that can only answered with 'yes' or 'no'."
                choice = raw_input(">> ")
                if choice == "yes":
                    start()
                elif choice == "no":
                    exit()

def foyer_room():
    print "'FOYER'"
    print "You can either go outside and wait for help"
    print "or take the lift to a different floor."
    print "What do you want to do %s?" % name

    choice = raw_input("\f'wait' or 'lift' \n>> ")
    if choice == "wait":
        print "You probably better get in there again. Or do you want to be responsible for the murderer escaping?"
        foyer_room()

    elif choice == "lift":
        lift()
    else:
        print "How long do you want to wait to make your next move? Remember there is a dangerous guy in the building! So again:"
        foyer_room()

def cafeteria():
    print "\nCAFETERIA"
    print "The smell of coffee is tempting. Oh and look at the jummy pastry. A little coffee break won't hurt anybody - wouldn't it?"
    print "Do you want to get a cup of coffee?"
    print "Or keep looking for the bad guy?"
    choice = raw_input("\f'coffee' or 'continue' \n>> ")
    if choice == "coffee":
        print "A very nice guy fixes you a cup of coffee."
        print "Do you want to take a short coffee break, or really enjoy your warm drink?"
        choice = raw_input("'short' or 'long' break? \n>> ")
        if choice == "short":
            print "The caffeine made you think clearer now."
            print "Wait a minute, why is there someone selling coffee anyway? There shouldn't be a person in here... except the murderer himself."
            print "Well done! It took you some time, but you sharpened your senses and managed to catch the bad guy. Wuuhuhu!\f"
        elif choice == "long":
            print "The coffee selling guy is gone... You were so deep in through that you didn't realize."
            print "By now he must be far, far away. What a shame!"

            print "\fDo you want to try again %s?" % name
            choice = raw_input(">> ")
            if choice == "yes":
                start()
            elif choice == "no":
                exit()
            else:
                print "It's a simple question that can only answered with 'yes' or 'no'."
                choice = raw_input(">> ")
                if choice == "yes":
                    start()
                elif choice == "no":
                    exit()

        else:
            print "\fSorry, can you type that again?"
            choice = raw_input("'short' or 'long' break? \n>> ")
            if choice == "short":
                print "The caffeine made you think clearer now."
                print "Wait a minute, why is there someone selling coffee anyway? There shouldn't be a person in here... except the murderer himself."
                print "Well done! It took you some time, but you sharpend your senses and managed to catch the bad guy. Wuuhuhu!\f"
            elif choice == "long":
                print "The coffee selling guy is gone... You were so deep in through that you didn't realize."
                print "By now he must be far, far away. What a shame!"

                print "\fDo you want to try again %s?" % name
                choice = raw_input(">> ")
                if choice == "yes":
                    start()
                elif choice == "no":
                    exit()
                else:
                    print "It's a simple question that can only answered with 'yes' or 'no'."
                    choice = raw_input(">> ")
                    if choice == "yes":
                        start()
                    elif choice == "no":
                        exit()
            else:
                print "\fSorry that was nonsense. Go back to the lift and make up your mind."
                lift()

    elif choice == "continue":
        print "You could question the coffee guy. Maybe he saw something?!"
        print "Check the room or go to another level."
        choice = raw_input("\f'question', 'check' or 'lift' \n>> ")
        if choice == "question":
            print "The coffee guy seems to be nice. But he does not know anything about the crime."
            print "Do you believe him?"
            choice = raw_input("\f'yes' or 'no' \n>> ")
            if choice == "yes":
                print "You decide not to waste any more time down here and go back to the lift."
                lift()
            elif choice == "no":
                print "Yeah, you are right. The whole sitation seems a bit odd."
                print "You hand-cuff the man and take him outside the building."
                print "After he has been taken into custody and many questionings it turns out he was the murderer."
                print "Agent %s you can be proud of yourself! You trusted your instincts and catch the bad guy." % name
            else:
                print "Please type in a clear answer."
                choice = raw_input("\f'yes' or 'no' \n>> ")
                if choice == "yes":
                    print "You decide not to waste any more time down here and go back to the lift."
                    lift()
                elif choice == "no":
                    print "Yeah, you are right. The whole sitation seems a bit odd."
                    print "You hand-cuff the man and take him outside the building."
                    print "After he has been taken into custody and many questionings it turns out he was the murderer."
                    print "Agent %s you can be proud of yourself! You trusted your instincts and catch the bad guy." % name
                else:
                    print "Sorry dude, GAME OVER! Maybe next time..."
                    print "Before you better learn to type."
                    print "\fDo you want to try again %s?" % name
                    choice = raw_input(">> ")
                    if choice == "yes":
                        start()
                    elif choice == "no":
                        exit()
                    else:
                        print "It's a simple question that can only answered with 'yes' or 'no'."
                        choice = raw_input(">> ")
                        if choice == "yes":
                            start()
                        elif choice == "no":
                            exit()

        elif choice == "check":
            print "The room looks fine."
            print "Do you need a short break?"
            choice = raw_input("'yes' or 'no' >> ")
            if choice == "yes":
                print "You decide to take a break and buy yourself a delicious piece pastry."
                print "You stare out of the window and don't see the coffee guy leaving."
                print "By the time you realise, it's too late."
                print "Your boss just let you know that somebody else had been killed one street away."
                print "You are being fired for carelessness."
                print "At least you tried agent %s." % name
                print "\fDo you want to try again %s?" % name
                choice = raw_input(">> ")
                if choice == "yes":
                    start()
                elif choice == "no":
                    exit()
                else:
                    print "It's a simple question that can only answered with 'yes' or 'no'."
                    choice = raw_input(">> ")
                    if choice == "yes":
                        start()
                    elif choice == "no":
                        exit()
            elif choice == "no":
                print "Good decision! Stay focused."
                print "There are still other rooms to check out."
                lift()

        elif choice == "lift":
            lift()
        else:
            print "You better make up your mind again and go back into the lift for now."
            lift()
    else:
        print "Why would you do that?"
        print "Start from the lift again."
        lift()

def office_room():
    print "\nOPEN SPACE OFFICE"
    print "Never before did you see so many desks and computers in one room."
    print "The murderer could be anywhere in here..."
    print "Do you want to take to time to search the whole office or go to another floor?"
    choice = raw_input("\f'search' or 'lift' \n>> ")
    if choice == "search":
        print "You want to do a good work and start to search the room."
        print "At some point it seems like a waste of time."
        print "The murderer could be anywhere by now."
        print "Do you continue searching or go somewhere else?"
        choice = raw_input("\f'continue' or 'lift' \n>> ")
        if choice == "continue":
            print "When you are half done with your room you hear sirens coming near."
            print "Finally help arrived and your patience pays off."
            print "You are a good agent, %s. Great job!" % name
            print "Do you want to keep looking or meet your team?"
            choice = raw_input("'continue' or 'team' \n>> ")
            if choice == "continue":
                print "You better go upstairs then."
                lift()
            elif choice == "team":
                print "You are relieved to speak to others."
                print "Your operation is over."
            else:
                print "Sorry %s, go back into the lift." % name
                lift()
        elif choice == "lift":
            lift()
        else:
            print "What are you doing? Better choose another floor."
            lift()

    elif choice == "lift":
        lift()
    else:
        print "Type something else."
        choice = raw_input("\f'search' or 'lift' \n>> ")
        if choice == "search":
            print "You want to do a good work and start to search the room."
            print "At some point it seems like a waste of time."
            print "The murderer could be anywhere by now."
            print "Do you continue searching or go somewhere else?"
            choice = raw_input("\f'continue' or 'lift' \n>> ")
            if choice == "continue":
                print "When you are half done with your room you hear sirens coming near."
                print "Finally help arrived and your patience pays off."
                print "You are a good agent, %s. Great job!" % name
                print "Do you want to keep looking or meet your team?"
                choice = raw_input("'continue' or 'team' >> ")
                if choice == "continue":
                    print "You better go upstairs then."
                    lift()
                elif choice == "team":
                    print "You are releived to speak to others."
                    print "Your operation is over."

        elif choice == "lift":
            lift()
        else:
            print "Sorry agent %s, but you didn't choose a reasonable option... You have to go back downstairs." % name
            foyer_room()


def bathroom():
    print "\nBATHROOM"
    print "What a stereotyped hiding place."
    print "Do you want to examine the toilet cabines or go somewhere else?"
    choice = raw_input("\f'examine' or 'lift' \n>> ")
    if choice == "examine":
        print "As soon as you enter you sense a noice..."
        print "Some kind of whistle."
        print "You run towards the cabine where the noise comes from."
        print "A little cute bird hops through the gap between door and floor."
        print "You go back into the lift - everything looks clear in here."
        lift()
    elif choice == "lift":
        lift()
    else:
        print "Ups, there must have been a typo. Try again."
        choice = raw_input("\f'examine' or 'lift' \n>> ")
        if choice == "examine":
            print "As soon as you enter you sense a noice..."
            print "Some kind of whistle."
            print "You run towards the cabine where the noise comes from."
            print "A little cute bird hops through the gap between door and floor."
            print "You go back into the lift - everything looks clear in here."
            lift()
        elif choice == "lift":
            lift()
        else:
            print "What shall we do with you? Can you read? Go back home and get some sleep."
            print "\fDo you want to try again %s?" % name
            choice = raw_input(">> ")
            if choice == "yes":
                start()
            elif choice == "no":
                exit()
            else:
                print "It's a simple question that can only answered with 'yes' or 'no'."
                choice = raw_input(">> ")
                if choice == "yes":
                    start()
                elif choice == "no":
                    exit()

def garden():
    print "\nROOF TOP GARDEN"
    print "From up here one's got an amazing view over town."
    print "Do you want to take a few seconds to admire the view?"
    print "Or better go look for the bad guy up here?"
    print "You can also go back into the lift."
    choice = raw_input("\f'view', 'search' or 'lift' \n>> ")
    if choice == "view":
        print "That was definitly worth a look."
        print "Now go look for the murderer."
        choice = raw_input("\f'search' or 'lift' \n>> ")
        if choice == "search":
            print "Without any warning you find the dead corpus behind some bushes."
            print "That means the murderer was definitely here. Unfortunately no other traces can be found."
            print "Go back downstairs, there is nothing else to do up here."
            lift()

        elif choice == "lift":
            lift()
        else:
            print "\fBe a good police officer and make a sensible decision."
            choice = raw_input("'search' or 'lift' \n>> ")
            if choice == "search":
                print "Without any warning you find the dead corpus behind some bushes."
                print "That means the murderer was definitely here. Unfortunately no other traces can be found."
                print "Go back downstairs, there is nothing else to do up here."
                lift()

            elif choice == "lift":
                lift()
            else:
                print "Just get into the lift."
                lift()

    elif choice == "search":
        print "Without any warning you find the dead corpus behind some bushes."
        print "That means the murderer was definitely here. Unfortunately no other traces can be found."
        print "Go back downstairs, there is nothing else to do up here."
        lift()
    elif choice == "lift":
        lift()
    else:
        print "\fWhat was it you wanted to do next?"
        choice = raw_input("'view', 'search' or 'lift' \n>> ")
        if choice == "view":
            print "That was definitly worth a look."
            print "Now go look for the murderer."
            choice = raw_input("\f'search' or 'lift' \n>> ")
            if choice == "search":
                print "Without any warning you find the dead corpus behind some bushes."
                print "That means the murderer was definitely here. Unfortunately no other traces can be found."
                print "Go back downstairs, there is nothing else to do up here."
                lift()

            elif choice == "lift":
                lift()
            else:
                print "Be a good police officer and make a sensible decision."
                choice = raw_input("\f'search' or 'lift' \n>> ")
                if choice == "search":
                    print "Without any warning you find the dead corpus behind some bushes."
                    print "That means the murderer was definitely here. Unfortunately no other traces can be found."
                    print "Go back downstairs, there is nothing else to do up here."
                    lift()

                elif choice == "lift":
                    lift()
                else:
                    print "Just get into the lift."
                    lift()

        elif choice == "search":
            print "Without any warning you find the dead corpus behind some bushes."
            print "That means the murderer was definitely here. Unfortunately no other traces can be found."
            print "Go back downstairs, there is nothing else to do up here."
            lift()
        elif choice == "lift":
            lift()
        else:
            print "You are done agent %s. You weren't able to make quick rational decicions." % name
            print "\fDo you want to try again %s?" % name
            choice = raw_input(">> ")
            if choice == "yes":
                start()
            elif choice == "no":
                exit()
            else:
                print "It's a simple question that can only answered with 'yes' or 'no'."
                choice = raw_input(">> ")
                if choice == "yes":
                    start()
                elif choice == "no":
                    exit()

def lift():
    print "LIFT"
    print """
    ROOF TOP GARDEN - 4
    BATHROOM - 3
    OFFICE - 2
    CAFETERIA - 1
    FOYER - G
    CAR PARK - 0
    """
    print "Where do you want to go?"
    choice = raw_input(">> ")

    if choice == "0":
        car_park()
    elif choice == "G":
        foyer_room()
    elif choice == "1":
        cafeteria()
    elif choice == "2":
        office_room()
    elif choice == "3":
        bathroom()
    elif choice == "4":
        garden()
    else:
        print "Seriously %s?! As a agent you should be able to press any button." % name
        choice = raw_input(">> ")

        if choice == "0":
            car_park()
        elif choice == "G":
            foyer_room()
        elif choice == "1":
            cafeteria()
        elif choice == "2":
            office_room()
        elif choice == "3":
            bathroom()
        elif choice == "4":
            garden()
        else:
            print "Are you drunk? Go home and let somebody else do the work."
            print "\fDo you want to try again %s?" % name
            choice = raw_input(">> ")
            if choice == "yes":
                start()
            elif choice == "no":
                exit()
            else:
                print "It's a simple question that can only answered with 'yes' or 'no'."
                choice = raw_input(">> ")
                if choice == "yes":
                    start()
                elif choice == "no":
                    exit()


def start():
    foyer_room()

start()
