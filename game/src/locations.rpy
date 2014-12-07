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
    mars.add_clue("heading to a world named after a god of war")
    mars.add_clue("a terrestial planet with 2 moons")
    mars.add_clue("going to the planet that Phobos orbited")
    mars.add_clue("going to the planet that Deimos orbited")
    mars.add_clue("going to a world that had an orbital period of 686.98 Earth Days")
    mars.add_clue("visitng a world first discovered by the Egyptians in the 2nd millennium BC")
    mars.add_clue("heading to the red planet. Red! Red! Red!")
    mars.add_clue("heading to the tallest mountain in the solar system")
    mars.add_clue("the planet with the largest dust storms")
    locations.append(mars)


    jupiter = Location('Jupiter')
    jupiter.add_clue("going to a world with 67 moons")
    jupiter.add_clue("hoping to vist the largest planet in the solar system")
    jupiter.add_clue("going to a planet that Io orbits")
    jupiter.add_clue("planning on stopping by Europa along the way")
    jupiter.add_clue("heading to a planet that orbits the Sun once every 11.8 Earth years")
    jupiter.add_clue("hoping to visit a storm that has been raging for 350 years")
    jupiter.add_clue("visiting the sector with the largest moon in the solar system")
    locations.append(jupiter)

    saturn = Location('Saturn')
    saturn.add_clue("hoping see Titan on the way to their destination")
    saturn.add_clue("heading to a planet first recorded in the 8th century BC by the Assyrians")
    saturn.add_clue("visiting a planet with more than 30 rings")
    saturn.add_clue("going to the flattest planet")
    saturn.add_clue("heading to a world that orbits the Sun once every 29.4 years")
    saturn.add_clue("was named after the Greek god Cronus")
    locations.append(saturn)


    uranus = Location('Uranus')
    uranus.add_clue("heading to a planet with 13 known rings")
    uranus.add_clue("visiting a planet that was discovered by William Herschel")
    uranus.add_clue("going to a world that was discovered March 13, 1781")
    uranus.add_clue("scurrying off to a world with a surface temperature of -197 C")
    uranus.add_clue("visiting the sector with the moon Oberon")
    uranus.add_clue("visiting the sector with the moon Titania")
    uranus.add_clue("visiting the sector with the moon Ariel")
    uranus.add_clue("planning to visit a world with an orbital period of 84.02 Earth years")
    locations.append(uranus)

    neptune = Location('Neptune')
    neptune.add_clue("visiting a world discovered by Urbain Le Verrier and Johann Galle")
    neptune.add_clue("heading to a world that was discovered September 23, 1846")
    neptune.add_clue("checking out a world with an orbital period of 164.8 Earth Years")
    neptune.add_clue("swinging by the smallest of the ice giants")
    neptune.add_clue("visiting a planet that takes only 18 hours to make one rotation")
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
        menu.append(("Destination, Inquistor?", None))
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
