
define e = Character('Computer', color="#c8ffc8")
define agent_x = Character('Agent X', color="#c8ffc8")
define agent_y = Character('Agent Y', color="#c8ffc8")

# The game starts here.
label start:
    $ warrent = None
    $ no_of_matches = 0
    $ villain = newVillain()
    show black
    e "A thing has been stollen!"

label location:
    $ location = next_location()
    $ x_clue = location.get_rand_clue()
    $ y_clue = location.get_rand_clue()
    $ x_trait = get_character_clue()
    $ y_trait = get_character_clue()

    jump location_actions

label location_actions:
    menu:
        e "What would you like to do?"
        "Question Agent X":
            $ active_agent = agent_x
            jump question_agent
        # "Question Agent Y":
        #     $ active_agent = agent_y
        #     jump question_agent
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
        if no_of_matches is not 1:
            e "You are hot on the trail! Seems like the rebel scum has been here recently."
            jump location
        else:
            jump trial_and_capture
    else:
        e "Doesn't seem to be any criminal activity around here. Perhaps you should review with your staff again."
        jump location_actions

label trial_and_capture:
    e "Our scanner indicates that the rebel criminal, [warrent], is in the area."
    e "Agents mobilizing for the capture of [warrent]."
    e "[warrent] captured. Taking to the facility for processing."

    if warrent == villain.name:
        e "Congratulations, you have successfully apprehended the right person."
    else:
        e "Unfortunately, it would seem [warrent] had nothing to do with the capture of the thing.  Way to mess up."

    return

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
    active_agent "Local rumor states the rebel said [villain.pronoun] was going to [clue]."
    jump question_agent

label describe_suspect:
    if active_agent == agent_x:
        $ clue = x_trait
    else:
        $ clue = y_trait
    active_agent "Local rumor states [villain.pronoun] had [clue]."
    jump question_agent

label dismiss_agent:
    active_agent "Yes, sir!"
    jump location_actions

label record_evidence:
    $ evidence = evidence_recorder(evidence)
    $ matches = calculate_match(evidence)
    $ no_of_matches = len(matches)
    $ warrent = matches[0].name
    if no_of_matches == 1:
        e "Warrent issued. All agents keep an eye out for [warrent]."
    jump location_actions


label game_over:
    e "Unfortunately, you're all out of fuel. Game over!"
    return
