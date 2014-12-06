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
    $ fuel = fuel - fuel_difficulty
    e "You have arrived at [player_location.name]."
    $ fuel_p = get_fuel_percentage()
    e "Fuel levels are currently at [fuel_p] percent"

    if fuel_p == 0:
        jump game_over

    if location.name == player_location.name:
        e "You are hot on the trail! Seems like the fugitive has been here recently."
        jump location
    else:
        e "Doesn't seem to be any criminal activity around here. Perhaps you should review the clues again."
        jump location_actions



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


label game_over:
    e "Unfortunately, you're all out of fuel. Game over!"
    return
