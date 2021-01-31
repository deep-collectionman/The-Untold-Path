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

# Effects

define effect_flashbulb = Fade(0.2, 0.0, 0.8, color="#fff")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black 
    with fade

    "Welcome to The Untold Path"

    "Maybe you are asking to yourself what all is this about... or maybe not. But anyways let me tell you."

    "The explanation will be briefly."

    "This game is about the decisions that you make BY YOUR OWN CHOICE regarding the different events that have place in this story."

    "Have into account that you will be talking with people who you haven't seen in a long time."

    "And maybe the things that you do during the game will impact in the relationship that you have with the other people. You must to figure out how to reconnect your old feelings that you lost long time ago."

    "You could ended up losing all your loved ones if you are careless."

    "Enjoy the game"

    play music "./audio/rill_sound.mp3" fadeout 1

    scene bg beautiful park game
    with dissolve

    "The sounds of water and wind can be feel in the atmosphere..."

    scene bg beautiful park game
    with effect_flashbulb

    show standby anger rsz at center
    with dissolve

    UNKNOW_PERSON "Hey" 
    UNKNOW_PERSON "Hey! are you listen?"

    play sound "./audio/wind.ogg"

    menu:
        "No":
            UNKNOW_PERSON "Argh... You dumbass!"
            $ RELEVANCE_VARIABLE = RELEVANCE_VARIABLE - 0.5
        "Umm Yeah. What happen?":
            UNKNOW_PERSON "Can you came here?"

    UNKNOW_PERSON "Look... I lost my dog here in the park."
    UNKNOW_PERSON "I got distracted listening to the local musicians"
    UNKNOW_PERSON "And then he started running to somewhere following something and I lost the clue of where he can be"
    UNKNOW_PERSON "Could you help me to find him?"

    menu:
        "I have better things to do":
            UNKNOW_PERSON "Oh well. Thank you for you KINDNESS"
            $ KINDNESS_ALLOWED = False
            $ RELEVANCE_VARIABLE = RELEVANCE_VARIABLE - 0.20
            call better_things_to_do
        "Fine":
            UNKNOW_PERSON "Ok. Follow me"
            call search_for_dog
        "Yeah sure! I will search between the trees and shrubbery there":
            UNKNOW_PERSON "Great!"
            $ KINDNESS_ALLOWED = True
            call search_for_dog


    return


label better_things_to_do:
    INNER_VOICE "Ugh... I don't want to waste my time finding what the others lost by their own negligence"

    VOICE_IN_OFF "That was gross of your part."
    VOICE_IN_OFF "You may not be the kind of person who is predisposed to helping to other. I will delete that characterist of your person"
    VOICE_IN_OFF "..."
    VOICE_IN_OFF "Done!"

    return


label search_for_dog:
    show find dog park
    with fade 

    "Where you want to start searching?"

    menu:
        "Go to left":
            "Mmmm... It seems that he is not here."
        "Search between the tree":
            play sound "./audio/ambience.ogg"
            "Well, It seems that I'm close to him..." 
            "Hey buddy! Where are you?"

    return
    
