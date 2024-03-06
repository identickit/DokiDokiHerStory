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
    km "What did you do to yourself now?"
    k "Huh?"
    km "Don't {i}'Huh?'{/i} me!"
    km "Did you think I wasn't going to notice your hand?"
    "I briefly hold up my hand and flex my wounded finger a bit."
    k "D-Don't worry, mother! It isn't serious."
    km "Of course it isn't. It doesn't have to be a major injury, as long as your friends at school can see it, right?"
    kf "Noriko, dear... Koto has obviously grown since the last time she acted how you're implying."
    km "Don't you dare try to get her off the hook!"
    km "Why else would she be hurt like this?"
    "I almost open my mouth to retort, but there's no way I can admit that I broke grandmother's watch."
    "I just stand in front of my mother, hoping that she doesn't take it any further."
    kf "Look, honey: As long as she's not seriously hurt, there shouldn't be anything to worry about."
    kf "I trust her."
    km "... {i}Fine{/i}"
    km "Go make yourself some breakfast and then get ready for school."
    km "You are {i}not{/i} arriving late again."
    kf "Noriko, she was feeling ill the morning she-"
    km "Don't push it, Saruka."
    "I quickly head to the kitchen to prepare my food before they get into it again."
    ##scene 2
    scene bg cafeteria
    with dissolve_scene_full
    play music wok
    k "Mother's gonna to kill me for sure now."
    y "I'm sure whaterver it is isn't as bad as it seems."
    k "I got an 84 on my Chemistry exam."
    y "..."
    y "Okay, that's admittedly pretty bad."
    y "Not the grade, of course. I personally believe your grades aren't prefect reflections-"
    k "-of your true potential. I know. You always see the best in everyone."
    k "I love you for that."
    y "A gentle reminder that I'm your cousin, dear Koto."
    k "What do you mean-"
    k "Oh."
    "I chuckle a little at her joke. She can be pretty funny when she wants to be."
    y "Anyways, I'm sure your father will be understanding?"
    k "Yeah... He's always had my back, hasn't he?"
    k "... Reminds me of when we were little and he took us both to the mall."
    k "We knocked over those mannequins and covered for us when Mother saw the resulting scene."
    "I laugh to myself for a minute before noticing the look on my cousin's face."
    y "..."
    y "I haven't heard you laugh in so long."
    k "C'mon, surely it hasn't been..."
    "..."
    "I feel my face burn up a little."
    "I genuinely can't remember the last time I had a good laugh."
    y "You don't have to be prefect, Koto. No matter what she says."
    y "There's people out there who will always see how incredible and irreplaceable you are."
    k "Yuri..."
    #bell ringing sfx
    "The bell rings, signaling the end of our lunch period."
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
    with wipeleft
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
    y "Hello, dear cousin."
    y "I just wanted to..."
    y "Are you feeling okay? You look rather anxious."
    k "Yuri, are my parents out with yours right now?"
    y "Koto, they went out last week. They only go out once a month, don't they?"
    k "... So that's a no?"
    y "Indeed."
    y "..."
    "Apparently I look even more anxious now, because Yuri's expression changes to one of concern."
    y "What's wrong?"
    k "I don't think they're here."
    y "They aren't?"
    y "From what you've told me before-"
    k "Yes, they're usually here right now."
    k "And I-"
    y "Hey..."
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
    y "Maybe... try again?"
    "I redial..."
    "..."
    "Still no answer."
    "I make a small sound that sounds awfully similar to when I lost my parents once when I was much younger."
    y "How about I look to see if they're here and just aren't answering for some reason?"
    "I nod slightly."
    #yuri sprite disappear
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





   