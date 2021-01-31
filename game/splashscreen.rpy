# This is the splashscreen shown at the beginning of the game

label splashscreen:
    scene presplash
    with dissolve
    with Pause(3)

    scene black
    with dissolve

    show text "Global Game Jam 2021..."
    with dissolve
    with Pause(1)

    hide text 
    with dissolve 
    with Pause(1.5)

    show text "or I should said 2020 and a quarter"
    with dissolve
    with Pause(1)

    hide text 
    with dissolve 
    with Pause(1.5)

    show text "By collectionman#9288 ..."
    with dissolve 
    with Pause(1)

    hide text 
    with dissolve 
    with Pause(2)

    return
