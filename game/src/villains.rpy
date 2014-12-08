init python:
    import random
    import copy
    #begin basic data
    villains = []
    # villains.append(Villain('Han Solo','A smuggler with a heart of gold','Male','Brown','Brown'))
    # villains.append(Villain('Luke Skywalker','A whiny Jedi','Male','Blond','Blue'))
    # villains.append(Villain('Leia Organa','A princess','Female','Brown','Brown'))
    # villains.append(Villain('Mara Jade','The Hand of the Emperor','Female','Red','Green'))
    # villains.append(Villain('Wedge Antilles','That dude who flew in all the battles','Male','Brown','Green'))
    # villains.append(Villain('Biggs Darklighter','Never made it past the first movie.','Male','Black','Brown'))

    villains.append(Villain('Monty Madigan', '', 'Male', 'Brown', 'Brown', 'Fair'))
    villains.append(Villain('Linwood Sabine', '', 'Male', 'Brown', 'Brown', 'Dark'))
    villains.append(Villain('Domenic Carthen', '', 'Male', 'Red', 'Green', 'Dark'))
    villains.append(Villain('Darron Callahan', '', 'Male', 'Black', 'Brown', 'Fair'))
    villains.append(Villain('Lucius Konicek', '', 'Male', 'Blond', 'Brown', 'Fair'))
    villains.append(Villain('Avery Belmont', '', 'Male', 'Black', 'Blue', 'Fair'))
    villains.append(Villain('Hunter Diseth', '', 'Male', 'Red', 'Blue', 'Dark'))
    villains.append(Villain('Cole Quintan', '', 'Male', 'Blond', 'Green', 'Dark'))
    villains.append(Villain('Maxwell Paulsen', '', 'Male', 'Brown', 'Green', 'Fair'))

    villains.append(Villain('Catheryn Kniffin', '', 'Female', 'Brown', 'Green', 'Fair'))
    villains.append(Villain('Robena Erikson', '', 'Female', 'Brown', 'Green', 'Dark'))
    villains.append(Villain('Lynna Dilucca', '', 'Female', 'Black', 'Brown', 'Dark'))
    villains.append(Villain('Cherlyn Tameron', '', 'Female', 'Red', 'Green', 'Dark'))
    villains.append(Villain('Tenesha Thoran', '', 'Female', 'Black', 'Brown', 'Fair'))
    villains.append(Villain('Catheryn Jann', '', 'Female', 'Red', 'Blue', 'Fair'))
    villains.append(Villain('Cyrstal Byrn', '', 'Female', 'Blond', 'Green', 'Fair'))
    villains.append(Villain('Porsche Tameron', '', 'Female', 'Blond', 'Blue', 'Fair'))


    def newVillain():
        return villains[randrange(len(villains))]

    def getGenderByName(name):
        for v in villains:
            if v.name is name:
                return v.gender
        return None


    villain = Villain()
