image bg standard = "images/background.png"

image ig_bot normal = "images/ig-bot.png"
image computer normal = "images/screen.png"

define ig_bot = Character('IG-BOT', color="#c8ffc8")


define agent_x = Character('Agent X', color="#c8ffc8")
define agent_y = Character('Agent Y', color="#c8ffc8")

# The game starts here.
label start:
    $ warrent = None
    $ no_of_matches = 0
    $ villain = newVillain()
    scene bg standard
    show ig_bot normal
    show computer normal
    with dissolve

    $ player_location = next_location(None)

    ig_bot "Greetings, Inquisitor."
    ig_bot "I am IG-BOT 1148.  I have been assigned to you by the Admiral to help aid you with tracking down rebel agents."
    ig_bot "My job is to help you coordinate with Imperial Agents on the field, and provide you with access to my state of the art criminal database."
    ig_bot "By imputing search parameters based on the description of the rebel scum, I shall be able to accurately provide you with a warrant for arrest."
    ig_bot "I do encourage you to attempt to solve this efficiently, and without the bumbling idiocy common to organics."
    ig_bot "Not only does the Admiral dislike failures, but we have limited resources when it comes to chasing criminals across the solar system."
    ig_bot "Budget cutbacks. Blame the Imperial Senate."
    ig_bot "According to the dossier the Admiral has forwarded to me, we shall first begin investigating [player_location.name], where the top secret plans were stollen."

label location:
    $ location = next_location(player_location)
    $ x_clue = location.get_rand_clue()
    $ y_clue = location.get_rand_clue()
    $ x_trait = get_character_clue()
    $ y_trait = get_character_clue()

    jump location_actions

label location_actions:
    show ig_bot normal
    menu:
        ig_bot "What are your orders, Inquisitor?"
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
        ig_bot "Ok, let's gather more evidence."
        jump location_actions

    ig_bot "Traveling to [destination]"

    $ player_location = get_location_by_name(destination)
    $ fuel = fuel - fuel_difficulty
    ig_bot "You have arrived at [player_location.name]."
    $ fuel_p = get_fuel_percentage()
    ig_bot "Fuel levels are currently at [fuel_p] percent"

    if fuel_p == 0:
        jump game_over

    if location.name == player_location.name:
        if no_of_matches is not 1:
            ig_bot "You are hot on the trail! Seems like the rebel scum has been here recently."
            jump location
        else:
            jump trial_and_capture
    else:
        ig_bot "Doesn't seem to be any criminal activity around here. Perhaps you should review with your staff again."
        jump location_actions

label trial_and_capture:
    show ig_bot normal
    ig_bot "Our scanner indicates that the rebel criminal, [warrent], is in the area."
    ig_bot "Agents mobilizing for the capture of [warrent]."
    ig_bot "[warrent] captured. Taking to the facility for processing."

    if warrent == villain.name:
        ig_bot "Congratulations, you have successfully apprehended the right person."
    else:
        ig_bot "Unfortunately, it would seem [warrent] had nothing to do with the capture of the thing.  Way to mess up."

    return

label question_agent:
    hide ig_bot normal
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
    ig_bot "Initializing Imperial Criminal Database..."
    hide ig_bot normal
    $ evidence = evidence_recorder(evidence)
    $ matches = calculate_match(evidence)
    $ no_of_matches = len(matches)
    $ warrent = matches[0].name
    show ig_bot normal
    if no_of_matches == 1:
        ig_bot "Warrent issued. All agents keep an eye out for [warrent]."
    jump location_actions


label game_over:
    ig_bot "Unfortunately, you're all out of fuel. Game over!"
    return
