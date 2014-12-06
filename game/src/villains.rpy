init python:
    import random
    import copy
    #begin basic data
    villains = []
    villains.append(Villain('Han Solo','A smuggler with a heart of gold','Male','Brown','Brown'))
    villains.append(Villain('Luke Skywalker','A whiny Jedi','Male','Blond','Blue'))
    villains.append(Villain('Leia Organa','A princess','Female','Brown','Brown'))
    villains.append(Villain('Mara Jade','The Hand of the Emperor','Female','Red','Green'))
    villains.append(Villain('Wedge Antilles','That dude who flew in all the battles','Male','Brown','Green'))
    villains.append(Villain('Biggs Darklighter','Never made it past the first movie.','Male','Black','Brown'))

    def newVillain():
        return villains[randrange(len(villains))]

    villain = Villain()
