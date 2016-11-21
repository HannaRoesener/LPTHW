# this is the original skeletion I imagined after a few trails. However, when I filled it with life it wouldn't work, so I used another structure.
# Hopefully this one was not closer to work than the one I decided to work on further! :)
# inspired by ex43 from LPTHW
class Scene(object):
    def enter(self):
        pass

    def start(self):
        print "Before we start, please choose a name for your character."
        name = raw_input(">> ")
        print "Welcome %s." % name
        self.Map()

class Mars(object):
    def enter(self):

        scenes = {
            'forest': Forest(),
            'lake': Lake(),
            'map': Map(),
            'rocket': Rocket(),
            'mountains': Mountains(),
            'swampland': Swampland(),
            'start': Scene()
            }


class Forest(Scene):
    pass

class Rocket(Scene):
    pass

class Lake(Scene):
    pass

class Swampland(Scene):
    pass

class Mountains(Scene):
    pass

class Map(Scene):
    pass

class Player(object):
    def __init__(self, lifes):
        self.lifes = 3





game = Scene()
game.start()
