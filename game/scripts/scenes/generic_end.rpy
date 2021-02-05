label generic_end:
    call on_progress_label

    show text "The End"
    with dissolve
    with Pause(2)

    return

label on_progress_label:
    scene black
    with dissolve

    show text "Still in Progress"
    with dissolve
    with Pause(2)
     