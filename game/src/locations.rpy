init python:
    import random
    import copy

    locations = []
    location = Location()
    player_location = Location()

    mercury = Location('Mercury')
    mercury.add_clue('the closest planet to the sun')
    mercury.add_clue("a place named after the Messenger to the gods")
    locations.append(mercury)

    venus = Location('Venus')
    venus.add_clue("the sister of Earth")
    venus.add_clue("beautiful world filled with carbon dioxide with a small amount of nitrogen")
    locations.append(venus)


    earth = Location('Earth')
    earth.add_clue("the twin of Venus")
    earth.add_clue("a world where a no spacesuit would be required")
    locations.append(earth)

    mars = Location('Mars')
    mars.add_clue("a monument to the god of war")
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

        menu.append(("Collect More Evidence","Back"))
        return renpy.display_menu(menu)

    def get_location_by_name(loc):
        for l in locations:
            if l.name == loc:
                return l
