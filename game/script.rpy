# The script of the game goes in this file.

#Characters
define d = Character("Destiny", color="#1db78b", what_color="#58deb8")
define d_t = Character("Destiny", color="#1db78b", what_italic=True, what_color="#618a7f")
define g = Character("Gabriel", color="#AED628", what_color="#cae66d")
define m = Character("Matthew", color="#639af9", what_color="#98baf7")
define s = Character("Simon", color= "#ff6961", what_color="#ff9e98")
define x = Character("?", color="#7b7b7b", what_italic=True )
define k = Character("Kai", color="#7b7b7b", what_color="#bebebe")
define c = Character("Cat", color="#7b7b7b", what_color="#bebebe" )
define c_n = Character("[catname]", color="#7b7b7b", what_color="#bebebe" )

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
            m "With tomorrow I don't mean 6:30PM. The office closes at 7:00PM. If it's not printed by then, you have to figure out how to print it."
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
            show matt_neut
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
            m "With the person in charge of design gone they have really been struggling to pull everything together."
            m "Since the deadline set by the client is in 2 weeks they desperately need someone to fill her place."
            m "And you will be done with your poster soon. {i}I'd hope{/i}. You'd be a good candidate to take the offer."
            m "I have to admit, I'm not too keen on you switching teams already. But Simon insisted I ask you to take the position."
            m "Beats me why he would request you specifically but I guess after one year you've had enough time to get into the swing of things here."
            m "So, Sullivan. Since you already agreed to taking this opportunity I hope you do your best to adjust to their work flow quickly."
            d "I'll give it my all."
            m "Good. Simon will be happy to hear I've found someone."
            m "Unlike me, Simon expects a lot more autonomy of his team." 
            d_t "Thank god. Finally some freedom. I can't deal with another controll freak like Matt."
            m "I was reluctant to offer you this position since it seems you still need the supervision. But it can't be helped."
            m "If he insists then I won't tell him otherwhise. Most of the other viable designers are quite busy with their own projects at the moment anyways."
            m "I hope you step up to the job and deliver as demanded."
            m "I don't want you to make a bad impression on his team. I'm sure you understand that that would also have very undesirable concequences on my side."
            d "I understand. I won't dissapoint you Matthew. I'm sure having a new work environment will be a great experience for me."
            m "Are you saying you don't like my way of doing things?"
            d "No of course not! I just meant it will be good for me to also get a look into how other teams do it around here."
            m "Alright. If you say so."
            "..."
            m "You don't seem to be hungry today do you."
            d "Yeahhh, I dont' have that big of an apetite right now."
            d_t "This is so uncomfortable why did he have to do this over lunch."
            m "There's no shame in addmiting you don't like mushrooms Sullivan. Not like your face does't give it away everytime you bite down on one."
            d "He he... Sorry. I just can't stand the texture. I think I'll just get up and go and get myse- oh no!"
            "Clank!"
            #The plate flips
            d "OH. I- I'm so sorry Matt..."
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
                    d_t "Maybe I'll find someone around here."
                    "BUMP"
                    show simon_neut
                    d "Oops Sorry!"
                    s "Oh! You're Destiny right!"
                    d "Huh?"
                    s "I've heard a lot about you!"
                    s "I thought Matthew said we would meet after lunch to talk about switching teams. Did something come up?"
                    d "You're Simon then! Yeah sorry about that."
                    d "Uhm, yes."
                    d "Something came up. I apolagize. You've heard a lot about me?"
                    s "Yes! your work speaks for it's self. Speaking of. I thought Matthew said you were still finishing up a project"
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
                    show simon_neut
                    s "I think I know how to get it running again."
                    d "Wow, Thank you so much Simon! You're a real life saver."
                    s "Oh don't be like that. It's the least I can do now that I know we'll finally have someone to take Kai's place."
                    d "Kai?"
                    s "Yes. She did our designs up until now."
                    s "I'm sure Matthew told you about her."
                    d "Not really, no."
                    s "No one knows why she would just quit so out of the blue. Especially since we are still in the middle of a project at the moment. "
                    s "She was always so passionate about what she did. Something important must have come up..."
                    s "Anyhow. We can only speculate. But I'm glad we have you to help us out soon now!"
                    s "We've really been struggling without her around."
                    s "I'm looking forward to working with you."
                    d "Me too!"
                    d_t "Anything beats Matt."
                    s "So, about that project you're still finishing up rigth now?"
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
                    d "It's not too far away and I have a great view."
                    d "Oh, and my friend that also works here actually lives there as well!"
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
            show gabe_happy
            g "There you are! What took so long? I heard what happened over lunch."
            g "You should have seen his face! It was hillarious."
            g "From an outside perspective of course. I'm sure you must have been fearing for your life."
            g "He was furious. The way he stormed out of the cafeteria left everyone dead silent."
            g "Did Matt catch you on your way out?"
            hide gabe_happy
            show gabe_neut
            d "Thankfully not. No, I don't think I'd be alive right now if that happened"
            g "I think Matt would have crucified you right on the spot."
            g "Did you stay longer to finish your project then?"
            d "No, I still have to work on it tomorrow. I had some trouble with the printer"
            if fix_printer==True:
                d "It Jammed and I had to find someone to help me print the forms I need to finally escape Matt."
            else:
                d "It Jammed so I couldn't print the forms to join that new team."
            hide gabe_neut
            show gabe_conf
            g "Did you use the old one in the back on floor 3?"
            d "Yeah, why? I've never had troubles with it so far."
            hide gabe_conf
            show gabe_neut
            g "Wow you must have had insane luck then. That one is known for eating paper like it's been starving for the last decade."
            d "Huh. I guess I just got lucky up until now."
            d "But I guess that luck has run out now."
            d "Let's just get going. I want to keep the chances of running into Matt or anyone was there to witness happened today to a low."
            g "Do you want to take the long or the short route?"
            menu:
                "Take the long way.":
                    d "I want to go the long way. I need some movement to clear my head."
                    d_t "If that screen is to trust just this once this stroll will be nice."
                    hide gabe_neut
                    show gabe_happy
                    g "The long one it is then."
                "Take the short way.":
                    d "The short one please. I just want to get home after today."
                    d_t "With that screen mentioning the stroll, I don't think I can trust it."
                    hide gabe_neut
                    show gabe_happy
                    g "The short one it is then."
            scene bg_street
            show gabe_neut
            g "How was your day, if we ignore the obvious fopa at lunch?"
            d "It was fine. I didn't get to work on the poster as much as I'd liked though. I have a lot to do tomorrow."
            hide gabe_neut
            show gabe_conf
            g "Why's that? Did something come up? I thought you kept your scedule as free as possible specifically to be able to work on it a lot today."
            d "It's not that. I didn't have anything else planned."
            d "I just wasn't able to focus at all."
            d "My thoughts were all over the place the entire day. Just never on work."
            hide gabe_conf
            show gabe_conc
            g "Got something on your mind Destiny? If there's something bothering you maybe talking anout it will help."
            d_t "Can I tell him about the screen?"
            menu: 
                "Tell him":
                    d "Have you ever started seeing things from looking at screens too much?"
                    hide gabe_conc
                    show gabe_conf
                    g "What do you mean? Like hallucinations?"
                    d "Yeah. Like a screen with legitemate text."
                    g "What!?"
                    hide gabe_conf
                    show gabe_conc
                    g "Have you been hallucinating.?"
                    d "Maybe?"
                    g "Destiny, I think you seriously need to get some rest. You've been overworking yourself too much."
                    g "Staring at that screen all day every day can't be good for you."
                    g "When was the last time you've taken a day off or just slept for a solid 8 hours?"
                    d "..."
                    d "Quite a while ago..."
                    hide gabe_conc
                    show gabe_neut
                    g "Okay. Why don't we make sure you get home a little earlier today and get a good night of sleep."        
                    g "I'm sure you're just overworked and maybe also a bit dehydrated. Did you have enough water today."
                    d "Now that I think about it, no I haven't really had too much to drink today."
                    d_t "But the screen was there even in the morning."
                    hide gabe_neut
                    show gabe_happy
                    g "See. I'm sure you'll feel better once you take a small break and have something to drink."
                    hide gabe_happy
                    show gabe_neut
                    g "And please make sure to go see a doctor if it gets worse, alright?"
                    

                "Be dismissive":
                    d "I think I might have just not slept enough."
                    d "Usually runnign on little sleep isn't a problem for me but this Project has been keeping me up more nights than I'd like"
                    g "Sounds to me like you're overworking yourself."
                    g "When was the last time you've taken a day off or just slept for a solid 8 hours?"
                    d "..."
                    d "Quite a while ago..."
                    hide gabe_conc
                    show gabe_neut
                    g "Okay. Why don't we make sure you get home a little earlier today and get a good night of sleep."        
                    g "Maybe you're also a bit dehydrated. Did you have enough water today."
                    d "Now that I think about it, no I haven't really had too much to drink today."
                    hide gabe_neut
                    show gabe_happy
                    g "I'm sure you'll feel better once you take a small break and have something to drink."

            hide gabe_happy
            show gabe_neut
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
            d "What?"
            x "I'm not an illusion. I'm here to help you."
            x "It doesn't have to happen to you too."
            d "I-"
            x "I know about your future. I know what you need to do now. I couldn't stop it myself but you can."
            x "He's after you. You have to remember m3."
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
            "!"
            d_t "Seriously!?"
            d_t "That screen is still here!"
            d_t "Hold on! It's changed. There's different achievements today."
            show achievements
            d_t "This can't just be from over working myself anymore."
            d_t "There's no way fatigue can cause something like this."
            d_t "That screen was there the whole time yesterday too. That's not even the worst of it." 
            d_t "All of the achievements came true somehow"
            d_t "What are you? And why do you know what I'm going to do?"
            d_t "It looks exactly the same as yesterday except for the text."
            d_t "I was honestly hoping it would just go away overnight."
            d_t "Clearly that was too optimistic of me."
            d_t "But they did all come true didn't they?"
            d_t "Hmm."
            d_t "Maybe if I can figure out what they actually mean beforehand I'll be able to avoid ruining my day this time."
            d_t "Let's see. They happened in the order they were writen in right?"
            d_t "What does my looming spector have to say about today?"
            default matt_excuse = 0
            label achievements2: 
                menu:
                    "\"Stick the landing\"":
                        d_t "Stick the landing. Hmm..."
                        d_t "The first thing today. Yesterday it was about coffee."
                        d_t "What landing is there to stick?"
                        d_t "Will this be about my breakfast again?"
                        d_t "Oh no. Not today. I'll make sure I don't eat anything sticky. Lord knows in how many {i}lovely{/i} ways sticking a landing can be interpreted."
                        d_t "Maybe dropping a jammy toast. Or Having an egg stick in the pan."
                        d_t "No none of that today."
                        d_t "I guess I'll just have some coffee today."
                        d_t "I really hope that's enough to avoid any major disasters. I mean hey, sticking the landing could also mean something good!"
                        jump achievements2
                       

                    "\"We meet again old foe\"":
                        d_t "Here we go. Only the second one of the day and this already sounds great. {i}Old foe{/i}. Who could it mean by foe?"
                        d_t "And an old one? The only foe I have right now, that I could think of, has to be Matthew."
                        d_t "But I wouldn't really call him a foe. We just don't really see eye to eye. Besides I'm barely supposed to see him today."
                        d_t "I just have to finish my poster and print it on time and then he'll have nothing to hold against me anymore."
                        d_t "Ugh. Easier said than done though."
                        d_t "He does seem to have it out for me. Why does he always have to be there whenever something goes wrong."
                        d_t "God I hope he doesn't bring up that fiasco from yesterday. Please just let today's work go smoothly"
                        d_t "Maybe I can prepare a bit now."
                        d_t "In the case I really will run into Matt today it certainly wouldn't hurt to know what to say."
                        d_t "Hmm what would be a good excuse for absolutely drenching him in stew and running away."
                        menu:
                            "Nausia":
                                d_t "I could say those mushrooms suddenly made me really nausious."
                                d_t "Maybe he'll buy it. I mean I did run to the bathrooms to hide."
                                d_t "Plus, I'm sure he can't really blame me for that. I doubt he'd rather had had me trow up in the cafeteria..."
                                d_t "Ew." 
                                d_t "No, that'll do. He won't ask too many questions after that."
                                $ matt_excuse = 1
                            "Getting tissues":
                                d_t "I could tell him i wanted to go get tissues to help him clean up."
                                d_t "I mean I did run in the direction of the bathrooms. I could have just as well wanted to go get something to wipe off the mushrooms."
                                d_t "Might not have been the most efficient way to do so but Gabe said Matt stormed out of the cafeteria too."
                                d_t "I could just say I went to go get tissues but couldn't find him when I got back."
                                d_t "It's risky but it'll work I think."
                                d_t "It's the best I've got right now."
                                $ matt_excuse = 2  
                        jump achievements2

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
                        d_t "A dinner for two. Huh, at least this one sounds pretty straight forward."
                        d_t "I dont see how this could be anything other than a literal dinner for two people."
                        d_t "Now who could it be with?"
                     
                    "\"Knock Knock\"":
                        d_t "Let's hope this is refering to a door. I honestly can't imagine anything else I'd be knocking on."
                        d_t "Oh! It might not be me knocking. Maybe I'm getting a package delivered."
                        d_t "Did I order anything recently?"
                        d_t "Hmmm. Maybe it's my new coffee machine. It's about time that arrived."
                        d_t "I've been starting to think they lost the package."
                        d_t "No. It's supposed to happen pretty late in the day. It's probably not the mail."
                        d_t "Could someone be coming to visit?"
                        d_t "Ugh. Is it going to be doordashers? I have heard some of the kids around the block have started going around the appartments recently."
                        d_t "Well, I don't think that would be significant enough to be on here. But who knows. That stain in the morning wasn't too significant either."
                        d_t "Maybe I'll be visiting someone."
                        d_t "Not that I'm planning to right now..."
                        d_t "I guess I'll just have to see. I don't think I can figure out what this means right now."
                        jump achievements2

                    "Finish checking achievements":
                        return
            d_t "It's not a lot of preparation. I'm pretty certain on some of them but why do they have to be so darn vague."
            d_t "And why now of all times? I wish I had more time to figure out where this is all coming from. But I'm neck deep in work right now."
            d_t "Still, there has to be a reason for this right? Let's hope today goes more smoothly than yesterday." 
            d_t "Maybe I'll have some time to be able to figure out why this is happening to me after I'm done with my project"
            d_t "Ughh. Time to get ready for work I guess."
            jump work2
        label work2:
            scene bg_office_computer
            d_t "Okay! I'm almost done with this darn poster!"
            d_t "I can't allow myself to be distracted now."
            #have to continue
            d_t "Phew that's it I think. It's not getting better than this."
            d_t "Alright! Time to print this baby and drop it off over in the meeting room."
            d_t "Oh shoot! It's already 5:00PM. Darn. Time really flew by me today."
            d_t "It should be fine though. I just have to print it. That won't take too long and then I'm done for today."
            d_t "Hey that went better than expected! I don't think I had any major hickups today."
            d_t "Other than maybe the one or two times the program crashed on me."
            d_t "But that's to be expected by now."
            d_t "Strange..."
            d_t "I though I'd have to deal with those stupid achievements all day. But come to think of it I don't think I've had a single one of them happen yet."
            d_t "Nothing about sticking or foes. Also no running yet."
            d_t "Eh it doesn't matter. I'm just glad all of that is over now. Seems like I was just reading into it way too hard yesterday."
            d_t "Time to go print this bad boy."
            scene bg_office_hallway
            show gabe_happy
            g "Oh Hi! Didn't expect to still see you today."
            d "Gabe! Hi."
            g "Hey, I didn't see you in the cafeteria today. Did you skip lunch to work on the poster?"
            d "Yeah. Heh... I had to crunch a bit. Plus I wanted to minimize my chances of running into Matt. But hey! I got it done!"
            g "Congrats! No surprises there though haha. I knew you'd get it done on time!"
            g "That's the regular Destiny for you right there. Always a bit last minute. But you never fail to stick the landing somehow!"
            d "Huh!?"
            d "Hold on, what did you just say?"
            g "Uhm..." 
            g "I just said that I'm amazed how you always stick the landing somehow."
            g "I meant that as a compliment. I'm sorry did I say something bad?"
            d "Oh, no no! Everything's alright Heh. I didn't catch what you said just then."
            d_t "Does this mean I wasn't overthinking it yesterday?"
            g "Oh thank god. You looked so shocked. Had me worried there for a second."
            d "I guess I am always a bit fasionably late, eh?"
            d_t "What do I do now? Are all the others also going to come true? It's so late in the day already."
            g "Late but with the best work!"
            g "Are you sure everything's fine? You look upset."
            d "Sorry. Really, I'm fine. Don't worry it's nothing."
            d "I was just thinking about how I still have to print it out. And what if the clients don't like it."
            d "Hey, who knows. Maybe this is the one where all of the rushing gets me. Where something goes wrong last minute or it's just not good enough."
            g "Oh come on now. You don't have to worry about that now. You got it done. There's not much more you can do now."
            g "Besides, I'm sure the clients will love your work."
            g "But now go and print it! I don't want to be the reason you don't make it on time, okay?"
            d "Yes! Right! Gotta go."
            if fix_printer == True:
                jump printer2fixed
            else:
                jump printer2unfixed

        label printer2fixed:
            scene bg_office_printer
            d_t "Here we are. Alright!"
            d_t "I just have to print this file right here, then I'll finally be done with this."
            "..."
            "Bing!"
            d_t "Oh! That must be my print!"
            d_t "And another win for miss Destiny Sullivan!"
            d_t "Today's going smoother than expected. All that's left now is to drop it off at the meeting room."
            d_t "Maybe I'll actually be able to leave on time today!"
            scene bg_office_cafeteria
            m "Sullivan!"
            show matt_neut
            d "H-Hey Matthew... long time no see."
            m "Yeah. {i}Not that I mind.{/i}"
            d "Look, uhm Matthew. I'm-"
            m "Can you please explain the absolute disrespect and mockery I had to endure yesterday. What's wrong with you? Are you a child? No reasonable adult just runs off like that."
            m "Yeah Mistakes happen jada jada-. But that? Seriously. Stand up to apolagize like the grownup you are."
            m "I expected better."
            if matt_excuse == 1:
                d "I'm really sorry Matthew. Truly. I didn't mean to just sprint out on you like that. It's not that I wanted to avoid apolagizing."
                d "But there was something about those mushrooms. I got so nausious all of a sudden. It felt like my stomach Had turned on it's head."
                m "..."
                d "I was scared I was going to throw up right there if I stayed any longer. And I didn't want to cause a scene in the cafeteria so I ran to the bathrooms"
                m "Well a scene it was."
                d "Sorry..."
                m "I looked like a darn fool."
                d "Uhm, I came looking for you to apolagze after I felt a little better. But I couln't find you in the cafeteria anymore."
                m "Sure."
                d "I'm very sorry."
                d "Really."
                m "We will seriously have to talk about your attitude. I understand feeling unwell but nonetheless your behavior was disrespectful and plain rude."
                d "I-"

            elif matt_excuse == 2:
                d "I'm really sorry Matthew. Truly. I didn't mean to just sprint out on you like that."
                d "I was actually looking for something to help you wipe off the stew from your shirt."
                m "..."
                d "I thought I'd run to get some from the washrooms. There's always tissues there."
                m "Tissues?"
                d "Yeah..."
                m "Really?"
                d "Uhm, I came looking for you to apolagze and clean up. But I couln't find you in the cafeteria anymore."
                m "And you expect me to believe that."
                d "Sorry. I-"
                m "We will seriously have to talk about your attitude. I could understand feeling unwell or something like that. But blaitantly lying?"
                m "This level of disrespect is unacceptable."
                d "I-"

            else:
                d "I- Uhm. I'm sorry. I don't know what got into me."
                m "That makes the two of us. What posessed you to think storming off would be a good idea?"
                m "First you ruin my shirt and then you bolt out like that would fix the situation."
                m "Not only did I look like a darn fool with stew all over his shirt, which i guess can happen. But you also refused to take responsibility for your actions by hiding in some bathroom stall somewhere I presume."
                d "I-"
                m "No no. You listen."
                m "We will seriously have to talk about your attitude. I could understand feeling unwell or something like that. But pulling off a stunt like that and then not even having an explanation for it?"
                m "This level of disrespect is unacceptable."



            g "Destiny!"
            d "Gabe?"
            show gabe_neut
            g "Oh, afternoon Matthew."
            m "Anderson."
            g "I wasn't expecting to see you two here."
            m "My thoughts exactly."
            g "Actually, Destiny I was looking for you. I have something I have to discuss with you."
            d "Wha-"
            m "Actually we are in the middle of a conversation at the moment. So If you'd excuse us."
            g "I'm terribly sorry Matthew. Seems you two are having quite the serious talk but it's something quite personal and urgent."
            g "Could I borrow her for a minute?"
            m "What could be so important that you need her right this instant?"
            g "Like I said it's a personal matter. But I assure you I wouldn't be barging in like this if it wasn't important."
            d "Gabe, it's alright I'll-"
            m "Fine. We'll continue this conversation some other time. I don't have the nerve for this right now. I'm quite {i}busy{/i} at the moment anyways."
            m "Besides, I doubt the time we have left today would suffice to discuss what needs to be adressed."
            m "For your sake I hope you at least finished your project already."
            d "Yes! Uh- I have the print right here actually. I was just about to bring it to the conference room."
            m "Then you'd better get on with that as soon as whatever this {i}urgency{/i} is has been dealt with"
            g "Shall we Destiny? Let's go back to your office to talk."
            g "It's much quieter there."
            d "S-sure."
            g "See you around Matthew."
            m "Yeah, see you around. Same goes for you Sullivan."
            m "Don't think you can get outt of this one so easily."
            d "I'm sorry. Of course."
            d "See you around."
            scene bg_office_hallway
            g "Phew! That was a close one. Looked like Matt was really out for blood this time. Looks like he took it quite personally"
            d "Oh yeah 100%. I was scared he was about to end my carreer right there on the spot."
            d "I'm done for. He's going to fire me!"
            g "Hey, take a deep breath. Surely they're not going to fire you."
            g "I'm pretty certain he can't do that just because of one incident. Higherups have to look over things like that. And an accident happen you know."
            d "How are you not scared of him?"
            d "I was about to cry. I could have never stood up to him like that."
            g "Oh hes not that scary. He's more like a dog."
            g "All bark no bite."
            g "He talks a lot and likes to pressure people but other than being mean he rarely does anything really."
            g "Besides what's he got on me? I just needed to talk to you about something important. The worst he could have done was refuse to let me talk to you."
            d "I don't know how you do it. Wow."
            d "Speaking of it. What did you want to talk to me about?"
            g "Oh, uhm nothing if I'm being honest. I didn't want you getting mauled out by Matt."
            g "Saving a friend from a ferral creature sounds personal and urgent enought to me."
            d "Tell that to Matt haha."
            g "Seems i came at exactly the right moment."
            g "Well, I was actually looking for you."
            d "Oh?"
            g "I forgot to ask you something before."
            g "Would be interested in making dinner together again tonight."
            g "You know. To celebrate you finally being done with this poster."
            g "You've looked so distressed lately. I thought you could use a nice relaxing evening."
            d_t "This has to be the dinner for two!"
            g "We could meet at your place and cook something nice."
            d "That does sound relaxing."
            d_t "Hold on! What would happen if I said no?"
            d_t "All of the other achievements came true so far. If this really is the dinner for two then doesn't this mean I wouldn't be able to say no?"
            d_t "This is the first time I've gotten the choice. But... this has to be the dinner for two."
            d_t "Shoot!"
            d_t "Cooking together sounds so nice. But this might be my only chance to prove the screen wrong!"
            g "So, What do you say? Do you want to cook together?"
            menu:
                "Agree to have dinner together.":
                    $ dinner_plans = True
                    d_t "Oh screw this. Why should I miss out on something I really want to do just to prove some stupid imaginary screen wrong?"
                    d_t "If that's what these dumb achievements want then so be it."
                    d "Yes! I'd love to! That sounds like exactly what I need."
                    g "Great! I've already got something in mind we could make. I have almost everything at home too."
                    d "Ohhh, sounds promising. What is it?"
                    g "It's a surprise but I'm sure you'll like it!"
                    g "I'm actually already done for today so I can go get the last few ingredients on my way home."
                    d "I still have to get this to the conference room and clean up a bit around my desk. How about we meet at my place at 7:00PM?"
                    g "Works for me."
                    g "See you at 7 then!"
                    d "Seeya."

                "Make up an excuse.":
                    $ dinner_plans = False
                    d_t "I'm sorry Gabe. But this might be my only chance at finding out what this all means."
                    d "I'd love to... but, I'm just so tired and exhausted from the last few days."
                    d "I barely got any sleep yesterday and I think I'd better just go to bed extra early today."
                    d "Let's do something on the weekend! I doubt I'd be fun company right now. I want to actually be able to help you in the kitchen when we do it haha. "
                    d "I think today I'd just doze off every couple of minutes."
                    g "Oh, Of course! I understand. Get some rest today. You've deserved it." 
                    d "Thanks."
                    g "Does Saturday night sound good? I don't have any plans over the weekend so whenever's good"
                    d "No Saturday sounds great. For sure!"
                    g "Nice. I'm actually already done for today so I'll catch you tomorrow for lunch?"
                    d "Yeah, of course. The table in the back, as usual."
                    g "Exactly."
                    g "Have a nice evening then Destiny!"
                    g "And go to bed extra early today."
                    d "I will! Thank you."
                    d "See you tomorrow."
                    g "Seeya."   
            jump running

        label printer2unfixed:
            scene bg_office_printer
            d_t "Here we are. Alright!"
            d_t "I just have to print this file right here, then we'll be-"
            "Trrrkkk"
            d_t "..."
            d "WHAT?"
            d "Not again."
            d "Not {i}you{/i} again!"
            d_t "Oh no"
            d_t "No... Stupid printer! I'm such an idiot. Why didn't I just have it fixed yesterday? Of course this is what's going to screw me over." 
            d_t "It's always the printers that doom me."
            d_t "Darn it! Seriously?! No one else needed to print anything since yesterday?"
            d_t "I should have just done it then. Stupid! Oh come on. I'm going to be late now!"
            d_t "Matt is going to murder me."
            d_t "I don't have time for this right now"
            d_t "I'll be beating myself up enough over this later. Right now I just have to find someone to help me."
            d_t "Fast."
            scene bg_office_hallway
            d_t "I'm sure I'll find someone around here!"
            "BUMP"
            show simon_neut
            s "Oops Sorry!"
            d "Sorry! I didn't s-"
            s "Wait! You're Destiny!"
            d "What?"
            s "You are Destiny, no? The graphic designer Matthew said he would interduce to me yesterday, the one that would start working for us?"
            s "I've heard so much about you!"
            d "Oh really? Yeah, that's me."
            d "You must be Simon then! Sorry about not showing up yesterday."
            d "Uhm. Something err... came up."
            s "Oh don't worry about it. This kind of stuff happens. I'm glad I finally get to meet you today! Your work really speaks for it's self."
            d "Wow, thank you!"
            s "What are you doing in such a hurry? I hope I'm not bothering you."
            d "No no! I'm glad I ran into someone here!"
            d_t "Isn't this just Perfect! He'll have a horrible first impression of me now!"
            d "Uh, I was just about to print the final design of my project but I think someone before me must have put in too much paper heh..."
            d "I tried taking the paperchute out but it won't budge."
            d "Printing the poster is the last thing I have to but I'm starting to run late again."
            s "Right! Matt mentioned you were just about to finish your project. Has he sent you the application forms yet?"
            s "Oh sorry!"
            s "Yes. First we deal with the printer!"
            s "I'll help you out. I've had my fair share of unfortunate encounters with that one. Let's go have a look at it."
            scene bg_office_printer
            show simon_neut
            s "I think I know how to get it running again."
            "WHAM"
            s "There!"
            s "Now we just have to wait for your print to finish."
            d "Wow, Thank you so much Simon! You're a real life saver. I can't imagine what Matt would do if I hand in another project late."
            s "Oh don't be like that. It's the least I can do now that I know we'll finally have someone to take Kai's place."
            d "Kai?"
            s "Yes. She did our designs up until now."
            s "I'm sure Matthew told you about her. No one knows why she would just quit so out of the blue. Especially since we are still in the middle of a project at the moment. "
            s "She was always so passionate about what she did. Something important must have come up..."
            s "Anyhow. We can only speculate. But I'm glad we have you to help us out soon now!"
            s "We've really been struggling without her around."
            s "I'm looking forward to working with you."
            d "Me too!"
            d_t "Anything beats Matt."
            s "So, this is that project you were still finishing up?"
            d "It's nothing big but I got tasked with designing an ad poster, yes."
            d "I'm glad I got it done today. "
            s "Well then. Seems like we'll be collaborating from now on. How exciting!"
            s "Matthew told me a few things about you already. You've been working here for about a year, no?"
            d "Yeah. One and a quarter actually. But I haven't really had the chance to work on any big projects yet."
            s "Matthew tends to be a bit too careful with handing out jobs"
            s "In my oppinion the only way to get experience is to do the thing you want to learn."
            s "Is view on the matter seems to be a bit more uptight."
            d "A little yes haha."
            s "Well then this will be a good new experience for you!"
            s "Did you also move here before starting work for Matthew?"
            s "Do you live somewhere around here too?"
            d "Yeah. I moved into one of the newer appartment complexes just two stops away."
            s "Wow, you must be in the ones close to the park then. I've heard only great things about them."
            s "How do you like the area? In my oppinion it's one of the best. Especially if you work in the city."
            d "I like it a lot actually! I have a great view of the park and the city from my appartment. And my neighbours are fantastic."
            d "Actually, a good friend of mine that also works here lives there as well!"
            s "Sounds lovely."
            "Bing!"
            d "Oh! That must be my print!"
            d "Thank you so much for helping me with the printer!"
            s "Of course. I'm glad I was able to help."
            s "I see you've printed the application as well! Don't forget to hand it in untill tonight."
            s "I'm looking forward to having you on my team!"
            d "Yes me too. I'm sorry I have to hurry back now."
            s "See you around Destiny."
            d "See you around!"
            d_t "Alright time to drop this poster off at the conference room!"
            jump running

        label running:
            scene bg_black
            scene bg_office_computer
            d_t "Whew. Glad I got that done now. I feel liberated. And I dropped it off on time too for once!"
            d_t "Oh yeah, time. What time is it?" 
            d_t "6:30PM already?! Wow! I really thought I'd be done earlier today."
            if dinner_plans== True:
                d_t "Oh no! I have to hurry. I almost forgot."
                d_t "I told Gabe he could be at my place at 7."
                d_t "Darn! Looks like I'll have to run afterall."
                d_t "I guess that screen was right. There's no denying it. I can't escape them so easily it seems."
                d_t "Well, at least I was able to mentally prepare myself this time."
                d_t "Oh come on me! A little jog won't kill me."
                d_t "UGH. That doesn't it's going to be fun!"
                jump dinnerfor2gabe
            else:
                d_t "Oh well, it can't be helped. At least I get to finally go home now."
                scene bg_street
                d_t "It's only Tuesday and this week has already been way too long."
                d_t "I wonder what's going to happen to the rest of the achievements now. Especially the dinner one."
                d_t "Maybe it was wrong this time. I can just refuse-"
                "Meowww!"
                d "Oh hey there Kitty!"
                c "Prrrt"
                d "Aww, aren't you a cute one!"
                d "Oh but you're all scraggly looking. What happened to you?"
                c "mEEEwr"
                d "You don't have a collar do you?"
                d "Oops, Sorry!"
                c "Hssss"
                "Thudd"
                d "Ah no my folder!"
                d "N- No not that! Spit that out!"
                c "mrrr"
                #the cat runs away
                d "Hey! No, come back here! That's my-"
                scene bg_ally
                d "HAH! Got you you little rascal!"
                c "awrr"
                d "Now give me back that forms."
                "Tug!"
                d "There"
                d "Looks like you made me run for it after all. Darn it. And here I was, planing on exactly not doing that today."
                d "You must be a secret little agent."
                d_t "Another one happened."
                "..."
                d "And of course you just had to take me to the dimmest, dirtiest allyway you could find eh?"
                d_t "Creepy..."
                d "Is this where you live?"
                c "Mwrrm"
                d "Hmmm, I can't just leave you here now... This place reaks."
                d "How about we try to find your owner."
                d "{i}If you have one{/i}"
                d_t "It's late already."
                d "We'll try to find your owner tomorrow, for now you're coming with me. What do you say little guy?"
                c "Meowww!"
                d "Ha ha. You're adorable ehm-"
                python:
                    catname = renpy.input("What should I call you?", length=32)
                    catname = povname.strip()

                    if not povname:
                        povname = "Kitty"
                d "[catname]!"
                d "Let's get you cleaned up [catname]."
                "Clank!"
                d "!"
                d "What was that?"
                d "..."
                d "Let's just get out of here. This place is starting to freaking me out."
                jump dinnerfor2cat

        label dinnerfor2gabe:
            scene bg_d_corridor
            g "Hey! It's me Gabe!"
            d "One second, be right there!"
            show gabe_neut
            g "So, want to get to cooking? I brought all the ingredients."
            d "Yes! Let's go."
            scene bg_d_kitchen
            g "I brought everything we need to make your favorite noodle soup!"
            d "You know me too well! Thank you so much Gabriel!"
            g "It's my pleasure."
            g "How about I start with preparing the broth? Then you can already get to chopping the vegetables."
            d "Perfect."
            #Skips to right before they're done.
            "*Knock Knock*"
            d "Shoot! Gabe can you go see who it is quickly? I just put the chicken in the pan."
            g "Yeah of course. One second."
            #Achievements glitch but no altered text
            g "Huh? Doesn't seem to be anyone there!"
            g "I'll have a look if they left anything outside!"
            #Achievements glitch but no altered text
            d_t "Oh right! The knocking. I wonder who it was."
            show gabe_conf
            g "Weird. There wasn't anyone outside. And they didn't leave anything either."
            d "Strange."
            d "It must have been some doordashers then."
            g "Probably."
 
            jump day3

        label dinnerfor2cat:
            #HAVE TO CONTINUE
            scene bg_d_kitchen
            d "Alrighty! Here we are."
            c "mrrr"
            d "Make yourself at home [catname]. But don't go around destroying anything alright?"
            c "Meowww!"
            d "Oh! You must be hungry! Let's see what I have for you."
            d "Hmmm. Looks like I have some tuna in my pantry. Do you like tuna?"
            c "MEEEwr!"
            d "Haha, someone's enthusiastic!"
            d "Wow, come to think of it I'm starving too!"
            d_t "I barely had anything to eat today."
            d "Time to make me some dinner too, no?"
            c "Prrrr"


            
            "*Knock Knock*"
            d_t "Huh?"
            d_t "Oh right. The \"knock knock\" one."
            c "Mrrauw?"
            d "You stay here little guy."
            d_t "Who it could be-"
            #Achievements glitch to Don't open the door.
            d "!"
            d_t "Wh- What was that?"
            d_t "-"
            d_t "No I must have just imagined it. I'll just look who's outside the door."
            #look outside (noone)
            d_t "What in the...?"
            d_t "Did they leave something at the door?"
            d_t "Maybe they-, I cant see it from here I'll have to go and check-"
            c "HSSSr!"
            #screen permanently glitches to DONT
            d_t "EHM?" 
            d_t "WHAT!?"
            d_t "I knew I saw something!"
            #Glitches to dont open it. and be quiet
            c "mEEEwr"
            d_t "What the F-"
            d "{i}Shhh. [catname] it's ok.{/i}"
            menu:
                "Open the door.":
                    $ open_door= True
                    d "He- Hello? Is someone there?"
                    d_t "They didn't leave anything..."
                "Keep it closed":
                    d_t "Oh hell no! What the hell is going on!?"
                    d_t "I'm not opening that door."
                    d_t "This is crazy!"
                    d_t "Who was that?!"
                    #Glitches to stay inside tonight.

            jump day3

#DAY 3
    label day3:
        label dream3:
            scene bg_black
            x "He was here!" 
            d "Who was-"
            x "You can't trust him Destiny! You have to stay away from him. He's dangerous."
            d "Who are you!"
            x "He's going to keep trying to get close to you. You can't let him win."
            x "Get help! I'm begging you. Don't do as he says."
            d "I-"
            x "He's trying to get you to like him."
            x "To trust him"
            d "Who are you talking about?"
            x "You can't trust him. He won't save you."
            x "He's keepin-g me (agEd."
            x "He*L 9 m-e."
            d "Wait!"
            x "I (an '7 e5c *p 3"
            x "-"
            jump morning3
        label morning3:
            if dinner_plans==False:
                scene bg_d_window
                d "AH!"
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
