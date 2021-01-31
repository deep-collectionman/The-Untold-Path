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
    pause

    show text "Maybe you are asking to yourself what all is this about... or maybe not. But anyways let me tell you."
    with dissolve
    pause

    show text "The explanation will be briefly."
    with dissolve
    pause

    show text "This game is about the decisions that you make BY YOUR OWN CHOICE regarding the different events that have place in this story."
    with dissolve
    pause

    show text "Have into account that you will be talking with people who you haven't seen in a long time."
    with dissolve
    pause

    show text "And maybe the things that you do during the game will impact in the relationship that you have with the other people. You must to figure out how to reconnect your old feelings that you lost long time ago."
    with dissolve
    pause

    show text "You could ended up losing your loved ones if you are careless"
    with dissolve
    pause

    show text "Enjoy the game"
    with dissolve
    pause

    stop music fadeout 2
    call play_alarm from _call_play_alarm

    scene bg room day
    with dissolve

    INNER_VOICE "Uhmm... What hour it's?"

    play music "./audio/urban noise.mp3"

    VOICE_IN_OFF "Today is an important day so pay attention please"

    INNER_VOICE "?"
    INNER_VOICE "What was that?"

    INNER_VOICE "..."

    scene bg room light rsz
    with dissolve

    INNER_VOICE "It looks pretty shiny out there."
    INNER_VOICE "..."
    INNER_VOICE "I feel really sleepy after had been working all the night and waking up in this way"

    VOICE_IN_OFF "Do you really feel like that?"

    INNER_VOICE "Huh?"
    INNER_VOICE "..."
    INNER_VOICE "Uhmm - What should I do today?"

    menu:
        "Go to the park":
            INNER_VOICE "Ok - I think that I should spend some time out and see if there is something interesting to do."
            INNER_VOICE "Maybe I could pass through the market and buy some things that I need"

            VOICE_IN_OFF "You don't really need nothing today"

            INNER_VOICE "..."
            INNER_VOICE "I swear that I'm listening some weird voices there"

            call park_scene from _call_park_scene
        "Stay at home":
            call stay_at_home from _call_stay_at_home

    scene black 
    with fade

    show text "The End"
    pause

    return
    
label play_alarm:
    play sound "./audio/clock.ogg"

    pause 3

    play sound "./audio/alarm.mp3"

    return