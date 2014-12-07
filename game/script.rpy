image bg standard = "images/background.png"
image bg input_background = "images/background-1.png"
image bg field = "images/background-2.png"
image bg mercury = "images/mercury.png"
image bg mars = "images/mars.png"
image bg neptune = "images/neptune.png"
image bg uranus = "images/uranus.png"

image splash = "images/splash.png"

image ig_bot normal = "images/ig-bot.png"
image ig_bot unhappy = "images/ig-bot-unhappy.png"
image agent normal = "images/agent_x.png"
image computer normal = "images/screen.png"

define ig_bot = Character('IG-BOT', color="#527018")


define agent_x = Character('Agent X', color="#72110b")
define agent_y = Character('Agent Y', color="#72110b")
image splash = "splash.png"

# The game starts here.
label start:
    #play music "audio/background.mp3"
    $ warrent = None
    $ no_of_matches = 0
    $ villain = newVillain()
    scene bg standard
    show ig_bot normal
    show computer normal

    $ player_location = next_location(None)

    ig_bot "Greetings, Inquisitor."
    ig_bot "I am IG-BOT 1148.  I have been assigned to you by the Admiral to help aid you with tracking down rebel agents."
    ig_bot "My job is to help you coordinate with Imperial Agents on the field, and provide you with access to my state of the art criminal database."
    ig_bot "By imputing search parameters based on the description of the rebel scum, I shall be able to accurately provide you with a warrant for arrest."
    hide ig_bot normal
    hide computer normal
    show ig_bot unhappy
    show computer normal
    ig_bot "I do encourage you to attempt to solve this efficiently, and without the bumbling idiocy common to organics."
    ig_bot "Not only does the Admiral dislike failures, but we have limited resources when it comes to chasing criminals across the solar system."
    ig_bot "Budget cutbacks. Blame the Imperial Senate."
    hide ig_bot unhappy
    hide computer normal
    show ig_bot normal
    show computer normal
    ig_bot "According to the dossier the Admiral has forwarded to me, we shall first begin investigating [player_location.name], where the top secret plans were stollen."

label location:
    $ location = next_location(player_location)
    $ x_clue = location.get_rand_clue()
    $ x_trait = get_character_clue(fuel_p)

    jump location_actions

label location_actions:
    scene bg input_background
    hide ig_bot normal
    show computer normal
    menu:
        ig_bot "What are your orders, Inquisitor?"
        "Question Agent X":
            $ active_agent = agent_x
            jump question_agent
        # "Question Agent Y":
        #     $ active_agent = agent_y
        #     jump question_agent
        "Access Imperial Criminal Database":
            jump record_evidence
        "Set Travel Destination":
            jump leave_location

label leave_location:
    $ destination = location_menu(location)

    if destination == 'Back':
        ig_bot "Ok, let's gather more evidence."
        jump location_actions

    scene bg standard
    show ig_bot normal
    show computer normal

    ig_bot "Traveling to [destination]"

    $ player_location = get_location_by_name(destination)
    $ fuel = fuel - fuel_difficulty
    ig_bot "Arrived at [player_location.name]."
    $ fuel_p = get_fuel_percentage()
    ig_bot "Fuel levels are currently at [fuel_p] percent."
    if fuel_p <= 20 and no_of_matches is not 1:
        ig_bot "Have you finished bumbling around yet? We are in danger of running out of fuel."

    if fuel_p == 0 and no_of_matches is not 1:
        jump game_over

    if location.name == player_location.name:
        if no_of_matches is not 1:
            ig_bot "It would seem you aren't as incompetent as your predecessor."
            ig_bot "Scans indicate that the suspect was recently spotted in this sector."
            jump location
        else:
            jump trial_and_capture
    else:
        hide ig_bot normal
        hide computer normal
        show ig_bot unhappy
        show computer normal
        ig_bot "Our scan would suggest that there hasn't been any criminal activity in this sector for quite some time."
        ig_bot "Might I suggest to review the information provided to you by the agents?"
        jump location_actions

label trial_and_capture:
    show ig_bot normal
    ig_bot "Our scanner indicates that the rebel criminal, [warrent], is in the area."
    ig_bot "Agents mobilizing for the capture of [warrent]."
    hide ig_bot normal
    hide computer normal
    scene bg field
    if player_location.name is 'Mars':
        scene bg mars
    if player_location.name is 'Mercury':
        scene bg mercury
    if player_location.name is 'Neptune':
        scene bg neptune
    if player_location.name is 'Uranus':
        scene bg uranus
    show agent normal
    show computer normal
    agent_x "[warrent] has been captured and is currently awaiting processing."

    hide agent normal
    hide computer normal
    show ig_bot normal
    show computer normal

    # Note, create admiral character and add here
    if warrent == villain.name:
        ig_bot "Congratulations, you have successfully apprehended the right person."
    else:
        hide ig_bot normal
        hide computer normal
        show ig_bot unhappy
        show computer normal
        ig_bot "Unfortunately, it would seem [warrent] had nothing to do with the capture of the thing.  Way to mess up."

    return

label question_agent:
    if player_location.name is 'Mars':
        scene bg mars
    if player_location.name is 'Mercury':
        scene bg mercury
    if player_location.name is 'Neptune':
        scene bg neptune
    if player_location.name is 'Uranus':
        scene bg uranus
    hide ig_bot normal
    hide computer normal
    show agent normal
    show computer normal
    active_agent "Agent X reporting from [player_location.name]. What are your orders, Inquisitor?"
    menu:
        "Rebel's Destination":
            jump where_suspect
        "Rebel's Description":
            jump describe_suspect
        "Dismiss":
            jump dismiss_agent

label where_suspect:
    if active_agent == agent_x:
        $ clue = x_clue
    else:
        $ clue = y_clue
    active_agent "Our sources indicate that [villain.pronoun] was [clue]."
    jump question_agent

label describe_suspect:
    $ clue = x_trait
    active_agent "Local rumor states [villain.pronoun] had [clue]."
    jump question_agent

label dismiss_agent:
    active_agent "Very well, Inquisitor!"
    jump location_actions

label record_evidence:
    hide computer normal
    show ig_bot normal
    show computer normal
    ig_bot "Initializing Imperial Criminal Database..."
    hide ig_bot normal
    $ evidence = evidence_recorder(evidence)
    $ matches = calculate_match(evidence)
    $ no_of_matches = len(matches)
    $ warrent = matches[0].name
    hide computer normal
    show ig_bot normal
    show computer normal
    if no_of_matches == 1:
        ig_bot "Warrent issued. All agents keep an eye out for [warrent]."
    jump location_actions


label game_over:
    ig_bot "Unfortunately, you're all out of fuel. Game over!"
    return
