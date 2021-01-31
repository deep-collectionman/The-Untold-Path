# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Relevance variable. This is one of the most important aspects of the game

define RELEVANCE_VARIABLE = 0

# Player feelings

define KINDNESS_ALLOWED     = None
define HUMILITY_ALLOWED     = None
define CURIOSITY_ALLOWED    = None
define PARANOIC_ALLOWED     = None
define PATIENCE_ALLOWED     = None
define JOY_ALLOWED          = None 

# Characters

define UNKNOW_PERSON = Character("?", color="#e5e5e5")
define VOICE_IN_OFF = Character("...", color="#ffffff")
define INNER_VOICE = Character("You", color="#2561a4")
define MARY = Character("Mary", color="#23b182")

# Effects

define effect_flashbulb = Fade(0.2, 0.0, 0.8, color="#fff")

# Ending

define KIND_OF_ENDING = None

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black 
    with fade

    show text "Welcome to The Untold Path"
    with dissolve
    # with Pause(1)
    pause

    show text "Maybe you are asking to yourself what all is this about... or maybe not. But anyways let me tell you."
    with dissolve
    # with Pause(1)
    pause

    show text "The explanation will be briefly."
    with dissolve
    # with Pause(1)
    pause

    show text "This game is about the decisions that you make BY YOUR OWN CHOICE regarding the different events that have place in this story."
    with dissolve
    # with Pause(1)
    pause

    show text "Have into account that you will be talking with people who you haven't seen in a long time."
    with dissolve
    # with Pause(1)
    pause

    show text "And maybe the things that you do during the game will impact in the relationship that you have with the other people. You must to figure out how to reconnect your old feelings that you lost long time ago."
    with dissolve
    # with Pause(1)
    pause

    show text "You could ended up losing all your loved ones if you are careless."
    with dissolve
    # with Pause(1)
    pause

    show text "Enjoy the game"
    with dissolve
    # with Pause(1)
    pause

    stop music fadeout 2
    call play_alarm

    scene bg room day
    with dissolve

    INNER_VOICE "Uhmm... What hour it's?"

    VOICE_IN_OFF "Today is an important day. Pay attention"

    INNER_VOICE "?"
    INNER_VOICE "What was that?"

    menu:
        "Go to the park":
            call park_scene
        "Stay at home":
            call stay_at_home

    scene black 
    with fade

    show text "The End"
    # with Pause(1)
    pause

    return
    
label play_alarm:
    play sound "./audio/clock.ogg"

    pause 3

    play sound "./audio/alarm.mp3"

    return