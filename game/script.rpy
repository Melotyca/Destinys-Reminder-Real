﻿# The script of the game goes in this file.

#Characters
define d = Character("Destiny", color="#1db78b", what_color="#58deb8")
define d_t = Character("Destiny", color="#1db78b", what_italic=True, what_color="#618a7f")
define g = Character("Gabriel", color="#AED628", what_color="#cae66d")
define m = Character("Matthew", color="#639af9", what_color="#98baf7")
define s = Character("Simon", color= "#ff6961", what_color="#ff9e98")
define x = Character("?", color="#7b7b7b", what_italic=True )
define k = Character("Kai", color="#7b7b7b", what_color="#bebebe")

#Variables
default fix_printer = False
default dinner_plans = False
default open_door = False
default call_police = False


# The game starts here.

label start:
#DAY 1
    label day1:
        label dream1:
            scene bg_black
            show girl
            x "Destiny..."
            x "Destiny!"
            x "You have to listen to me."
            x "Something bad is going to happen."
            x "Please."
            x "Don't trust him. You're in danger"
            x "I can help you."
            hide girl 
        
        label morning1:
            "Ping!"
            d_t "Who, What was that?"
            d_t "{i}Ugh{/i} What time is it? It feels like I've only just fallen asleep."
            scene bg_d_window
            show phone  
            # (phone appears(see Her reminder Project due tomorrow, Day and time: Mon 07:13). 
            d_t "Oh come on. Just let me sleep."  
            d_t "Why can't it be like 4am."
            d_t "Pleaseee... If I stay in bed now I'll be late."
            d_t "I guess I've got no other choice."  
            d_t "Coffee time!"   

            scene bg_d_kitchen
            d_t "Oh boy. I really need to get more sleep today." 
            d_t "I shouldn't have stayed up so late yesterday. What time is Gabe going to be here again?"
            d_t "Didn't he say he was going to text me?"
            #(phone appears, time now 07:30)
            #unlock)   
            show phone
            #(home screen, a couple apps, no notifications waits a little). 
            #(gets a message from Gabriel (Omw! Hope you didn’t overseep again ;))). 
            d_t "Shoot! I totaly forgot about time!"
            d_t "I have to get ready."  
            #(destiny looks around, window, corridor back to kitchen/messy).
            hide phone
            d_t "Jeez, I really need to clean this mess up soon. How did my room become this messy again so fast." 
            d_t "When did I even wear that shirt? God even my desk is filled."
            d_t "Actually, I don't think I've ever seen that screen of Achievements over there."
            d_t "Wait."
            d_t "ACHEIVMENTS!?"   
            #(background gets a bit darker as Achievements stand out.). 
            d_t "What in the-"   

            show achievements
            d  "Heh. Heh he..."  
            d_t "A display. Really?"  
            d_t "Oh god. No more games before bed."
            d_t "What's next. Some NPC walks through my door? As if."
            d_t "This can't be serio-" 
            "{i}Knock knock.{/i}" 
            d "AH!" 
            hide achievements
            #(cup falls and shatters and spills). 
            #(shattered mug). 
            g "It's me, Gabe. Is everything alright in there?"   
            d "Yes yes! On my way."
            #door opens
            scene bg_d_corridor 
            show gabe_conc
            g "I'm sorry. I didn't mean to startle you"  
            d "No, no. It's fine! I just. Uhm. Didn't expect you yet."  
            d_t "Oh god this shirt is ruined."
            hide gabe_conc
            show gabe_happy 
            g "Well then, the usual Destiny then." 
            hide gabe_happy
            show gabe_conf
            g "But are you sure you're alright Destiny? You look a little shaken."  
            d "Oh, shut it. You almost scared me to death." 
            hide gabe_conf
            show gabe_neut
            d "I still have to get ready. Make yourself at home."  

            scene bg_d_kitchen
            d "Please just ignore the mess. I'm working on it I promise." 
            d "Oh and don't bother with the mug. I'll clean it up later too."  
            show gabe_conc
            g "Oh no not the chipmunk mug." 
            hide gabe_conc
            show gabe_neut
            g "I really liked that one. I think your mom gave you that right?"  
            d "Mhm. Must've been easter or something like that."  
            d_t "Shoot! What am I going to wear now?"  
            #Narrator: Destiny starts rummaging through her room. 
            g "I don't mind cleaning up a bit. I'll just take care of these shards if that's allright."  
            d "Yes! Found it!" 
            d "Give me a second to throw this on."  
            #(blackspace). 
            hide gabe_neut
            show gabe_happy
            g "{i}*chuckle*{/i}. No worries, I'll just go ahead and do it." 
            g "Besides, our bus leaves in 20 minutes."  
            d "I'll be quick!"  

            scene bg_d_bathroom
            #(Destiny in the mirror, dishevelled).
            show destiny_neut 
            d_t "Let's see how this fits." 
            d_t "Anything it better than this desaster right now."
            d_t "Jeez its worse than I thought. The coffee really went everywhere."
            d_t "Better tidy this mess of a haircut up a bit too while I'm at it."
            d_t "I have to find a brush."
            #looks around
            "!" 
            d_t "That screen's still here!? Did it seriously follow me?"
            d_t "What even is that. I can't touch it. Just text."
            d_t "It's saying something about a Stain."
            d_t "Hah! What a coincidence!"
            d_t "Kinda ceepy though..."
            d_t "Wasn't that text there before I even spilled my mug? But why would that be an achievemnt?"
            d_t "Oh no I'm officially going insane."  
            d_t "I really should have slept longer. Maybe the last couple of all-nighters are starting to get to me."
            d_t "Although."
            d_t "Achievements..."
            d_t "Let's see."
            d_t "Yeah, I do think that stain is stying. But what could the other ones mean?"
            menu: 
                "Under his watch.":
                    jump underhiswatch
                
                "This food is flipping good.":
                    jump flippinggood

                "Jam on!":
                    jump jamon

                "Comforting stroll":
                    jump comfortingstroll  

            label underhiswatch:
                d_t "\"{i}Under his watch{/i}\" Oh doesn't this just sound dandy. Who could be watching me?"
                jump gotowork

            label flippinggood:
                d_t "\"{i}This food is flipping good.{/i}\" Hey if this really predicts the future than atleast the food will be good."
                jump gotowork

            label jamon:
                d_t "\"{i}Jam on!{/i}\" Jam? As in music? Does this mean I'll hear some good music?"
                jump gotowork

            label comfortingstroll:
                d_t "\"{i}Comforting stroll.{/i}\" Eh I doubt it. As if I'd freely choose to go for a walk."
                jump gotowork
                            
        label gotowork:    
            d_t "Hmm. What about the rest-"
            g "Destiny!"
            g "Where's the bin? I can't find it anywhere."  
            d_t "Shoot! I have to hurry."  
            d "It's next to the counter. Be there in a second!"  

            scene bg_d_kitchen
            show gabe_neut
            g "Ready to go?"  
            d "Yes! Sorry for the wait."  
            g "No worries."
            g "We've got enough time. Besides we've got a long enough day ahead of us."
            g "Do you think you'll get done with your design today?" 
            d_t "Oh right. I'm supposed to finish the design for that ad poser this week."  
            d "Hah.. we'll see."
            d "Something's just not right about it yet but I can't figure out what."
            d "And Matt just gave that speach last meeting about being stricter with deadlines and quality from now on." 
            d "Im screwed."  
            g "Don't be too hard on yourself Destiny."
            g "You've always found a way to get things done till now."  
            d "Yeah like a day past the due date." 
            hide gabe_neut
            show gabe_happy 
            g "Oh come on, good work takes time."
            hide gabe_happy
            show gabe_neut
            g "How did he say it? {i}ehem \"As one of the most promising companies in our field, we don't tolerate rushed or unfinished work Sullivan!\"{/i}" 
            g "I can't believe he still refuses to use our firstnames."
            g "I seriously doubt he's ever heard himself speak." 
            d "HAHA! That was scarily accurate. Have you secretly been practicing?"
            g "Yeah right!"
            d "Hey who knows. But yeah, you're right. Thank you Gabe."
            g "Now let's get going." 
            g "Before we actually end up being late." 
            jump Work1 

        label Work1:
            scene bg_office_computer
            d_t "And yet another conspiracy theory..."
            d_t "How obsessed with a movie can you be? \"Watch out! it's the Matrix trying to get you to wake up!\" As if."
            d_t "Is there seriously nothing useful on the internet about something like this?"
            d_t "This can't just be me imagining things. I mean it knew I was going to stain my shirt."
            d_t "I wouldn't even know that myself. Besides none of these dumb theories explain how I can SEE this thing."
            d_t "It's still there..."
            d_t "Maybe it's a hallucination? I have been staring at screens a lot lately. And the lack of sleep definetely isn't helping either."
            d_t "Maybe I should go see a doctor..."
            d_t "I'm sure there has to be logical explanation for all of this."
            d_t "Maybe it'll just go away. It's starting to creep me out a bit. I'm sure if I just get enough rest tonight it will be fine."
            d_t "Who knows. It might even go away during the day!"
            "..."
            d_t "But what if it doesn't?"
            d_t "Come on internet do me a solid won't you?"
            #keeps clicking through
            d_t "I'm not being unreasonable. I'm sure someone has had this before. I just need to search harder."
            d_t "\"Electomagnetic transmissions\"... Possible. What do they say about seeing text?"
            m "Sullivan!"
            d "What!?"

            scene bg_office_hallway
            show matt_neut
            d_t "Oh shoot. How did I not see him coming."   
            d "Y- Yes? Oh, g- good morning Matthew."  
            m "What website is that?"
            d "Huh?"
            m "I don't remember \"bumming around on forums for conspiracy theorists\" being in your job description."
            d_t "Crap."
            d "Oh that? No, s-sorry I was just taking a quick break."
            m "Does this mean you've finally finished the Poster?"
            m "It'd better be. We can't have you hand in another Project late."
            m "Or last minute like last time. It's still a miracle to me how you somehow managed to get that one printed in time."
            m "Make sure you're ready ahead of time. I'd highly suggest you print an example latest tomorrow. So we can show it to our clients in time."
            m "Although, today would be much better..."
            d "Sorry..."
            m "Oh, And Sullivan" 
            d "Yes?"
            m "With tomorrow I don't mean 6:30PM. The office closes at 7:00. If it's not printed by then, then you have to figure out how to print it."
            m "Is that undersood?"
            d "Yes. Of course. I'll have it in time this time."
            m "Great! Now to other matters."
            m "I'd like to propose a promising business opportunity to you. And lord knows you need one of those."
            m "Two of them actually, now that I think about it."
            m "Today must be your lucky day."
            d_t "Ugh. What does he want now."
            m "Firstly, I'd like to introduce you to one of our team leaders Simon."
            d_t "Oh?"
            m "He's looking for someone to fill for someone that left in their current project."
            m "The woman that was previously in charge of design seems to have quit unexpectedly."
            m "I suggested some great options, but Simon mentioned you as a possible replacement."
            m "Whatever his reasons might be."
            m "So What do you say Sullivan? The desicion is quite obvious in my oppinion."
            m "I will send you the application forms later this afternoon if you decide to take this-, how do I put it..."
            m "{i}Rather rare opportunity.{/i}"
            d "Yes! Of course! Should I go talk to him right now?"
            m "No need. I have some files I need to run by him anyways. We can go by his office together afterwards."
            d "Toghether?"
            m "Yes, which brings me to my second proposal."
            d_t "Oh no here we go."
            m "I would like to invite you to lunch. To talk about some things regarding your current project."
            d_t "What?"
            d "Uhm. Lunch? You want to go eat lunch with me?"
            m "Yes. Down at the cafeteria."
            m "I thought this would be a wonderful opportunity to have a nice talk about the problems you seem to be having with this poster."
            menu:
                "No no it's going fine. I was just taking a break.":
                    jump mattlunch_n

                "Oh, sure...": 
                    jump mattlunch_y 
            
        label mattlunch_y:
            m "Wonderfull. I heard today's menu would offer something special."
            "..."
            d "OH! You meant right now?"
            d "Yes! One second please. I need to. Uhm, finish some last tweeks and save my project really quickly."
            m "Alright. I'll just go ahead. Come meet me in the Cafeteria when you're done"
            d_t "How does he always catch me in the worst moments possible. And here I was looking forward to lunch with gabe and the others"
            d_t "Oh yeah, didn't that screen also say something about food?"
            jump mattlunch

        label mattlunch_n:
            m "I'm not really asking Sullivan."
            m "I need to speak with you. Not only about your design."
            d "Sorry. Yes of course. Uhm, I need to finish some last tweeks and save my project. But after that I'll come right away."
            m "Fine. I'll just go ahead. Come meet me in the Cafeteria when you're done. Don't make me wait too long. I heard todays menu is promising"
            d_t "How does he always catch me in the worst moments possible. And here I was looking forward to lunch with gabe and the others"
            d_t "Oh yeah, didn't that screen also say something about food?"
            jump mattlunch

        label mattlunch:
            scene bg_office_cafeteria
            d "Mushrooms and mashed potatoes."
            m "Looks great doesn't it!"
            d "Yeah..."
            m "Being fussy about the food Sullivan?"
            d "No no. It looks delicious. I just had to uhm, figure out what it was first..."
            d_t "God I hate mushrooms."
            m "So, Sullivan. This Poster you're working on. How is it coming along? Do you know if you will be done on time?"
            menu: 
                "It's going great!":
                    d "Oh yeah, It's going great haha. I'm s-sorry about before. I'm actually almost done."
                    d_t "Please just don't ask about specifics"
                    d "I just have one or two more little graphics to make. And maybe some last minute text editing."
                    m "Will you be able to have it done today? So it can be printed tomorrow. "
                    m "I would really prefer you finish it today, so we don't have another situation like last time."
                    m "But with the pace you're working at it looks like you won't be able to finish today. "
                    d "No... I'm sorry."
                    d "I'll have it tomorrow evening. Promised"

                "About that...":
                    d "Yeah, about that. I don't think I'll be able to finish it today."
                    d "I'll have it in time. I promise. But I've been having some difficulty with the programm lately"
                    m "I would have really prefered you finish it today. Just make sure we don't have another situation like last time."
                    d "Yes I promise."

            m "I hope you can keep that promise."
            "..."
            m "Is something the matter with your plate? You've been poking around in it like you're trying to excavate something."
            m "{i} It's starting to make me nervous.{/i}"
            d "S-sorry. I'll stop."
            m "Fine. With that settled, I would like to talk to you about this new Job Simon is offering you."
            m "As I mentioned earlier. Someone from his team quit unexpectedly just last week. They are still in the midst of finishing an important project at the moment."
            m "Along with the marketing side of things the clients also requested designs for their upcoming business concept."
            m "But with the person in charge of design gone they have really been struggling to pull everything together."
            m "Since the deadline set by the client is in 2 weeks they desperately need someone to fill her place."
            m "And since you will be done with your poster soon. {i}I hope{/i}. You'd be a good candidate to take the offer."
            m "I have to admit, I'm not too keen on you switching teams already. But I guess after one year you've had enough time to get into the swing of things here."
            m "So, Sullivan. Since you already agreed to taking this opportunity I hope you do your best to adjust to their work flow quickly."
            d "I'll give it my all."
            m "Good. Simon will be happy to hear I've found someone."
            m "Unlike me, Simon expects a lot more autonomy of his team." 
            d_t "Thank god. Finally some freedom. I can't deal with another controll freak like Matt."
            m "I was reluctant to offer you this position since it seems you still need the supervision. But it can't be helped."
            m "Most of the other viable designers are quite busy with their own projects at the moment."
            m "I hope you step up to the demand and deliver as demanded."
            m "I don't want you to make a bad impression on his team. I'm sure you understand that that would also have very undesirable concequences on my side."
            d "I understand. I won't dissapoint you Matthew. I'm sure having a new work environment will be a great experience for me."
            m "Are you saying you don't like my way of doing things?"
            d "No of course not! I just meant it will be good for me to also get a look into how other teams do it around here."
            m "Alright. If you say so."
            m "You don't seem to be hungry today do you."
            d "Yeahhh, I dont' have that big of an apetite right now."
            d_t "This is so uncomfortable why did he have to do this over lunch."
            m "There's no shame in addmiting you don't like mushrooms Sullivan. Not like your face does't give it away everytime you bite down on one."
            d "He he... Sorry. I just can't stand the texture. I think I'll just get up and go and get myse- oh no!"
            "Clank!"
            #The plate flips
            d "I- I'm so sorry Matt..."
            d "Oh no I didn't mean to-"
            m "How-"
            d "I'm sorry I have to go!"
            #Destiny runs away
            #HAVE TO CONTINUE
        label printer1:
            scene bg_office_computer
            #later during the day
            d_t "URGH that was so stupid! Why did I just run away!"
            d_t "God Matt is going to hate me even more now. If that's even possible."
            d_t "I didn't get to talk to Simon."
            d_t "I hope Matt didn't change his mind about it."
            d_t "Oh god. What if he told Simon I wasn't a good match."
            d_t "I have to print and give him the forms as soon as possible!"
            #see time
            d_t "I can't believe it's this late already. This day has been a disaster."
            d_t "Let's just print this application and get it over with."
            #goes to printer
            scene bg_office_printer
            d_t "These weird achievements have been messing with my head the entire day. Can't they be a little clearer?"
            d_t "If I'd known I was supposed to take them so litterally I would have been more careful with my food."
            d_t "Flipping good. Don't make me laugh. This whole thing could've been avoided."
            d_t "Matts never going to forgive me for that."
            d_t "What's next? Jam on."
            d_t "I swear, if this stupid screen is going to make me spill jam on myself I'm going to lose it."
            d_t "I don't need another stai-"
            "{i}krrrt!{/i}"
            d_t "What was that?"
        #shows error message 
            d_t "Oh no."
            d_t "No no no"
            d_t "Not this too"
            d_t "This can't be happening to me right now!"
            d_t "Of all the people you could have failed on you just had to choose me?"
            d "Urgh! Stupid printer!"
            "BAMM"
            d_t "Damn it. I jammed it"
            "..."
            d_t "Jammed..."
            "..."
            d_t "OH! You little-."
            d_t "Jam on! I get it now."
            d_t "What on earth is this?! How the hell did it know that?"
            d_t "How does this keep happening?"
            d_t "First the stain then lunch and now this?"
            d_t "I can't just be imagining this anymore."
            d_t "I bet you think you're funny right now don't you, you stupid screen!"
            d_t "If you already decide to make my life a living nightmare just be direct about it."
            d_t "\"Jam on\". \"Flipping good\". Why does everything have to have multiple meanings."
            d_t "And why does it always have to be the worst one that comes true!"
            d_t "Come on. Relax Destiny. Maybe It's not all for nothing."
            d_t "Maybe it still printed some of the pages."
            d_t "Of course."
            d_t "None of them. Why did I think anything would go in favor today."
            d_t "And I can't even get the paperchute to open."
            d_t "I don't think I can fix this myself..."
            menu: 
                "Get help to fix the printer.":
                    $ fix_printer = True
                    d_t "I have to find someone to help me fix this darn printer"
                    scene bg_office_hallway
                    #goes to look for someone runns into simon
                    s "Oh! You're Destiny right!"
                    s "I thought Matthew said we would meet after lunch. Did something come up?"
                    d "You're Simon then! Yeah sorry about that."
                    d "Uhm, yes."
                    d "Something came up."
                    s "What are you doing around here? Can I help you with anything?"
                    d "Yes actually."
                    menu:
                        "I jammed the printer":
                            d "I was about to print the forms to join your team but I must have put in too much paper."
                            d "Now it won't do anything anymore. I think I must've jammed it."
                        "Someone jammed the printer":
                            d "I was about to print the forms to join your team but someone must have put in too much paper."
                            d "There's an error message. I think someone must've jammed it."
                    d "Do you know who I could go to to help me fix it?"
                    s "Not that old printer again! We should have replaced that ancient thing years ago."
                    s "Wait I'll help you out. I've had my fair share of unfortunate encounters with that one. Let's go have a look at it."
                    scene bg_office_printer
                    s "I think I know how to get it running again."
                    d "Wow, Thank you so much Simon! You're a real life saver."
                    s "Oh don't be like that. It's the least I can do now that I know we'll finally have someone to take Kai's place."
                    d "Kai?"
                    s "No one knows why she would just quit so out of the blue. Especially since we are still in the middle of a project at the moment. "
                    s "She was always so passionate about what she did. Something important must have come up..."
                    s "Anyhow. We can only speculate. But I'm glad we have you to help us out soon now!"
                    s "We've really been struggling without her around."
                    s "I'm looking forward to working with you."
                    d "Me too!"
                    d_t "Anything beats Matt."
                    s "I heard you're still finishing up a project right now?"
                    d "It's nothing big but I got tasked with designing an ad poster, yes."
                    d "I'll most likely be done by tomorrow though."
                    s "Well then. We'll be collaborating from then on!"
                    s "Now let me help you with that printer. I don't want to keep you here any longer than necessary."
                    #simon helps destiny
                    s "My appolagies! That took a little longer than expected."
                    s "I'm curious now. Not many people would be willing to stay this late." 
                    s "But since I live close by it's not a problem for me to stay a little longer."
                    s "Do you live somewhere around here too?"
                    d "Yeah. I live just two stops away from here. So I don't have a long commute at all."
                    s "Do you like the area? In my oppinion it's one of the best if you work in the city."
                    d "Mostly yeah. I really lucked out with my appartment."
                    d "Not too far and a great view as well."
                    s "Wow, you must be in one of the newer ones close to the park then! I've heard only great things about them."
                    s "You've been working here for a year now am I right?"
                    d "Yeah. One and a quarter actually. But I haven't really had the chance to work on any big projects yet."
                    s "Matthew tends to be a bit too careful with handing out jobs"
                    s "In my oppinion the only way to get experience is to do the thing you want to learn."
                    s "Is view on the matter seems to be a bit more uptight."
                    d "A little yes haha."
                    s "Well then this will be a good new experience for you!"
                    s "You said you'll be on it tomorrow right?"
                    d "Yes. I'll make sure to fill this out and submit it by tomorrow night."
                    s "Excellent!"
                    "RING!"
                    d "Sorry! That must be Gabriel. I have to go. I'm running late to meet my friend."
                    d "Thank you so much for helping me with the printer!"
                    s "Of course. I'm glad I was able to help."
                    s "See you around Destiny."
                    d "Have a nice evening!"
                    jump stroll
                    
                "Leave it and go home.":
                    $ fix_printer = False
                    d_t "Oh screw this. I don't have the nerve to deal with this right now."
                    d_t "Someone else will have to fix it."
                    d_t "I bet Gabriel's already waiting for me. I can just print this out tomorrow."
                    d_t "It's not like I'll be done with the poster before then anyways."
                    d_t "I can print those together. I don't want to make Gabe wait for too long."
                    jump stroll

        label stroll:
            scene bg_office_cafeteria
            g "There you are! What took so long? Did Matt catch you on your way out? I heard what happened over lunch."
            d "Thankfully not. No, I don't think I'd be alive right now if that happened"
            g "I think Matt would have crucified you right on the spot."
            g "Did you stay longer to finish your project?"
            d "No, I still have to work on it tomorrow. I had some trouble with the printer"
            if fix_printer==True:
                d "It Jammed and I had to find someone to help me print the forms I need to finally escape Matt."
            else:
                d "It Jammed so I couldn't print the forms to join that new team."
            g "Did you use the old one in the back on floor 3?"
            d "Yeah, why? I've never had troubles with it so far."
            g "Wow you must have had insane luck then. That one is known for eating paper like it's been starving for the last decade."
            d "Huh. I guess I just got lucky up until now."
            d "But I guess that luck has run out now."
            d "Let's just get going. I want to keep the chances of running into Matt or anyone was there to witness happened today to a low."
            g "Do you want to take the long or the short route?"
            menu:
                "Take the long way.":
                    d "I want to go the long way. I need some movement to clear my head."
                    d_t "If that screen is to trust just this once this stroll will be nice."
                    g "The long one it is then."
                "Take the short way.":
                    d "The short one please. I just want to get home after today."
                    d_t "With that screen mentioning the stroll, I don't think I can trust it."
                    g "The short one it is then."
            scene bg_street
            g "How was your day, if we ignore the obvious fopa at lunch?"
            d "It was fine. I didn't get to work on the poster as much as I'd liked though. I have a lot to do tomorrow."
            g "Why's that? Did something come up? I thought you kept your scedule as free as possible specifically to be able to work on it a lot today."
            d "It's not that. I didn't have anything else planned."
            d "I just wasn't able to focus at all."
            d "My thoughts were all over the place the entire day. Just never on work."
            g "Got something on your mind Destiny? If there's something bothering you maybe talking anout it will help."
            d_t "Can I tell him about the screen?"
            menu: 
                "Tell him":
                    d "Have you ever started seeing things from looking at screens too much?"
                    g "What do you mean? Like hallucinations?"
                    d "Yeah. Like a screen with legitemate text."
                    g "What!?"
                    g "Have you been hallucinating.?"
                    d "Maybe?"
                    g "Destiny, I think you seriously need to get some rest. You've been overworking yourself too much."
                    g "Staring at that screen all day every day can't be good for you."
                    g "When was the last time you've taken a day off or just slept for a solid 8 hours?"
                    d "..."
                    d "Quite a while ago..."
                    g "Okay. Why don't we make sure you get home a little earlier today and get a good night of sleep."        
                    g "I'm sure you're just overworked and maybe also a bit dehydrated. Did you have enough water today."
                    d "Now that I think about it, no I haven't really had too much to drink today."
                    d_t "But the screen was there even in the morning."
                    g "See. I'm sure you'll feel better once you take a small break and have something to drink."
                    g "And please make sure to go see a doctor if it gets worse, alright?"
                    

                "Be dismissive":
                    d "I think I might have just not slept enough."
                    d "Usually runnign on little sleep isn't a problem for me but this Project has been keeping me up more nights than I'd like"
                    g "Sounds to me like you're overworking yourself."
                    g "When was the last time you've taken a day off or just slept for a solid 8 hours?"
                    d "..."
                    d "Quite a while ago..."
                    g "Okay. Why don't we make sure you get home a little earlier today and get a good night of sleep."        
                    g "Maybe you're also a bit dehydrated. Did you have enough water today."
                    d "Now that I think about it, no I haven't really had too much to drink today."
                    g "I'm sure you'll feel better once you take a small break and have something to drink."

            g "We can't have you getting sick from working too much now can we?"
            d "Thank you Gabe."
            g "Just tell if there's something I can do for you. You can call me whenever."
            g "Oh! Looks like we're on our street already."
            g "Time really flew by us this time didn't it!"
            d "Here already? Wow."
            g "We must've been walking extra fast. But now go and get some sleep."
            g "And don't so much about tomorrow. I'm sure you'll get everything done on time."
            d "See you tomorrow Gabriel."
            g "See you tomorrow!"
                
        label evening1:
            jump day2
        

#DAY 2
    label day2:
        label dream2:
            scene bg_black
            x "Please Destiny I'm trying to help you. You have to listen to me"
            x "I'm not an illusion. I'm here to help you."
            x "It doesn't have to happen to you too."
            x "I know what is going to happen now. I couldn't stop it myself but you can."
            x "He's after you now. You have to remember."
            x "Do-* 4jT F0-_r g*3 T"
            jump morning2
        label morning2:
            scene bg_d_window
            d_t "What-"
            d_t "Why does this feel so familiar. It feels like I'm having a dejavu"
            d_t "Didn't I have that same strange dream yesterday?"
            d_t "Arrgh. Why can't I remember. My head feels like it's spinning."
            d_t "I have to go get something to drink. What time is it even?"
            # (phone appears(see Her reminder Project due today, Day and time: Tue 06:23). 
            d_t "Whoa. That's unusually early. No wonder my head feels like a truck ran over it."
            d_t "So much for getting more sleep today. I still have almost an hour until I have to get up."
            d_t "But I doubt I'll be able to ignore this headache and go back to sleep. I have to go get a glass of water"
            #gets up
            d_t "Seriously!?"
            d_t "That screen is still here!"
            d_t "Wait! It's changed. There's different achievements today."
            d_t "This can't just be from over working myself anymore."
            d_t "The screen that's always there but even worse all of the achievements came true somehow"
            d_t "It looks exactly the same as yesterday except for the text."
            d_t "What does it say this time?"
            show achievements
            #screen
            d_t "I was hoping it would just go away overnight."
            d_t "Clearly that was too optimistic of me."
            d_t "But they did all come true didn't they?"
            d_t "Maybe if I can figure out what they actually mean beforehand I'll be able to avoid ruining my day unlike yesterday."
            d_t "Let's see. They happened in the order they were writen in right?"
            d_t "What does my looming spector have to say about today?"
            label achievements2: 
                menu:
                    "\"Stick the landing\"":
                        d_t "Stick the landing. Hmm..."
                        d_t "The first thing today."
                        d_t "What landing is there to stick?"
                        d_t ""
                        d_t "If "

                    "\"We meet again old foe\"":
                        d_t "Here we go. The second one and this sounds great already. {i}Old foe{/i}. What could it mean by foe?"
                        d_t "And an old one? The only foe I have right now that I could think of has to be Matthew."
                        d_t "But I wouldn't really call him a foe. We just don't really see eye to eye."
                        d_t "He does seem to have it out for me. Why does he always have to be there whenever something goes wrong."
                        d_t "God I hope he doesn't bring up that fiasco from yesterday."
                        d_t "But I can prepare a bit now."
                        d_t "In the case I really will run into Matt today unexpectedly it certainly wouldn't hurt to know what to say."
                        d_t "Hmm what would be a good excuse for drenching him in stew. That won't "

                    "\"Running, my new hobby!\"":
                        d_t "Yeah right. Now it's just being unrealistic."
                        d_t "The last thing I want to do is go for a run today."
                        d_t "Does this mean I'll be late for something? I don't have anything planned yet other than finishing my poster."
                        d_t "Maybe I'll be late to printing again. I can't miss the deadline today. I'd better keep a close eye on the time today."
                        d_t "Let's see maybe I can avoid it? Even if not, at least I know now that I'll probably have to run at some point today."
                        d_t "I don't think I'll be enjoying running though, that's for sure. {i}New hobby{/i} yeah right."
                        d_t "I don't know if I can really believe that but I'll definetely put on some more comfortable shoes today."
                        jump achievements2

                    "\"Dinner for two\"":
                        d_t "dinner for two"
                     
                    "\"Knock Knock\"":
                        d_t "Let's hope this is refering to a door. Maybe I'm getting a package delivered."
                        d_t "Did I order anything recently?"
                        d_t "Hmmm. Maybe it's my new coffee machine. It's about time that arrived."
                        d_t "I've been starting to think they straight up just lost the package."
                        d_t "It's supposed to happen pretty late in the day though. Maybe it's not the mail."
                        d_t "Could someone be coming to visit?"
                        d_t "Ugh. Is it going to be doordashers?"
                        d_t "Well, I don't think that would be significant enough to be on here."
                        d_t "Maybe I'll be visiting someone."
                        d_t "Not that I'm planning to right now..."
                        
                    "Finish checking achievements":
                        return
            d_t "I can prepare a little more than yesterday. Still, they're as unclear as yesterday"
            jump work2
        label work2:
            if fix_printer == True:
                jump printer2fixed
            else:
                jump printer2unfixed
        label printer2fixed:
            jump running
        label printer2unfixed:
            jump running
        label running:
            if dinner_plans== True:
                jump dinnerfor2gabe
            else:
                jump dinnerfor2dog
        label dinnerfor2gabe:
            jump day3
        label dinnerfor2dog:
            menu:
                "Open the door.":
                    $ open_door= True
                "Keep it closed"
            jump day3

#DAY 3
    label day3:
        label dream3:
            jump morning3
        label morning3: 
            if dinner_plans==False:
                menu:
                    "Call Gabriel.":
                        jump callgabealone
                    "Call the police.":
                        $ call_police= True
                        jump call_police
                    

            else:
                jump callgabedinner
        label callgabedinner:
            jump work3
        label callgabealone:
            jump work3
        label callpolice:
            jump work3
        label work3:
            if call_police==True:
                jump partypolice
            else:
                jump party
        label party:
            jump simonconvo
        label partypolice:
            jump simonconvo
        label simonconvo:
            if dinner_plans== True:
                jump simonevaded
            else:
                if open_door== True and call_police==True:
                    jump simonmad
                elif open_door== True and call_police==False:
                    jump simoncreepy
                elif open_door== False and call_police==True:
                    jump simonmad
                elif open_door== False and call_police==False:
                    jump simonevaded
        label simonevaded:
        label simonmad:
        label simoncreepy:
    
    label day4:


    

    # This ends the game.

    return
