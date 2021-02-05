default chat_msg_view = ChatLog()

screen sms_screen():
    frame id "phone_screen":
        xpos 420
        ypos 25
        xsize 360
        ysize 620
        # padding Borders(70,80,72,72).padding
        background Frame("phone_template.png", tile=False)
        foreground None

        use chat_log(chat_msg_view)

label stay_at_home:
    INNER_VOICE "I don't feel in the mood to go out."
    INNER_VOICE "I think that I could stay in home for today."
    INNER_VOICE "I can read some books and then watch a movie."
    INNER_VOICE "..."
    INNER_VOICE "Yeah - that will be fine"

    "You decide to stay at home for the rest of the day. Embraced by the silence of your room."

    play music "../audio/silent_night.wav" fadeout 1

    scene bg room night
    with fade

    ###
    # show screen sms_screen
    # with dissolve
    #
    # $ chat_msg_view.add_chat(
    #   msg="Hey! Are you listen?",
    #   nick="???"
    # )


    "After a while you fall sleepy on the couch... The day was boring as hell."

    "You start thinking that you could had expend your time in a better way today."

    "Some nostalgic feelings invade your body and your memories are bring to light."

    "..."

    "Then you remember someone in particular."

    show standby happy rsz
    with effect_flashbulb

    pause 2

    hide standby happy
    with effect_flashbulb

    "..."

    INNER_VOICE "Who was she?"
    INNER_VOICE "..."
    INNER_VOICE "Ugh..."
    INNER_VOICE "I can't remember her"
    INNER_VOICE "Anyways"
    INNER_VOICE "What a day..."

    "..."

    VOICE_IN_OFF "Nothing important happen today besides I told you that you must to pay attention"
    VOICE_IN_OFF "I told you - Now there is nothing that I can do to help you..."
    VOICE_IN_OFF "..."
    VOICE_IN_OFF "Just continue... with your monotonous life"

    pause 2

    "Your start feeling that you missed something relevant in your life"

    play music "../audio/bad ending.mp3" fadein 2

    scene black
    with dissolve

    show text "The End"
    with dissolve
    
    pause

    return