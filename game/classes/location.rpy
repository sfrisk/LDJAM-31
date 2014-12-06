init python:
    from random import randrange

    class Location(object):
        def __init__(self,name=''):
            self.name = name
            self.clues = []

        def add_clue(self,clue):
            self.clues.append(clue)

        def get_rand_clue(self):
            return self.clues[randrange(len(self.clues))]
