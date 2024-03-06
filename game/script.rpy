label start:

    # This label configures the anticheat number for the game after Act 1.
    $ anticheat = persistent.anticheat

    # This variable sets the chapter number to 0 to use in the mod.
    $ chapter = 0

    # This variable controls whether the player can dismiss a pause in-game.
    $ _dismiss_pause = config.developer

    ## Names of the Characters
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ k_name = "Kotonoha"
    $ y_name = "Yuri"
    $ km_name = "Mother"
    $ kf_name = "Father"
    $ na_name = "Girl 1"

    # This variable controls whether the quick menu in the textbox is enabled.
    $ quick_menu = True

    # This variable c ontrols whether we want normal or glitched dialogue
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # This variable controls whether Sayori is dead. It is recommended to leave
    # this as-is.
    $ in_sayori_kill = None
    
    # These variables controls whether the player can skip dialogue or transitions.
    $ allow_skipping = True
    $ config.allow_skipping = True

    if persistent.playthrough == 0:
        $ style.say_window = style.window
        call ch0 from _call_ch0