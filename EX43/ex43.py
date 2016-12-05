from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


        # ne sure tp print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mum would be proud..if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet #25 have invaded your ship and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod."
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costumes flowing around his hate filled body. He's blocking the door to the Armory and about to pull a weapon to blast you."

        action = raw_input("> ")

        if action == "shoot!":
            print "Quick on the drae you yank out your blaster anf fire it at the Gothon. His clown costume is flowing and moving around his body, which throws off your aim. Your laser hits his costume but misses him entirly. This makes him fly into an insane rage and blast you repeadedly in the face until you are dead. Then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cracks a laser past your head. In the middle of your artful dodge your foor slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and eats you."
            return 'death'

        elif action == "tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know: \nLbhe zbgure vf fb sbg, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur. \n The Gothon stops, tries not to laugh, then busts out laughing and can't stop. While he's laughing you run up and shoot him square in the head putting him down, then jump through the Weapon Armory door."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "A lot of things happen in here. Blablabla."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "BZZZZZEED!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "Go to the bridge."
            return 'the_bridge'
        else:
            print "Ups. Ypu die."
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "You have a bomb under your arm and haven't pulled your weapon yet as more Gorthons emerge."

        action = raw_input("> ")

        if action == "throw the bomb":
            print "You die."
            return 'death'

        elif action == "slowly place the bomb":
            print "You run to the escape podto get off this tin can."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print "There's 5 pods, which one do you take?"
        good_pot = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You die."
            return 'death'
        else:
            print "You won!"
            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job!"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
