label park_scene:
    play music "../audio/rill_sound.mp3" fadeout 1

    scene black
    with dissolve

    show text "You decide to go out of home and feel the breeze for a moment."
    with dissolve
    with Pause(2)

    hide text
    with dissolve

    scene bg beautiful park game
    with dissolve

    "The sounds of water and wind can be feel in the atmosphere..."

    INNER_VOICE "The day is explendid!"
    INNER_VOICE "The sun breeze of April is the best thing in the world."
    INNER_VOICE "I hope to have some extra time to come back to the park after buying some things and enjoy the time."

    "All seems to be pretty calm until you hear a voice"

    INNER_VOICE "..."

    scene bg beautiful park game
    with effect_flashbulb

    show standby anger rsz at center
    with dissolve 

    UNKNOW_PERSON "Hey" 
    UNKNOW_PERSON "Hey! are you listen?"

    menu:
        "No":
            UNKNOW_PERSON "Urgh... You dumbass!"
            $ RELEVANCE_VARIABLE = RELEVANCE_VARIABLE - 0.5
        "Uhm Yeah. What happen?":
            UNKNOW_PERSON "Can you came here?"

    UNKNOW_PERSON "Look... I lost my dog here in the park."
    UNKNOW_PERSON "I got distracted watching the birds flying around the park"
    UNKNOW_PERSON "And then he started running to the bushes following something and I lost the clue of where he can be"
    UNKNOW_PERSON "Could you help me to find him?"

    menu:
        "I have better things to do":
            UNKNOW_PERSON "Oh well. Thank you for you KINDNESS"

            hide standby anger rsz
            with dissolve

            $ KINDNESS_ALLOWED = False
            $ RELEVANCE_VARIABLE = RELEVANCE_VARIABLE - 0.20
            call better_things_to_do from _call_better_things_to_do
        "Fine":
            UNKNOW_PERSON "Ok. Follow me"
            call search_for_dog from _call_search_for_dog
        "Yeah sure! I will search between the trees and shrubbery there":
            UNKNOW_PERSON "Great!"
            $ KINDNESS_ALLOWED = True
            call search_for_dog from _call_search_for_dog_1

    return

label better_things_to_do:
    INNER_VOICE "Ugh... I don't want to waste my time finding what the others lost by their own negligence"

    "..."

    pause 1

    VOICE_IN_OFF "That was gross of your part."
    VOICE_IN_OFF "..."
    VOICE_IN_OFF "Ugh.. you may not be the kind of person who is predisposed to helping to others."

    "What do you want to do now?"

    menu:
        "Start walking around the park":
            pause 0.5
            #  call stay at the park
            
        "Come back to start searching for the dog":
            "You start to regret what you did at moment ago"

            INNER_VOICE "Uh - Thinking it better I should come back to see If I can find him"   

            call search_for_dog from _call_search_for_dog_2
        "Go to the beach":
            # call beach_scene_alone:
            scene black
            with dissolve

            show text "Feeling upset you start walking with direction to the beach"
            with dissolve
            with Pause(2)

    call generic_end

    return

label search_for_dog:
    scene find dog park
    with fade 

    "Where you want to start looking for?"

    menu:
        "Keep walking throught the footpath":
            INNER_VOICE "Mmmm... It seems that he is not here."
            
            "Suddenly you hear the voice of the girl who you were talking a moment ago."

            UNKNOW_PERSON "It's here!!"

            "You decided to follow her voice."
        "Search between the trees":
            play sound "../audio/ambience.ogg"
            "Well - It seems that I'm close to him..." 
            "Hey buddy! Where are you?"

            "You can see a furry thing trying to catch some butterflies there."

            UNKNOW_PERSON "You found him!"

            stop sound

    show standby joy rsz at center
    with dissolve
    
    UNKNOW_PERSON "Pepper! You're going to scare me to death if you keep running out of my sight"
    UNKNOW_PERSON "But I'm so glad that we could find you."

    show standby sarrow rsz at center
    with dissolve

    UNKNOW_PERSON "Don't make this again to me Pepper - please."
    "..."

    show standby happy rsz at center
    with dissolve

    UNKNOW_PERSON "And thank you for helping me with this. I don't know what I will do if I lost him."

    play sound "../audio/Well Done CCBY3.ogg" fadein 1

    "There is a voice in your head. While she stands smiling at you."
    "..."

    VOICE_IN_OFF "It seems that you like it. Do you want to continue chatting with her?"
    INNER_VOICE "..."

    menu:
        "Remain in silence":
            INNER_VOICE "..."
            INNER_VOICE "Uh - What? From where came that voice?"
        "You blush":
            VOICE_IN_OFF "Hahaha. Look at that red face!"
            "You can barely stay calm while you are looking her."

    "..."

    UNKNOW_PERSON "Why do you stay there like a dumb?"

    INNER_VOICE "..."

    show standby joy rsz at center
    with dissolve

    UNKNOW_PERSON "By the way - I didn't introduce myself."
    UNKNOW_PERSON "My name is Mary."

    menu:
        "Nice to meet you Mary":
            $ RELEVANCE_VARIABLE = RELEVANCE_VARIABLE + 0.10

            show standby happy rsz at center
            with dissolve

            MARY "The pleasure is mine"
        "Hi...":
            show standby happy rsz at center
            with dissolve
    
    INNER_VOICE "..."
    INNER_VOICE "Damn! Her smile is so familiar to me but I can't remember"

    MARY "What were you doing here?"

    INNER_VOICE "Huh?"

    show standby anger rsz
    with dissolve

    MARY "Yes - I'm talking to you!"

    show standby happy rsz
    with dissolve

    MARY "What were you doing before we met?"

    menu:
        "I don't know. I just started walking to nowhere":
            MARY "Oh - really?"
            MARY "For me it was pretty much the same. I just decided to take some fresh air while I let Pepper play around in the park."
            MARY "Well - In that case I think that I had been blessed with your presence after all."
        "It's not of your business":
            VOICE_IN_OFF "This part of the game remain incompletely..."
    
    call generic_end

    return