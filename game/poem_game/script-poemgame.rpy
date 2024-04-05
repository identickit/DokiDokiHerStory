## script-poemgame.rpy

# This file contains the code to the DDLC poem game (now improved [finally...])
# Still commented a bit by Terra.

init python: 
    # This dictionary stores every poemword and the class preference values of each character.
    full_wordlist = {}

    # This class holds a word, and point values for each of the four heroines
    class PoemWord:
        def __init__(self, s):
            self.sPoint = s
        def val(self):
            return self.sPoint

    with renpy.file("poem_game/poemwords.txt") as pf:
        for line in pf:
            line = line.decode("utf-8").strip()
            # Ignore lines beginning with '#' and empty lines
            if line == '' or '#' in line: continue
            # File format: word,sPoint
            x = line.split(',')
            full_wordlist[x[0]] = PoemWord(int(x[1])).val()

    # This class handles Chibi Movement in a better way
    class ChibiTrans(object):
        def __init__(self):
            self.charTime = renpy.random.random() * 4 + 4
            self.charPos = 0
            self.charOffset = 0
            self.charZoom = 1

        def produce_random(self):
            return renpy.random.random() * 4 + 4

        def reset_trans(self):
            self.charTime = self.produce_random()
            self.charPos = 0
            self.charOffset = 0
            self.charZoom = 1

        def randomPauseTime(self, trans, st, at):
            if st > self.charTime:
                self.charTime = self.produce_random()
                return None
            return 0

        def randomMoveTime(self, trans, st, at):
            if st > .16:
                if self.charPos > 0:
                    self.charPos = renpy.random.randint(-1,0)
                elif self.charPos < 0:
                    self.charPos = renpy.random.randint(0,1)
                else:
                    self.charPos = renpy.random.randint(-1,1)
                if trans.xoffset * self.charPos > 5: self.charPos *= -1
                return None
            if self.charPos > 0:
                trans.xzoom = -1
            elif self.charPos < 0:
                trans.xzoom = 1
            trans.xoffset += .16 * 10 * self.charPos
            self.charOffset = trans.xoffset
            self.charZoom = trans.xzoom
            return 0
    
    # This dictionary stores every poemgame character and their points.
    chibis = {}

    # This class supers' ChibiTrans and is used to store poem point data.
    class Chibi(ChibiTrans):
        POEM_DISLIKE_THRESHOLD = 29
        POEM_LIKE_THRESHOLD = 45

        def __init__(self, name):
            if not isinstance(name, str):
                raise Exception("'name' argurment must be a string, not " + type(name))
                
            self.charPointTotal = 0
            self.appeal = 0
            super(Chibi, self).__init__()
            chibis[name] = self

        def reset(self):
            self.charPointTotal = 0
            self.reset_trans()

        def add(self, point):
            self.charPointTotal += point
        
        def calculate_appeal(self):
            if self.charPointTotal < self.POEM_DISLIKE_THRESHOLD:
                return -1
            elif self.charPointTotal > self.POEM_LIKE_THRESHOLD:
                self.win = True
                return 1
            return 0

    seen_eyes_this_chapter = False

    # Declare Chibi variables for transforms and points.
    chibi_s = Chibi('sayori')

    telist = [audio.te01, audio.te02]
    poemf = True

    # Start of the poem game in python
    def poem_game_startf():
        played_baa = False
        poemgame_glitch = False

        # Resets points of every character
        for c in chibis:
            chibis[c].reset()
        
        # Makes a copy of the full dictionary for editing purposes.
        
        wordList = full_wordlist.copy()

        # A way better while loop than Dan did
        progress = 1
        progresspb = 1
        while progress <= 1:
            # This section grabs 10 random words and stores the word in a list.
            random_words = []
            # While the length of the list is less than 10.
            while len(random_words) < 10:
                #Var word is decided randomly from the list of wordList keys.
                word = random.choice(list(wordList.keys()))
                #If the current wordList word's value is equal to the progress, then add to the list.
                if wordList[word] in (progresspb,progresspb+1):
                    random_words.append(word)
                    # Remove the word from the full dictionary once its picked and added from the local copy (while it equals a certain value).
                    del wordList[word]

            # Display the poem game
            
            poemword = renpy.call_screen("poem_test", words=random_words, progress=progress, poemgame_glitch=poemgame_glitch)

            renpy.play(gui.activate_sound)

            progress += 1

    # Start of the poem game in python
    def poem_game_start():
        played_baa = False
        poemgame_glitch = False
        poemf = False

        # Resets points of every character
        for c in chibis:
            chibis[c].reset()
        
        # Makes a copy of the full dictionary for editing purposes.
        
        wordList = full_wordlist.copy()

        # A way better while loop than Dan did
        progress = 1
        progresspb = 3
        while (renpy.music.is_playing('music')):
            while progress <= 2:
                # This section grabs 10 random words and stores the word in a list.
                random_words = []
                # While the length of the list is less than 10.
                while len(random_words) < 10:
                    #Var word is decided randomly from the list of wordList keys.
                    word = random.choice(list(wordList.keys()))
                    #If the current wordList word's value is equal to the progress, then add to the list.
                    if wordList[word] in (progresspb,progresspb+1):
                        random_words.append(word)
                        # Remove the word from the full dictionary once its picked and added from the local copy (while it equals a certain value).
                        del wordList[word]

                # Display the poem game
                poemword = renpy.call_screen("poem_test", words=random_words, progress=progress, poemgame_glitch=poemgame_glitch)
                renpy.play(gui.activate_sound)
                renpy.music.play(telist[progress], loop=False)

                # Adds points to the characters and progress by 1.
                progresspb += 2
                progress += 1
            

    def poem_game_startpb():

        # Resets points of every character
        for c in chibis:
            chibis[c].reset()
        
        # Makes a copy of the full dictionary for editing purposes.
        
        wordList = full_wordlist.copy()

        # A way better while loop than Dan did
        progress = 1
        progresspb = 1
        while progress <= 1:
            # This section grabs 10 random words and stores the word in a list.
            random_words = []
            # While the length of the list is less than 10.
            while len(random_words) < 10:
                #Var word is decided randomly from the list of wordList keys.
                word = random.choice(list(wordList.keys()))
                #If the current wordList word's value is equal to the progress, then add to the list.
                if wordList[word] in (progresspb,progresspb+1):
                    random_words.append(word)
                    # Remove the word from the full dictionary once its picked and added from the local copy (while it equals a certain value).
                    del wordList[word]

            # Display the poem game
            while (renpy.music.is_playing('music')):
                poemword = renpy.call_screen("poem_test", words=random_words, progress=progress, poemgame_glitch=poemgame_glitch)
            else:
                progress += 1

            renpy.play(gui.activate_sound)

            progresspb += 2
            progress += 1
            
    
    # End of the game
    def poem_game_finish():
        poemwinner[chapter] = max(chibis, key=lambda c: chibis[c].charPointTotal)


#Words argument is equal to random_words list.
screen poem_test(words, progress, poemgame_glitch, progresspb = 1):

    if progress is not None:

        # Two fixed areas for the two sections of poemgame we have
        fixed:
            xpos 440
            ypos 160
            
            viewport:
                has vbox
                spacing 56

                if poemf == True:
                    for i in range(5):
                        python:
                            wordString = words[i]

                        textbutton wordString:
                            if words[i] == "silver":
                                if clock >= 3:
                                    action Return(wordString)
                                    text_style "poemgame_text"
                                else:
                                    text_style "poemgame_text"
                            else:
                                text_style "poemgame_text"

                else:
                    for i in range(5):
                        python:
                            wordString = words[i]

                        textbutton wordString:

                            if words[i] == "lavender":
                                if 12 >= clock >= 9:
                                    action Return(wordString)
                                    text_style "poemgame_text"
                                else:
                                    text_style "poemgame_text"

                            elif progress == 2:
                                text_style "poemgame_text"

                            else:
                                action Return(wordString)
                                text_style "poemgame_text"
                    

        fixed:
            xpos 680
            ypos 160

            viewport:
                has vbox
                spacing 56

                if poemf == True:
                    for i in range(5):
                        python:
                            wordString = words[5+i]

                        textbutton wordString:
                            if words[5+i] == "silver":
                                if clock >= 3:
                                    action Return(wordString)
                                    text_style "poemgame_text"
                                else:
                                    text_style "poemgame_text"
                            else:
                                text_style "poemgame_text"

                else:
                    for i in range(5):
                        python:
                            wordString = words[5+i]

                        textbutton wordString:
                            
                            if words[5+i] == "lavender":
                                if 12 >= clock >= 9:
                                    action Return(wordString)
                                    text_style "poemgame_text"
                                else:
                                    text_style "poemgame_text"

                            elif progress == 2:
                                text_style "poemgame_text"

                            else:
                                action Return(wordString)
                                text_style "poemgame_text"


label poemboss(transition=True):
    stop music fadeout 2.0

    scene bg notebook
        
    if transition:
        with dissolve_scene_full

    $ config.allow_skipping = False
    $ allow_skipping = False

    show screen my_timer
    show screen dialog("Look, I appreciate your interest in this project...", ok_action=Hide("dialog"))
    $ poem_game_startf()
    hide screen my_timer
    $ clock = 0
    $ poemf = False
    call screen dialog("But this one isn't supposed to have any poem games.", ok_action=Return())
    call screen dialog("I'm not entirely sure why Yuri advised Kotonoha to write random words...", ok_action=Return())
    call screen dialog("However, unfortunately I need to ask you to stop playing.", ok_action=Return())
    pause 2.0
    call screen dialog("When you get bored here, you can show yourself out.", ok_action=Return())
    $ run_input ("", "Accessing mic...")
    pause 2.0
    hide screen console_screen
    pause 2.0
    show screen my_timer
    play music te01
    
    $ poem_game_start()
    $ poem_game_startpb()
    $ poem_game_finish()

    $ config.allow_skipping = True
    $ allow_skipping = True

    stop music fadeout 2.0
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return

## Scare code moved as it's own label
label poem_eye_scare:
    $ seen_eyes_this_chapter = True
    $ quick_menu = False
    play sound "sfx/eyes.ogg"
    $ persistent.seen_eyes = True
    stop music
    scene black with None
    show bg eyes_move
    pause 1.2
    hide bg eyes_move
    show bg eyes
    pause 0.5
    hide bg eyes
    show bg eyes_move
    pause 1.25
    hide bg eyes with None
    $ quick_menu = True
    return

############ Image definitions start here. #############
image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
        
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset chibi_s.charOffset xzoom chibi_s.charZoom
    block:
        function chibi_s.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_s.randomMoveTime
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset chibi_n.charOffset xzoom chibi_n.charZoom
    block:
        function chibi_n.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_n.randomMoveTime
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset chibi_m.charOffset xzoom chibi_m.charZoom
    block:
        function chibi_m.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_m.randomMoveTime
        repeat

image r_sticker:
    "mod_assets/rikka_assets/r_sticker_1.png"
    xoffset chibi_r.charOffset xzoom chibi_r.charZoom
    block:
        function chibi_r.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_r.randomMoveTime
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset chibi_s.charOffset xzoom chibi_s.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image r_sticker hop:
    "mod_assets/rikka_assets/r_sticker_2.png"
    xoffset chibi_r.charOffset xzoom chibi_r.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "r_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset chibi_n.charOffset xzoom chibi_n.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset chibi_m.charOffset xzoom chibi_m.charZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset chibi_y.charOffset xzoom chibi_y.charZoom zoom 3.0
    block:
        function chibi_y.randomPauseTime
        parallel:
            sticker_move_n
        parallel:
            function chibi_y.randomMoveTime
        repeat

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_mright:
    xcenter 330 yalign 0.5 subpixel True

transform sticker_mleft:
    xcenter 100 yalign 0.5 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
