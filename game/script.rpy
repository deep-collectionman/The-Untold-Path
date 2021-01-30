# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define VOICE_IN_OFF = Character("...", color="ffffff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #bshow eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    $ voice_dialogues = [
        "Hello there",
        "How are you, how do you feel?"
        "Is all ok?"
        "Excellent"
    ]

    python:
        for dialogue in voice_dialogues[0:3]:
            say(VOICE_IN_OFF, dialogue)

    menu:
        "This is a menu option. First One":
            "Ok 1"

        "This is a menu option. Second One":
            "Ok 2"

    VOICE_IN_OFF "Let's go ahead and see what happen"
    call select("17")

    VOICE_IN_OFF "That is awesome. We come back to the main function"
    call came(2)

    VOICE_IN_OFF "What about you? Did you forget something?"

    return

label select(name="default"):
    "Well [name]"

    return