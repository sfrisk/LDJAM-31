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

    locations = []
    location = Location()
    old_location = Location()

    mercury = Location('Mercury')
    mercury.add_clue('I heard they were going to the closest planet to the sun')
    mercury.add_clue("They're going to a place named after the Messenger to the gods")
    locations.append(mercury)

    venus = Location('Venus')
    venus.add_clue("They're going to the sister of Earth")
    venus.add_clue("It may be beautiful where they're going, but be careful not to breath the air! It's mostly carbon dioxide with a small amount of nitrogen")
    locations.append(venus)


    earth = Location('Earth')
    earth.add_clue("The twin of Venus")
    earth.add_clue("I won't be needing a space suit where I'm going!")
    locations.append(earth)

    mars = Location('Mars')
    mars.add_clue("War! All the War!")
    mars.add_clue("Mars Clue 2")
    locations.append(mars)


    jupiter = Location('Jupiter')
    jupiter.add_clue("Jupiter Clue 1")
    jupiter.add_clue("Jupiter Clue 2")
    locations.append(jupiter)

    saturn = Location('Saturn')
    saturn.add_clue("Saturn Clue 1")
    saturn.add_clue("Saturn Clue 2")
    locations.append(saturn)


    uranus = Location('Uranus')
    uranus.add_clue("Uranus Clue 1")
    uranus.add_clue("Uranus Clue 2")
    locations.append(uranus)

    neptune = Location('Neptune')
    neptune.add_clue("Neptune Clue 1")
    neptune.add_clue("Neptune Clue 2")
    locations.append(neptune)


    def next_location():
        return locations[randrange(len(locations))]

    def location_menu(loc):
        locations_copy = copy.deepcopy(locations)
        for l in locations_copy:
            if l.name == loc.name:
                locations_copy.remove(l)

        choices = random.sample(locations_copy, 3)


        choices.append(loc)
        choices =  random.sample(choices,4)
        menu = []
        menu.append(("Where should we go?", None))
        for c in choices:
            if c.name == loc.name:
                menu.append((c.name, c.name))
            else:
                menu.append((c.name, c.name))
        return renpy.display_menu(menu)

    def get_location_by_name(loc):
        for l in locations:
            if l.name == loc:
                return l

define e = Character('Eileen', color="#c8ffc8")

# The game starts here.
label start:

    $ villain = newVillain()
    $ location = next_location()
    show black
    e "[villain.name], [villain.pronoun] has escaped!"
    e "[villain.bio]"
    e "But we have a clue!"
    $ clue = location.get_rand_clue()
    "[clue]"

    $ destination = location_menu(location)

    "Traveling to [destination]"

    $ old_location = copy.deepcopy(location)
    $ location = get_location_by_name(destination)

    if location.name == old_location.name:
        jump good_location
    else:
        jump bad_location

    return
label good_location:
    e "You have arrived at [location.name]."
    e "You picked right!"
    pause
    return

label bad_location:
    e "You have arrived at [location.name]."
    e "You picked wrong!"
    pause
    return
