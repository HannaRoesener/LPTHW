class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


def first():
    print """
    Happy birthday to you,
    I don't want to get sued,
    So I'll stop right there
    """

happy_bday = first([""])



bulls_on_parade = Song(["They rally around tha family",
"With pocktes full of shells"])



first.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
