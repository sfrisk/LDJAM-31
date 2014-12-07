init python:
    import random
    import copy

    locations = []
    location = Location()
    player_location = Location()

    mercury = Location('Mercury')
    mercury.add_clue('hoping to get a lot closer to the sun')
    mercury.add_clue("going to a planet named after an ancient Messenger to the Gods")
    mercury.add_clue("going somewhere where the year lasts only 88 days")
    mercury.add_clue("going to the second densest planet in the system")
    mercury.add_clue("going to the second hottest planet in our glorious empire")
    mercury.add_clue("in the process of buying some extreme weather gear. Surface temperatures at their destination ranges from -173 to 427 Celcius")
    locations.append(mercury)

    venus = Location('Venus')
    venus.add_clue("hoping to visit the sister of Earth")
    venus.add_clue("going to a terestial planet that rotates counter-clockwise")
    venus.add_clue("the second brightest object in the sky after the Moon")
    venus.add_clue("going to the second largest terrestrial planet in our glorious empire")
    venus.add_clue("going to a planet named after the Roman goddess of love and beauty")
    venus.add_clue("world filled with carbon dioxide with a small amount of nitrogen")
    venus.add_clue("going to the hottest planet in our solar system")
    locations.append(venus)


    earth = Location('Earth')
    earth.add_clue("interested in seeing the twin of Venus")
    earth.add_clue("heading to a planet not named after a god")
    earth.add_clue("prepping for a trip to the largest terrestrial planet")
    earth.add_clue("heading to a world where a no spacesuit would be required")
    earth.add_clue("interested in spending some time about 1 AU away from the sun")
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


    def next_location(loc):
        locations_copy = copy.deepcopy(locations)

        if loc != None:
            for l in locations_copy:
                if l.name == loc.name:
                    locations_copy.remove(l)

        return locations_copy[randrange(len(locations_copy))]

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
