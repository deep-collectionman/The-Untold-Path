# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define VOICE_IN_OFF = Character("...", color="#ffffff")


define effect_flashbulb = Fade(0.2, 0.0, 0.8, color="#fff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black 
    with fade

    "Welcome to The Untold Path"

    "Maybe you are asking to yourself what all is this about... or maybe not but anyways let me tell you."

    "The explanation will be briefly. This game is about the decisions that you make BY YOUR OWN CHOICE regarding the different events that have place in this story"

    "Enjoy the game"

    scene bg beautiful park game
    with dissolve

    "The completly silence can be feel in the atmosphere..."

    scene bg beautiful park game
    with effect_flashbulb

    VOICE_IN_OFF "Hey, are you listen?" 

    return