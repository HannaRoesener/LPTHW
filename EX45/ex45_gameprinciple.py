# so this is a trial version, that is suppossed to test if the construct is actually running. It is not. So I'll just write down the game how I imagined it and leave you to the grading! :)

class Scenes(object):
    def __init__(self):
        print """
        Mars Map
        """
        print "Where do you want to go?"

        userinput = raw_input(">> ")
        while userinput != "exit":
            if "forest" or "Forest" in userinput:
                self.mars = Forest()
            else:
                print "This is unknown territory. You got eaten by Aliens."
                print "Do you want to try again?"
                choice = raw_input(">> ")
                if "yes" or "Yes" in choice:
                    self.mars = Scenes()
                elif "no" or "No" in choice:
                    print "Next time better stick to the map. Hope to see you soon. Humanity needs you! Goodbye."
                else:
                    print "Sorry, an astronaut should be able to type! Goodybe."



class Mars(object):
    def __init__(self):
        pass

    def start(self):
        print "Hi there, this is so exciting! You are astronaut on its way to Mars. Your rocket will land shortly. Do not loosen your seatbelt!" # more info about mission
        # name??
        self.mars = Scenes()


    def collection(self, items):
        self.item = items
        self.collection = ["seams"]

    def addItem(self, thing):
        self.thing = thing
        print "This is your collection so far:"
        print self.collection
        self.collection.append("thing")
        print "Hurray, you've got more things in your collection. This is what you've got:"
        self.collection = collection
        print self.collection 

class Forest(Mars):
    def response(self):
        print "Nice inside Forest."
        if seams in self.collection:
            print "You grow a tree and go back to scenes."
            self.mars = Scenes()
        else:
            print "You collect some sticks."
            self.collection.append("sticks")
            print self.collection

mars = [Forest()]
app = Mars()
app.start()
