# version with engine -> like in ex 43:)
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening


class Scenes(object):
    def start(self, mars_scene):
        self.mars = mars_scene
        print "Wuuhu this is exciting! Your rocket will shortly land."
        print "Before, quickly choose a name for your astronaut!"
        name = raw_input(">> ")
        print "Welcome %s." % name
        self.mars = Scenes.response()


    def response(self):
        print """
        ___________________________________
            Forest              Swampland
            YYYYYY               +++++
                     NASA Base X
            /\/\/\/\               ~~~~~~
            Mountains               Lake
        ___________________________________
        """
        print "This is the map NASA gave you. It is all you can use for orientation."

        print "Where do you want to go?"
        position = raw_input(">> ")
        while position != "exit":
            if "forest" or "Forest" in position:
                self.mars = Forest.response()
            elif "swampland" or "Swampland" in position:
                self.mars = Swampland.response()
            elif "Mountains" or "mountains" or "Mountain" or "mountain" in position:
                self.mars = Mountains.response()
            elif "lake" or "Lake" in position:
                self.mars = Lake.response()
            elif "NASA Base" or "nasa base" or "NASA base" or "Nasa Base" or "nasa Base" in position:
                self.mars = Rocket.response()
            else:
                print "This is unknown territory. Aliens came to eat you."
                print "Do you want to try again?"
                userinput = raw_input(">> ")
                if "yes" or "Yes" in userinput:
                    self.mars = Scenes.response()
                elif "no" or "No" in userinput:
                    print "Next time you should stick to the map. Goodbye!"
                else:
                    print "Sorry, an austronaut should be able to type!"


class Mars(object):
    pass



class Rocket(Mars):
    def response(self):
        print "Your rocket became your home."
        print "There is stuff all over the place."
        print "What do you want to do?"
        print "Have a nap? Tidy up? Or go explore?"

        action = raw_input(">> ")

        if "nap" or "sleep" in action:
            print "You close the door and sleep for a while. You wake up and leave the rocket."
            self.mars = Scenes()
        elif "tidy" or "Tidy" in action:
            print "You actually find lots of useful things while tidying up."
            print "Do you want to keep any of the following?"
            Ritems = ["cell phone", "seams", "blanket", "cup", "bottle"]
            print Ritems
            userinput = raw_input(">> ")
            if "yes" in userinput:
                print "Which ones do you want to pick up?"
                Items = raw_input(">> ")
                return addItem(collection)
            elif "no" in userinput:
                self.mars = Scenes()
            else:
                self.mars = Scenes()

class Lake(Mars):
    def response(self):
        print "What do you want to do %s.?" % name
        print "Drink some water, fill some up or make a call?"
        choice = raw_input(">> ")
        if "drink" or "Drink" in choice:
            return DrinkWater()
        elif "conserve" in choice:
            return takeWater()
        elif "call" in choice:
            return call()
        else:
            "What?? Who would do that at a lake??"
            self.mars = Lake()

    def drinkWater():
        if "cup" in collection:
            print "You can try and drink some water."
            print "Are you thirsty?"
            drink = raw_input(">> ")
            if "yes" in drink:
                print "The water is not made for a human body."
            elif "no" in drink:
                "Good decision, you never know if it is poisonous."
            else:
                self.mars = Lake()

        else:
            print "Sorry you did not bring a cup."
            print "But your system needs fluid urgently."

    def call():
        if "cell phone" in collection:
            print "You get out your phone, but the reception is really bad."
            print "Also the battery is running low, better keep it for an emergency."
            self.mars = Lake()

        else:
            "You do not have any super power, or have you ever managed to call someone without a phone?"
            self.mars = Lake()

    def takeWater():
        if "bottle" in collection:
            print "You use the bottle to conserve some water."
            self.item = addItem(water)
            print "Very clever of you, %d." % name
            self.mars = Lake()

    def Map():
        self.mars = Scenes()

class Forest(Mars):
    def response(self):
        print "It is nice inside the woods, although the trees look a bit funny."
        print "But then, you are not on earth."
        print "Have a look inside your pockets, to see what you can do here."
        if "seams" in collection:
            print "Do you want to try grow something?"
            choice = raw_input(">> ")
            if "yes" or "Yes" in choice:
                if "water" in collection:
                    print "Hurray, your managed to grow something edible on Mars."
                    print "You earn a life."
                else:
                    print "Your little plant dies, since you cannot water it."
            elif "no" or "No" in choice:
                self.mars = Scenes()
        else:
            print "The forest starts to become a bit scary. You hear strange voices. Maybe there are aliens around??"
            print "You run back to your rocket."
            self.mars = Scenes()

class Swampland(Mars):
    def response(self):
        print "How did you think you were gonna land on this ground??"
        print "Use your brain occasionally!"
        self.mars = Scenes()

class Mountains(Mars):
    def response(self):
        print "The weather is actually pretty good here."
        print "You love hiking and are tempted to go for a walk."
        print "Or should you better watch your rocket?"

        choice = raw_input(">> ")

        if "watch" or "Watch" or "rocket" or "Rocket" in choice:
            print "That might be better. You could come here another time."
        elif "hiking" or "Hiking" or "walk" or "Walk" in choice:
            print "You reach the top of the highest mountain."
            if "cell phone" in collection:
                print "And try to call home."
                print "From up here you receive some reception."
                print "Well done you!"
            else:
                print "The view is amazing. Next time you should try to bring the cell up here."
                self.mars = Scenes()

mars = [Lake(), Rocket(), Mountains(), Swampland(), Forest(), Scenes()]
app = Scenes()
app.start(mars_scene)
