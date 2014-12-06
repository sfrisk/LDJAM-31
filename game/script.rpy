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
    player_location = Location()
    clue = ''

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

define e = Character('Computer', color="#c8ffc8")

define agent_x = Character('Agent X', color="#c8ffc8")
define agent_y = Character('Agent Y', color="#c8ffc8")

# The game starts here.
label start:

    $ villain = newVillain()
    show black
    e "[villain.name], [villain.pronoun] has escaped!"

label location:
    $ location = next_location()

    $ x_clue = location.get_rand_clue()
    $ y_clue = location.get_rand_clue()
    jump location_actions


label good_location:
    e "You have arrived at [player_location.name]."
    e "You are hot on the trail! Seems like the fugitive has been here recently."
    jump location


label bad_location:
    e "You have arrived at [player_location.name]."
    e "Doesn't seem to be any criminal activity around here."
    jump leave_location

label location_actions:
    menu:
        e "What would you like to do?"
        "Question Agent X":
            $ active_agent = agent_x
            jump question_agent
        "Question Agent Y":
            $ active_agent = agent_y
            jump question_agent
        "Record Evidence":
            jump record_evidence
        "Travel":
            jump leave_location

label leave_location:
    $ destination = location_menu(location)

    if destination == 'Back':
        e "Ok, let's gather more evidence."
        jump location_actions

    e "Traveling to [destination]"

    $ player_location = get_location_by_name(destination)

    if location.name == player_location.name:
        jump good_location
    else:
        jump bad_location


label question_agent:
    active_agent "What would you like to know, boss?"
    menu:
        "Where did the suspect go?":
            jump where_suspect
        "Tell me about the suspect":
            jump describe_suspect
        "Very good agent. You're dismissed.":
            jump dismiss_agent

label where_suspect:
    if active_agent == agent_x:
        $ clue = x_clue
    else:
        $ clue = y_clue
    active_agent "Local rumor states [villain.pronoun] said he was going to [clue]"
    jump question_agent

label describe_suspect:
    active_agent "Traits aren't supported yet. TODO"
    jump question_agent

label dismiss_agent:
    active_agent "Yes, sir!"
    jump location_actions

label record_evidence:
    e "Recording evidence isn't currently supported"
    jump location_actions
