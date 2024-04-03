default persistent.autosave = False
label ch0:
    $ persistent.autosave = True
    scene bg koto_bedroom
    with dissolve_scene_full
    play music wn6
    "My alarm goes off on my phone."
    "I slowly reach to turn it off, but instead of feeling the flat surface of my phone..."
    "I jerk my hand back quickly and sit straight up in my bed."
    "I shouldn't have placed my broken watch so close to my phone."
    "Sure, I needed a reminder to get it fixed, but this is a bit more than a reminder now."
    "I get up and pull out a bandage from a nearby cabinet."
    "After wrapping it around my finger, I tap my phone screen and finally turn off my alarm."
    scene bg koto_livingroom
    with dissolve_scene_half
    #kotonoha perspective
    show km 1a at t11
    km "What did you do to yourself now?"
    k "Huh?"
    km "Don't {i}'Huh?'{/i} me!"
    km "Did you think I wasn't going to notice your hand?"
    "I briefly hold up my hand and flex my wounded finger a bit."
    k "D-Don't worry, mother! It isn't serious."
    km "Of course it isn't. It doesn't have to be a major injury, as long as your friends at school can see it, right?"
    show km 1a at t21
    show kf 1a at f22
    kf "Noriko, dear... Koto has obviously grown since the last time she acted how you're implying."
    show km 1a at f21
    show kf 1a at t22
    km "Don't you dare try to get her off the hook!"
    km "Why else would she be hurt like this?"
    show km 1a at t21
    "I almost open my mouth to retort, but there's no way I can admit that I broke grandmother's watch."
    "I just stand in front of my mother, hoping that she doesn't take it any further."
    show kf 1a at f22
    kf "Look, honey: As long as she's not seriously hurt, there shouldn't be anything to worry about."
    kf "I trust her."
    show km 1a at f21
    show kf 1a at t22
    km "... {i}Fine{/i}"
    km "Go make yourself some breakfast and then get ready for school."
    km "You are {i}not{/i} arriving late again."
    show km 1a at t21
    show kf 1a at f22
    kf "Noriko, she was feeling ill the morning she-"
    show km 1a at f21
    show kf 1a at t22
    km "Don't push it, Saruka."
    show km at thide
    show kf at thide
    hide km
    hide kf
    "I quickly head to the kitchen to prepare my food before they get into it again."
    ##scene 2
    scene bg cafeteria
    with dissolve_scene_full
    play music wok
    k "Mother's gonna to kill me for sure now."
    show yuri turned curi me oe at t11
    y "I'm sure whatever it is isn't as bad as it seems."
    k "I got an 84 on my Chemistry exam."
    y "..."
    show yuri turned neut cm e1b at t11
    y "Okay, that's admittedly pretty bad."
    show yuri turned flus e1a cm at t11
    y "Not the grade, of course. I personally believe your grades aren't prefect reflections-"
    k "-of your true potential. I know. You always see the best in everyone."
    k "I love you for that."
    show yuri turned happ cm oe blus at t11
    y "A gentle reminder that I'm your cousin, dear Koto."
    k "What do you mean-"
    k "Oh."
    "I chuckle a little at her joke. She can be pretty funny when she wants to be."
    show yuri turned laug cm e1a nobl at t11
    y "Anyways, I'm sure your father will be understanding?"
    k "Yeah... He's always had my back, hasn't he?"
    k "... Reminds me of when we were little and he took us both to the mall."
    show yuri ce at t11
    k "We knocked over those mannequins and covered for us when Mother saw the resulting scene."
    "I laugh to myself for a minute before noticing the look on my cousin's face."
    show yuri turned neut oe ma at t11
    y "..."
    y "I haven't heard you laugh in so long."
    k "C'mon, surely it hasn't been..."
    "..."
    "I feel my face burn up a little."
    "I genuinely can't remember the last time I had a good laugh."
    show yuri ce at t11
    y "You don't have to be prefect, Koto. No matter what she says."
    y "There's people out there who will always see how incredible and irreplaceable you are."
    k "Yuri..."
    #bell ringing sfx
    "The bell rings, signaling the end of our lunch period."
    show yuri oe at t11
    "Yuri and I stand and look each other for a moment before she breaks our silence."
    y "It's going to be okay, Silver."
    k "... Thank you, Lavender."
    "It has to have been years since we've called each other by those names."
    "But it manages to make my heart jump a little, the same way it did when I got to hang with my cousin back then."
    ##scene 3
    scene bg class_day
    with dissolve_scene_full
    #play music tkoto
    "I enter my next class, heading towards the front of the room..."
    "... Where I apparently don't sit anymore?"
    show na 1a at t11 
    k "Excuse me, ma'am? I believe this is my seat."
    na "Oh, sorry! Somebody took my seat and I'm uh..."
    na "Honestly, I'm not the kind of person who likes confrontations..."
    k "... No worries, Miss..."
    na "No need to call me by my last name. I'm Naomi."
    $ na_name = "Naomi"
    k "Nice to meet you. I'm-"
    na "Kotonoha, right?"
    k "Y-Yes... Just out of curiosity, how do you...?"
    na "Yuri talks about how sweet you are."
    na "She looks up to you a lot, you know? You're probably her favorite person by how she talks about you."
    "I feel my face burning as I smile."
    na "Sorry, wasn't trying to put you on the spot. But the way you treat your cousin is..."
    na "... Incredible. Never stop being you, Kotonoha."
    k "Please, call me Koto."
    "I hold out my hand for Naomi to shake."
    "{i}Anything to change the subject before I completely freeze up.{/i}"
    "She shakes my hand before our teacher walks in."
    scene bg class_day
    with wipeleft_scene
    t "Okay, everyone! Time is up."
    "I put my pencil down and place my exam on the corner of my desk."
    "After a few minutes, our teacher has graded our exams and handed them back to us."
    "..."
    "{i}No{/i}..."
    "He can't be serious..."
    "Mother is going to kill me if I get anything below a 90 on an exam..."
    "Once the bell rings and everyone starts filing out, I approach my teacher."
    k "Excuse me, sir?"
    t "Ah, how may I help you, Kotonoha?"
    k "I noticed that I received an 87 on my exam, and I was curious if there was any way..."
    t "That you could get some extra credit?"
    "I nod politely."
    t "I'm sorry, but it wouldn't be fair if I only offered such an opportunity for one student."
    k "O-Oh..."
    "{i}What do I do??{/i}"
    "..."
    "I have to tell him the truth about..."
    k "Look... I haven't gotten anything below a 90 yet in this class..."
    k "A-And my mother has very high expectations for my grades..."
    k "If there's... any way you'd be willing to make some sort of exception..."
    t "..."
    t "Before I ask this, it isn't because I don't believe you. I just want to verify something."
    t "Who's your mother, if you don't mind my asking?"
    k "Noriko Ha-"
    t "Oh."
    t "I'm sorry you have... I mean, I'll..."
    t "... How about this: I'll give you some sort of makeup assignment so you can get a few extra points."
    t "I'll have to give it to everyone in the class, of course, but how would you feel about-"
    k "That would be amazing!"
    k "... Sorry, I didn't mean to interrupt."
    t "That's quite alright. I'll email you once the assignment has been published."
    t "And if it helps any, I'll hold on to your exam. If your mother asks what you made..."
    t "Feel free to tell her I needed some extra time to grade everyone's exams this time around."
    k "Thank you so much."
    "I bow and wish him a great rest of his day"
    ##scene 4
    scene bg residential_day
    with dissolve_scene_full
    stop music
    "I've never seen a teacher work so fast."
    "He's already published the extra credit assignment during my walk home."
    k "Everything's going to work out, Kotonoha..."
    "I mutter this under my breath yet again during my commute alone."
    "But this time, I'm a bit more confident in saying it."
    k "You're gonna be alright..."
    "I step onto my front porch and take a deep breath."
    k "Everything will work out."
    "I gently open the door."
    scene bg koto_livingroom
    with dissolve_scene_half
    "... No one's home?"
    "Usually, this is about the time when Father is getting ready to go out for work."
    "And Mother will typically be out in the living room so she can ask about my grades."
    k "I'm home!"
    "I shout loud enough so that my parents can hear if they're in their room."
    "Sure, I'll get told off for speaking loudly in the house, but at least I'll know if they're here."
    "... There's no response."
    "I pull out my phone and dial Yuri's number, but before I can hit call I hear a knock on the front door."
    "... Yuri?"
    show yuri turned happ cm ce at t11
    y "Hello, dear cousin."
    show yuri oe at t11
    y "I just wanted to..."
    show yuri me at t11
    y "Are you feeling okay? You look rather anxious."
    k "Yuri, are my parents out with yours right now?"
    show yuri turned curi mj oe at t11
    y "Koto, they went out last week. They only go out once a month, don't they?"
    k "... So that's a no?"
    y "Indeed."
    y "..."
    show yuri turned flus e1a md b2b at t11
    "Apparently I look even more anxious now, because Yuri's expression changes to one of concern."
    y "What's wrong?"
    k "I don't think they're here."
    show yuri me b1a at t11
    y "They aren't?"
    y "From what you've told me before-"
    k "Yes, they're usually here right now."
    k "And I-"
    y "Hey..."
    show yuri turned neut b1c md at t11
    "She puts her hands on my shoulders and looks deeply into my eyes."
    "She's probably able to tell I'm on the verge of a panic attack right about now."
    y "It's going to be okay, Koto."
    "..."
    "I take a few deep breaths before gently nodding."
    y "Have you tried calling them yet?"
    "I shake my head, not breaking eye contact from the one person keeping me from freaking out."
    y "Why don't we try calling them to see where they are?"
    k "Okay..."
    "I look down at my phone and dial my mother's number."
    "A few rings..."
    "..."
    "No answer."
    show yuri turned flus e1a md b2b at t11
    y "Maybe... try again?"
    "I redial..."
    "..."
    "Still no answer."
    "I make a small sound that sounds awfully similar to when I lost my parents once when I was much younger."
    show yuri me at t11
    y "How about I look to see if they're here and just aren't answering for some reason?"
    "I nod slightly."
    show yuri at thide
    hide yuri
    "I try calling again..."
    "And again..."
    y "Hey, Koto, I think I hear her phone buzzing somewhere over here."
    y "She might have gone out to do something and forgot it?"
    k "That doesn't sound like her, though..." 
    "Yuri doesn't respond."
    "After a few seconds, I open my mouth to ask Yuri if she's found her phone yet."
    "But I'm stopped by..."
    "{cps=10}... the most horrible scream I've ever heard.{/cps}"
    k "Yuri? Are you okay??"
    "I run as fast as I can to where Yuri sounds like she is, my mother's room."

    #scene 5
    scene bg koto_bedroom
    with dissolve_scene_full
    k "Yu-"
    "I immediately slap my hand over my mouth and try not to scream."
    "My mother is lying on her bed..."
    "And her head is completely detached from her-"
    #scene bg cemetery
    #with dissolve_scene_full
    #play music
    "I don't know how I haven't burst into tears at this point."
    "She's been gone for two weeks now, but it still doesn't feel real."
    "Yuri is silently crying next to me."
    "I haven't seen my father at all since the morning before Mother passed."
    y "Koto?"
    "I look at Yuri and tilt my head slightly."
    y "It's... It's gonna be okay."
    k "I know..."
    "My voice cracks as I say this."
    "The moment finally comes as I bury my face in her shoulder and start sobbing."
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    "You're still more than welcome at our place, if you'd like to stay for a while?"
    "I manage to speak between sobs."
    k "I don't... wanna bother you... or your parents..."
    y "You wouldn't. I promise."
    #play music wah fadein 1.0
    "Neither of us say anything for a while."
    "After I've cried for what feels like a lifetime, I start to calm down."
    k "Lav?"
    y "Yes, Silver?"
    "A smile pulls at my mouth despite the somber moment."
    k "... She knew that I still loved her even if she aggravated the hell out of me, right?"
    "Yuri chuckles a little."
    "She gently lets go of me to meet my eyes."
    "Of course she-"
    #play music wnh
    y "{b}DIDN'T{/b}"
    y "{b}DIDN'T{/b}"
    y "{b}DIDN'T{/b}"
    y "{b}DIDN'T{/b}"
    y "{b}SHE{/b}"
    y "{b}HATED{/b}"
    y "{b}YOU{/b}"
    y "{b}JUST{/b}"
    y "{b}LIKE{/b}"
    y "{b}EVERY{/b}"
    y "{b}ONE{/b}"
    y "{b}ELSE{/b}"
    y "{b}YOU'RE{/b}"
    y "{b}JUST{/b}"
    y "{b}A{/b}"
    y "{b}WHINY{/b}"
    y "{b}IDIOTIC{/b}"
    y "{b}SELFISH{/b}"
    y "{b}BITCH{/b}"
    window hide
    $ nt = 0
    call screen fakeexception

label ch0_breathe:
    scene black
    pause 2.0
    "test"
    return

label ch0_p2:
    scene bg koto_bedroom
    with dissolve_scene_full
    y "Koto, it's nearly time to leave for school."
    "I sigh to myself."
    "I drag myself off of my bed and make my way to the living room."
    scene bg koto_livingroom
    with wipeleft_scene
    show yuri turned happ cm e1a at t11
    y "How are you feeling this morning?"
    k "Eh."
    show yuri turned anno md oe at t11
    y "(That's better than yesterday, at least.)"
    show yuri turned happ cm e1a at t11
    y "Do you have everything ready for school today?"
    k "Yes."
    y "Your homework is finished, too?"
    k "{i}Yes.{/i}"
    show yuri turned neut cm oe at t11
    y "Please don't take that kind of tone with me. You know I'm just-"
    k "Yuri, I don't mean to sound rude but please stop talking like that."
    show yuri turned dist me at t11
    k "You sound exactly like my mother and it still hurts to be rem..."
    k "..."
    show yuri turned happ me b1b e1a at t11
    y "To be reminded of the last time you saw her?"
    k "... Yeah."
    show yuri turned sad cm ce at t11
    y "My apologies."
    y "I'm just really worried about my cousin."
    show yuri turned oe at t11
    y "Especially after you were caring enough to assist me in my first days at Kuribayashi."
    k "Hey, we're family. Of course I'm going to be here to help."
    show yuri turned e1a ma blus at t11
    "Yuri blushes slightly before we walk to school in near silence."
    show yuri at thide
    hide yuri

    #scene 2
    scene bg music_room
    with dissolve_scene_full
    play music wn20
    "I'm sitting alone in front of the piano."
    "I've made a sort of habit of this during my advisory periods lately."
    "For the first time, however, I hear the door open while lost in thought."
    "The sound makes me jump a little, but I quickly regain my composure and..."
    show monika forward nerv mb ce n2 at t11
    m "O-Oh, sorry! I didn't know anyone was going to be in here today."
    "Huh? I'm always..."
    "Wait, how long have I been here? Is the school day already over?"
    k "No need to apologize! I was just leaving."
    "I try my best to sound believable as I stand to grab my belongings."
    show monika forward lsur cm e1a n1 at t11
    m "Wait, I wasn't trying to... to pressure you into leaving or anything!"
    k "Hey, don't worry about it. I usually just relax here during my advisory period."
    k "Somehow, I didn't realize school had already let out."
    show monika forward nerv cm ce at t11
    m "Well... I-If you want, I don't have any problem with you sticking around."
    m "I typically just come here to practice the piano when I don't have too much work to do after school."
    stop music fadeout 2.0
    k "Wait, I feel like I recognize you from somewhere..."
    show monika forward lsur cm e1a at t11
    m "You... do?"
    k "..."
    k "Are you in the debate club by any chance?"
    play music tmonika
    show monika forward happ om oe at t11
    m "I am!"
    k "Ah, so that's why you seem familiar. I'm in debate as well."
    m "Really? I'm surprised I didn't recognize you just now!"
    show monika forward ce
    "We keep talking for a few minutes before I glance at the time."
    k "I should probably be headed home."
    show monika forward happ cm oe at t11
    m "Alright! I guess I'll see you on Saturday..."
    k "Kotonoha. You can call me Koto."
    show monika forward ce at t11
    m "That's such a pretty name."
    "I feel my face starting to turn red."
    k "Thank you... Mi... Mo..."
    show monika forward oe at t11
    m "Do you want me to-"
    k "Monika? Right?"
    show monika forward neut me b2a at t11
    m "Oh-"
    show monika forward neut n3 e1a ma b1a at t11
    m "Yes, that's my name!"
    k "Great. See you Saturday, Monika."
    "I walk down to the front of the{nw}"
    stop music
    $ _skipping = False
    show monika at Glitch(_fps=24.)
    $ renpy.pause (0.75, hard=True)
    scene black
    $ renpy.pause (1.0, hard=True)
    #scene3
    play music t6
    $ renpy.pause (4.5, hard=True)
    show screen player_input_disable
    $ quick_menu = False
    hide screen player_input_disable
    scene bg koto_livingroom
    show yuri glitch2 at t11
    stop music
    y "Where were you??"
    k "Sorry, I ran into somebody from debate."
    y "..."
    show yuri turned neut cm oe at t11
    pause 1.0
    show yuri e4a at t11
    pause 2.0
    show yuri oe at t11
    y "Koto..."
    y "Could you not have at least texted me to inform me that you wouldn't be walking home with me?"
    k "I didn't even know I was-"
    show yuri e4a at t11
    y "I'm aware. But please..."
    y "In the future, give me some kind of heads up if there's even a chance you'll be staying at school late unexpectedly."
    show yuri oe at t11
    y "I-"
    k "Why?"
    k "Why do you {i}have{/i} to know that I'm staying at school an extra five minutes?"
    show yuri turned neut mj oe blus at t11
    y "Because-"
    k "Why do you {i}have{/i} to make sure my homework is done every single day??"
    show yuri e1a at t11
    y "Because-"
    k "Why do you {i}have{/i} to live here with me as soon as-"
    show yuri turned angr cm oe at t11
    y "Because I love you Koto!!"
    y "I'm your cousin! You've helped me so many times when I'm downcast or struggling with panic attacks!"
    y "Why would I not care about you and want to be here for you when you're struggling??"
    k "..."
    k "....."
    show yuri turned lsur om e1a nobl at t11
    y "W-Wait, please don't cry, I'm sorry, I didn't mean to yell, I..."
    "I shake my head as I start tearing up."
    k "It's not... because of your yelling..."
    show yuri turned neut b1c md at t11
    y "What's wrong, then, Koto?"
    k "... I don't deserve you."
    play music t10
    k "I'm standing here, yelling at you like... like the bitch that I am..."
    "Yuri looks like she wants to interject, but apparently decides to let me say everything I want to before speaking up."
    k "I... I'm so used to having pressure from Mother..."
    k "And now that she's... gone, no matter how much I truly loved her... and still love her..."
    k "There's been a sense of relief that..."
    k "... I don't have to be perfect enough for anyone anymore."
    k "That... probably sounds horrible, but it's..."
    k "I don't even know."
    k "But you... a-acting so much like her right now..."
    k "It hurts in ways that... would sound really dumb if I tried to explain."
    k "... You can say what you want to now. I'm done."
    "Yuri takes a step closer to me and grabs my hands gently."
    show yuri turned laug cm e1a at t11
    y "You aren't a bad person by any means."
    y "Just because you get worked up or yell at me doesn't make you horrible."
    y "And you definitely deserve someone who cares about you no matter what."
    show yuri ce at t11
    y "... I know it can feel gross to be relieved for any reason when losing someone."
    y "But it isn't abnormal."
    show yuri e1a at t11
    y "And I realize it can be... difficult, to say the least, to describe feelings like these."
    y "But I think I have something that might help at least a little."
    show yuri at thide
    hide yuri
    "Yuri pulls out a notebook, flipping to a blank page."
    "She pulls a pen out as well before handing both to me."
    y "I'm assuming you haven't written a poem in at least several years..."
    y "So what I had in mind was at least writing a few words that mean something to you."
    y "They can relate to things you're feeling, memories from your past..."
    y "Just a few words that mean something to you."
    "I take the pen and look up at Yuri."
    return

    






label cred:
    #play music
    show text "Written and Directed by cpcantimark" with dissolve_scene_half
    pause 2.0
    hide text with fade
    show text "Music by cpcantimark, inspired by music from Dan Salvato" with dissolve_scene_half
    pause 2.0
    hide text with fade
    show text "Programmed by Chino" with dissolve_scene_half
    pause 2.0
    hide text with fade
    show text "Custom backgrounds by " with dissolve_scene_half
    pause 2.0
    hide text with fade
    show text "Glitched Yuri sprite created by " with dissolve_scene_half
    pause 2.0
    hide text with fade
    show text "I hope you have a great rest of your day!" with dissolve_scene_half
    pause 4.0
    hide text with fade
    show text "No one is ever too tainted to save." with dissolve_scene_half
    play sound wnh
    pause 3.0
    hide text with fade





   