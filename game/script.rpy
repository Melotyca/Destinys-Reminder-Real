#Destinys Reminder
#Fonts
#Characters
define d = Character("Destiny",who_font="Minako-Regular.ttf",who_size=53, color="#067b6d", what_font="Minako-Regular.ttf", what_color="#1db7a5", what_size=38)
define d_t = Character("Destiny",who_font="Minako-Regular.ttf",who_size=53, color="#067b6d", what_font="Minako-Regular.ttf", what_italic=True, what_color="#79b0a3cb", what_size=38)
define g = Character("Gabriel",who_font="Hey Comic.ttf", color="#627e05",what_font="Hey Comic.ttf", what_color="#84a41b")
define m = Character("Matthew",who_font="DraftingMono-Bold.otf", color="#1346a0",what_font="DraftingMono-Bold.otf", what_color="#4c77c1")
define s = Character("Simon",who_font="Typo_Round_Bold_Demo.otf", color= "#b01d1d",what_font="Typo_Round_Bold_Demo.otf", what_color="#c64e48")
define x = Character("?",who_font="KGRedHands.ttf",who_size=45, color="#444444",what_font="KGRedHands.ttf", what_italic=True, what_color="#7b7b7bb5",what_size=30 )
define k = Character("Kai",who_font="KGRedHands.ttf", color="#444444",what_font="KGRedHands.ttf", what_color="#7b7b7b")
define c = Character("Cat",who_font="gabriele-bad.ttf", color="#444444",what_font="gabriele-bad.ttf", what_color="#7b7b7b" )
define c_n = Character("[catname]",who_font="gabriele-bad.ttf", color="#673b05",what_font="gabriele-bad.ttf", what_color="#aa811a" )
define o = Character("Officer R.",who_font="texgyrecursor-bold.otf", color="#001f55", what_font="texgyrecursor-bold.otf", what_color="#315089")
define s_k = Character("-",who_font="Typo_Round_Bold_Demo.otf", color= "#6c4848",what_font="Typo_Round_Bold_Demo.otf", what_color="#9f706e")

#Variables
default fix_printer = False
default dinner_plans = False
default open_door = False
default call_police = False
default gabe_hints = 0
default trust_kai = False
default track_who = 0
default gabe_ally = False
#GAME
    
label start:
    label game:
    #DAY 1
        label day1:
            label dream1:
                scene dream1
                x "Destiny..."
                x "Destiny!"
                x "You have to listen to me."
                x "Something bad is going to happen."
                x "Please."
                x "Don't trust him. You're in danger"
                x "I can help you."
            label morning1:
                scene bg_black
                "Ping!"
                d_t "Who, What was that?"
                d_t "{i}Ugh{/i} What time is it? It feels like I've only just fallen asleep."
                scene bg_d_window
                show phone
                show a_day1  
                # (phone appears(see Her reminder Project due tomorrow, Day and time: Mon 07:13). 
                d_t "Oh come on. Just let me sleep."  
                d_t "Why can't it be like 4am."
                d_t "Pleaseee... If I stay in bed now I'll be late."
                d_t "I guess I've got no other choice."  
                d_t "Coffee time!"   

                scene bg_d_kitchen
                show a_day1
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

                hide a_day1
                show a_day1 at right
                d  "Heh. Heh he..."  
                d_t "A display. Really?"  
                d_t "Oh god. No more games before bed."
                d_t "What's next. Some NPC walks through my door? As if."
                d_t "This can't be serio-" 
                "{i}Knock knock.{/i}" 
                d "AH!" 
                hide a_day1
                show a_day1
                #(cup falls and shatters and spills). 
                #(shattered mug). 
                g "It's me, Gabe. Is everything alright in there?"   
                d "Yes yes! On my way."
                #door opens
                scene bg_d_corridor 
                show a_day1
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
                show a_day1
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
                show a_day1
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
                show a_day1
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
                show a_day1
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
                show a_day1
                show matt_neut
                d_t "Oh shoot. How did I not see him coming."   
                d "Y- Yes? Oh, g- good morning Matthew."  
                m "What website is that?"
                d "Huh?"
                hide matt_neut
                show matt_mad
                m "I don't remember \"bumming around on forums for conspiracy theorists\" being in your job description."
                d_t "Crap."
                d "Oh that? No, s-sorry I was just taking a quick break."
                hide matt_mad
                show matt_conf
                m "Does this mean you've finally finished the Poster?"
                hide matt_conf
                show matt_neut
                m "It'd better be. We can't have you hand in another Project late."
                m "Or last minute like last time. It's still a miracle to me how you somehow managed to get that one printed in time."
                m "Make sure you're ready ahead of time. I'd highly suggest you print an example latest tomorrow. So we can show it to our clients in time."
                m "Although, today would be much better..."
                d "Sorry..."
                m "Oh, And Sullivan" 
                d "Yes?"
                hide matt_neut
                show matt_mad
                m "With tomorrow I don't mean 6:30PM. The office closes at 7:00PM. If it's not printed by then, you have to figure out how to print it."
                hide matt_mad
                show matt_conf
                m "Is that undersood?"
                d "Yes. Of course. I'll have it in time this time."
                hide matt_conf
                show matt_happy
                m "Great! Now to other matters."
                hide matt_happy
                show matt_neut
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
                hide matt_neut
                show matt_mad
                m "{i}Rather rare opportunity.{/i}"
                hide matt_mad 
                show matt_neut
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
                hide matt_neut
                show matt_happy
                m "Wonderfull. I heard today's menu would offer something special."
                "..."
                d "OH! You meant right now?"
                d "Yes! One second please. I need to. Uhm, finish some last tweeks and save my project really quickly."
                m "Alright. I'll just go ahead. Come meet me in the Cafeteria when you're done"
                d_t "How does he always catch me in the worst moments possible. And here I was looking forward to lunch with gabe and the others"
                d_t "Oh yeah, didn't that screen also say something about food?"
                jump mattlunch
            label mattlunch_n:
                hide matt_neut
                show matt_mad
                m "I'm not really asking Sullivan."
                m "I need to speak with you. Not only about your design."
                d "Sorry. Yes of course. Uhm, I need to finish some last tweeks and save my project. But after that I'll come right away."
                hide matt_mad
                show matt_neut
                m "Fine. I'll just go ahead. Come meet me in the Cafeteria when you're done. Don't make me wait too long. I heard todays menu is promising"
                d_t "How does he always catch me in the worst moments possible. And here I was looking forward to lunch with gabe and the others"
                d_t "Oh yeah, didn't that screen also say something about food?"
                jump mattlunch
            label mattlunch:
                scene bg_office_cafeteria
                show a_day1
                show matt_neut
                d "Mushrooms and mashed potatoes."
                hide matt_neut
                show matt_happy
                m "Looks great doesn't it!"
                d "Yeah..."
                hide matt_happy
                show matt_neut
                m "Being fussy about the food Sullivan?"
                d "No no. It looks delicious. I just had to uhm, figure out what it was first..."
                d_t "God I hate mushrooms."
                m "So, Sullivan. This Poster you're working on. How is it coming along? Do you know if you will be done on time?"
                menu: 
                    "It's going great!":
                        d "Oh yeah, It's going great haha. I'm s-sorry about before. I'm actually almost done."
                        d_t "Please just don't ask about specifics"
                        d "I just have one or two more little graphics to make. And maybe some last minute text editing."
                        m "Will you be able to have it done today? So it can be printed tomorrow."
                        m "I would really prefer you finish it today, so we don't have another situation like last time."
                        hide matt_neut 
                        show matt_conf
                        m "But with the pace you're working at it looks like you won't be able to finish today. "
                        d "No... I'm sorry."
                        d "I'll have it tomorrow evening. Promised"
                        hide matt_conf

                    "About that...":
                        d "Yeah, about that. I don't think I'll be able to finish it today."
                        d "I'll have it in time. I promise. But I've been having some difficulty with the programm lately"
                        m "I would have really prefered you finish it today. Just make sure we don't have another situation like last time."
                        d "Yes I promise."
                        hide matt_neut

                show matt_neut
                m "I hope you can keep that promise."
                "..."
                m "Is something the matter with your plate? You've been poking around in it like you're trying to excavate something."
                hide matt_neut
                show matt_conf
                m "{i} It's starting to make me nervous.{/i}"
                d "S-sorry. I'll stop."
                hide matt_conf
                show matt_neut
                m "Fine. With that settled, I would like to talk to you about this new Job Simon is offering you."
                m "As I mentioned earlier. Someone from his team quit unexpectedly just last week. They are still in the midst of finishing an important project at the moment."
                m "Along with the marketing side of things the clients also requested designs for their upcoming business concept."
                m "With the person in charge of design gone they have really been struggling to pull everything together."
                m "Since the deadline set by the client is in 2 weeks they desperately need someone to fill her place."
                m "And you will be done with your poster soon. {i}I'd hope{/i}. You'd be a good candidate to take the offer."
                m "I have to admit, I'm not too keen on you switching teams already. But Simon insisted I ask you to take the position."
                hide matt_neut
                show matt_conf
                m "Beats me why he would request you specifically but I guess after one year you've had enough time to get into the swing of things here."
                hide matt_conf
                show matt_neut
                m "So, Sullivan. Since you already agreed to taking this opportunity I hope you do your best to adjust to their work flow quickly."
                d "I'll give it my all."
                hide matt_neut
                show matt_happy
                m "Good. Simon will be happy to hear I've found someone."
                hide matt_happy
                show matt_neut
                m "Unlike me, Simon expects a lot more autonomy of his team." 
                d_t "Thank god. Finally some freedom. I can't deal with another controll freak like Matt."
                m "I was reluctant to offer you this position since it seems you still need the supervision. But it can't be helped."
                m "If he insists then I won't tell him otherwhise. Most of the other viable designers are quite busy with their own projects at the moment anyways."
                m "I hope you step up to the job and deliver as demanded."
                hide matt_neut
                show matt_mad
                m "I don't want you to make a bad impression on his team. I'm sure you understand that that would also have very undesirable concequences on my side."
                d "I understand. I won't dissapoint you Matthew. I'm sure having a new work environment will be a great experience for me."
                hide matt_mad
                show matt_conf
                m "Are you saying you don't like my way of doing things?"
                d "No of course not! I just meant it will be good for me to also get a look into how other teams do it around here."
                hide matt_conf
                show matt_neut
                m "Alright. If you say so."
                "..."
                m "You don't seem to be hungry today do you."
                d "Yeahhh, I dont' have that big of an apetite right now."
                d_t "This is so uncomfortable why did he have to do this over lunch."
                m "There's no shame in addmiting you don't like mushrooms Sullivan. Not like your face does't give it away everytime you bite down on one."
                d "He he... Sorry. I just can't stand the texture. I think I'll just get up and go and get myse- oh no!"
                hide matt_neut
                show matt_spill
                "Clank!"
                #The plate flips
                d "OH. I- I'm so sorry Matt..."
                d "Oh no I didn't mean to-"
                m "How-"
                d "I'm sorry I have to go!"
            label printer1:
                scene bg_office_computer
                show a_day1
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
                show a_day1
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
                        show a_day1
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
                        show a_day1
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
                        s "Wow you live there all by yourself?"
                        d "Yes but a friend of mine that also works here actually lives really close as well!"
                        d "I moved in not long after him."
                        s "ou must be in one of the newer ones close to the park then! I've heard only great things about them."
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
                show a_day1
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
                show a_day1
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
                        $ gabe_hints + 1
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
                scene dream2
                x "Please Destiny I'm trying to help you. You have to listen to me"
                d "What?"
                x "I'm not an illusion. I'm here to help you."
                x "It doesn't have to happen to you too."
                d "I-"
                x "I know about your future. I know what you need to do now. I couldn't stop it myself but you can."
                x "He's after you. You have to remember m3."
                d "Who?"
                x "D0n*T oq3n 1 T"
                x "Do-* 4jT F0-_r g*3 T"
                jump morning2
            label morning2:
                scene bg_black
                "Ping!"
                scene bg_d_window
                show a_day2
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
                show a_day2 at right
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
                        "Stick the landing":
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
                        

                        "We meet again old foe":
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

                        "Running, my new hobby!":
                            d_t "Yeah right. Now it's just being unrealistic."
                            d_t "The last thing I want to do is go for a run today."
                            d_t "Does this mean I'll be late for something? I don't have anything planned yet other than finishing my poster."
                            d_t "Maybe I'll be late to printing again. I can't miss the deadline today. I'd better keep a close eye on the time today."
                            d_t "Let's see maybe I can avoid it? Even if not, at least I know now that I'll probably have to run at some point today."
                            d_t "I don't think I'll be enjoying running though, that's for sure. {i}New hobby{/i} yeah right."
                            d_t "I don't know if I can really believe that but I'll definetely put on some more comfortable shoes today."
                            jump achievements2

                        "Dinner for two":
                            d_t "A dinner for two. Huh, at least this one sounds pretty straight forward."
                            d_t "I dont see how this could be anything other than a literal dinner for two people."
                            d_t "Now who could it be with?"
                        
                        "Knock Knock":
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

                        "Start the day":
                            d_t "That's got to be enough for now."
                d_t "It's not a lot of preparation. I'm pretty certain on some of them but why do they have to be so darn vague."
                d_t "And why now of all times? I wish I had more time to figure out where this is all coming from. But I'm neck deep in work right now."
                d_t "Still, there has to be a reason for this right? Let's hope today goes more smoothly than yesterday." 
                d_t "Maybe I'll have some time to be able to figure out why this is happening to me after I'm done with my project"
                d_t "Ughh. Time to get ready for work I guess."
                jump work2
            label work2:
                scene bg_office_computer
                show a_day2
                d_t "Okay! I'm almost done with this darn poster!"
                d_t "I can't allow myself to be distracted now."
                d_t "Although those achievements do make me wonder..."
                d_t "I feel like I've heard someone say something about knowing the future."
                d_t "But who was that?"
                d_t "Did I maybe just read that online somewhere?"
                d_t "Yesterday was so weird too."
                d_t "That one about being watched..."
                d_t "Something is off about it. I don't know why but I get this sinking feeling in my stomach anytime I see that screen."
                d_t "These things it's saying. They looked so inocent but some of them went completely the other way."
                d_t "Who knows maybe this will all clear up today."
                d "No more procrastinating Destiny!"
                d "Time to get this all out of my head and this project done!"
                #htransitiones to after she's done
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
                show a_day2
                show gabe_happy
                g "Oh Hi! Didn't expect to still see you today."
                d "Gabe! Hi."
                hide gabe_happy
                show gabe_conf
                g "Hey, I didn't see you in the cafeteria today. Did you skip lunch to work on the poster?"
                d "Yeah. Heh... I had to crunch a bit. Plus I wanted to minimize my chances of running into Matt. But hey! I got it done!"
                hide gabe_conf
                show gabe_happy
                g "Congrats! No surprises there though haha. I knew you'd get it done on time!"
                g "That's the regular Destiny for you right there. Always a bit last minute. But you never fail to stick the landing somehow!"
                d "Huh!?"
                d "Hold on, what did you just say?"
                hide gabe_happy
                show gabe_conf
                g "Uhm..." 
                g "I just said that I'm amazed how you always stick the landing somehow."
                hide gabe_conf
                show gabe_conc
                g "I meant that as a compliment. I'm sorry did I say something bad?"
                d "Oh, no no! Everything's alright Heh. I didn't catch what you said just then."
                d_t "Does this mean I wasn't overthinking it yesterday?"
                hide gabe_conc
                show gabe_neut
                g "Oh thank god. You looked so shocked. Had me worried there for a second."
                d "I guess I am always a bit fasionably late, eh?"
                d_t "What do I do now? Are all the others also going to come true? It's so late in the day already."
                hide gabe_neut
                show gabe_happy
                g "Late but with the best work!"
                hide gabe_happy
                show gabe_conc
                g "Are you sure everything's fine? You look upset."
                d "Sorry. Really, I'm fine. Don't worry it's nothing."
                d "I was just thinking about how I still have to print it out. And what if the clients don't like it."
                d "Hey, who knows. Maybe this is the one where all of the rushing gets me. Where something goes wrong last minute or it's just not good enough."
                hide gabe_conc
                show gabe_neut
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
                show a_day2
                d_t "Here we are. Alright!"
                d_t "I just have to print this file right here, then I'll finally be done with this."
                "..."
                "Bing!"
                d_t "Oh! That must be my print!"
                d_t "And another win for miss Destiny Sullivan!"
                d_t "Today's going smoother than expected. All that's left now is to drop it off at the meeting room."
                d_t "Maybe I'll actually be able to leave on time today!"
                scene bg_office_cafeteria
                show a_day2
                m "Sullivan!"
                show matt_neut
                d "H-Hey Matthew... long time no see."
                hide matt_neut
                show matt_mad
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
                    hide matt_mad
                    show matt_conf
                    m "Well a scene it was."
                    d "Sorry..."
                    hide matt_conf
                    show matt_mad
                    m "I looked like a darn fool."
                    d "Uhm, I came looking for you to apolagze after I felt a little better. But I couln't find you in the cafeteria anymore."
                    hide matt_mad
                    show matt_conf
                    m "Sure."
                    d "I'm very sorry."
                    d "Really."
                    hide matt_conf
                    show matt_mad
                    m "We will seriously have to talk about your attitude. I understand feeling unwell but nonetheless your behavior was disrespectful and plain rude."
                    d "I-"
                    hide matt_mad

                elif matt_excuse == 2:
                    d "I'm really sorry Matthew. Truly. I didn't mean to just sprint out on you like that."
                    d "I was actually looking for something to help you wipe off the stew from your shirt."
                    m "..."
                    d "I thought I'd run to get some from the washrooms. There's always tissues there."
                    hide matt_mad
                    show matt_conf
                    m "Tissues?"
                    d "Yeah..."
                    m "Really?"
                    d "Uhm, I came looking for you to apolagze and clean up. But I couln't find you in the cafeteria anymore."
                    hide matt_conf
                    show matt_mad
                    m "And you expect me to believe that."
                    d "Sorry. I-"
                    m "We will seriously have to talk about your attitude. I could understand feeling unwell or something like that. But blaitantly lying?"
                    m "This level of disrespect is unacceptable."
                    d "I-"
                    hide matt_mad
                    

                else:
                    d "I- Uhm. I'm sorry. I don't know what got into me."
                    m "That makes the two of us. What posessed you to think storming off would be a good idea?"
                    m "First you ruin my shirt and then you bolt out like that would fix the situation."
                    m "Not only did I look like a darn fool with stew all over his shirt, which i guess can happen. But you also refused to take responsibility for your actions by hiding in some bathroom stall somewhere I presume."
                    d "I-"
                    m "No no. You listen."
                    m "We will seriously have to talk about your attitude. I could understand feeling unwell or something like that. But pulling off a stunt like that and then not even having an explanation for it?"
                    m "This level of disrespect is unacceptable."
                    hide matt_mad



                show matt_neut
                g "Destiny!"
                d "Gabe?"
                hide matt_neut
                show matt_neut at right
                show gabe_neut at left
                g "Oh, afternoon Matthew."
                m "Anderson."
                g "I wasn't expecting to see you two here."
                hide matt_neut 
                show matt_mad at right
                m "My thoughts exactly."
                hide matt_mad
                show matt_neut at right
                g "Actually, Destiny I was looking for you. I have something I have to discuss with you."
                d "Wha-"
                hide matt_neut 
                show matt_mad at right
                m "Actually we are in the middle of a conversation at the moment. So If you'd excuse us."
                hide gabe_neut
                show gabe_conc at left
                g "I'm terribly sorry Matthew. Seems you two are having quite the serious talk but it's something quite personal and urgent."
                g "Could I borrow her for a minute?"
                hide matt_mad
                show matt_conf at right
                m "What could be so important that you need her right this instant?"
                hide gabe_conc
                show gabe_neut at left
                g "Like I said it's a personal matter. But I assure you I wouldn't be barging in like this if it wasn't important."
                d "Gabe, it's alright I'll-"
                hide matt_conf
                show matt_neut at right
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
                hide matt_neut
                show matt_mad at right
                m "Don't think you can get outt of this one so easily."
                d "I'm sorry. Of course."
                d "See you around."
                scene bg_office_hallway
                show a_day2
                show gabe_neut
                g "Phew! That was a close one. Looked like Matt was really out for blood this time. Looks like he took it quite personally"
                d "Oh yeah 100 percent. I was scared he was about to end my carreer right there on the spot."
                d "I'm done for. He's going to fire me!"
                g "Hey, take a deep breath. Surely they're not going to fire you."
                hide gabe_neut
                show gabe_conf
                g "I'm pretty certain he can't do that just because of one incident. Higherups have to look over things like that. And an accident happen you know."
                hide gabe_conf
                show gabe_neut
                d "How are you not scared of him?"
                d "I was about to cry. I could have never stood up to him like that."
                g "Oh hes not that scary. He's more like a dog."
                hide gabe_neut
                show gabe_happy
                g "All bark no bite."
                hide gabe_happy
                show gabe_neut
                g "He talks a lot and likes to pressure people but other than being mean he rarely does anything really."
                g "Besides what's he got on me? I just needed to talk to you about something important. The worst he could have done was refuse to let me talk to you."
                d "I don't know how you do it. Wow."
                d "Speaking of it. What did you want to talk to me about?"
                g "Oh, uhm nothing if I'm being honest. I didn't want you getting mauled out by Matt."
                hide gabe_neut
                show gabe_happy
                g "Saving a friend from a ferral creature sounds personal and urgent enought to me."
                d "Tell that to Matt haha."
                hide gabe_happy
                show gabe_neut
                g "Seems i came at exactly the right moment."
                g "Well, I was actually looking for you."
                d "Oh?"
                g "I forgot to ask you something before."
                g "Would be interested in making dinner together again tonight."
                hide gabe_neut
                show gabe_happy
                g "You know. To celebrate you finally being done with this poster."
                hide gabe_happy
                show gabe_neut
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
                        hide gabe_neut
                        show gabe_happy
                        g "Great! I've already got something in mind we could make. I have almost everything at home too."
                        d "Ohhh, sounds promising. What is it?"
                        g "It's a surprise but I'm sure you'll like it!"
                        hide gabe_happy
                        show gabe_neut
                        g "I'm actually already done for today so I can go get the last few ingredients on my way home."
                        d "I still have to get this to the conference room and clean up a bit around my desk. How about we meet at my place at 7:00PM?"
                        g "Works for me."
                        hide gabe_neut
                        show gabe_happy
                        g "See you at 7 then!"
                        d "Seeya."
                        hide gabe_happy

                    "Make up an excuse.":
                        $ dinner_plans = False
                        d_t "I'm sorry Gabe. But this might be my only chance at finding out what this all means."
                        d "I'd love to... but, I'm just so tired and exhausted from the last few days."
                        d "I barely got any sleep yesterday and I think I'd better just go to bed extra early today."
                        d "Let's do something on the weekend! I doubt I'd be fun company right now. I want to actually be able to help you in the kitchen when we do it haha. "
                        d "I think today I'd just doze off every couple of minutes."
                        hide gabe_neut
                        show gabe_happy
                        g "Oh, Of course! I understand. Get some rest today. You've deserved it." 
                        d "Thanks."
                        hide gabe_happy
                        show gabe_conf
                        g "Does Saturday night sound good? I don't have any plans over the weekend so whenever's good"
                        d "No no, Saturday sounds great. For sure!"
                        hide gabe_conf
                        show gabe_happy
                        g "Nice. I'm actually already done for today so I'll catch you tomorrow for lunch?"
                        d "Yeah, of course. The table in the back, as usual."
                        hide gabe_happy
                        show gabe_neut
                        g "Exactly."
                        g "Have a nice evening then Destiny!"
                        g "And go to bed extra early today."
                        d "I will! Thank you."
                        d "See you tomorrow."
                        g "Seeya."   
                jump running
            label printer2unfixed:
                scene bg_office_printer
                show a_day2
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
                show a_day2
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
                show a_day2
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
                s "Do you live somewhere around here? This area is one of the best if you're working in the city."
                d "Yeah. I moved into one of the newer appartment complexes just two stops away."
                s "You live there all by your self?"
                d "No no, actually, a good friend of mine who also works here lives really close as well!"
                d "I moved in shortly after him."
                s "Wow, you must be in the ones close to the park then. I've heard only great things about them."
                s "How do you like the area? In my oppinion it's one of the best. Especially if you work in the city."
                d "I like it a lot actually! I have a great view of the park and the city from my appartment. And my neighbours are fantastic."
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
                show a_day2
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
                    d_t "UGH. That doesn't mean it's going to be fun!"
                    jump dinnerfor2gabe
                else:
                    d_t "Oh well, it can't be helped. At least I get to finally go home now."
                    scene bg_street
                    show a_day2
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
                    show a_day2
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
                    d_t "Creepy... "
                    d_t "Why do I feel like I'm being watched?"
                    d "Is this where you live?"
                    c "Mwrrm"
                    d "Hmmm, I can't just leave you here now... This place reaks. {i}And something is very off about it.{/i}"
                    d "How about we try to find your owner!"
                    d "{i}If you even have one{/i}"
                    d_t "It's late already."
                    "Rustle"
                    hide a_day2
                    show a_day2_run
                    d "-"
                    hide a_day2_run
                    show a_day2
                    d "Yeah, no. I'm not staying here any longer than I need to."
                    d "We'll try to find them tomorrow, for now you're coming with me. What do you say little guy?"
                    c "Meowww!"
                    d "Ha ha. You're adorable ehm-"
                    python:
                        catname = renpy.input("What should I call you?", length=15)
                        catname = catname.strip()

                        if not catname:
                            catname = "Kitty"
                    d "[catname]!"
                    d "Let's get you cleaned up [catname]."
                    "Clank!"
                    #screen glitches to just RUN for a sec
                    d "!"
                    d "What was that? Did that just say-"
                    d "Oh we have to get out of here ASAP. That's freaking creepy."
                    d "This place is starting to give me the chills."
                    jump dinnerfor2cat
            label dinnerfor2gabe:
                scene bg_d_corridor
                show a_day2
                g "Hey! It's me Gabe!"
                d "One second, be right there!"
                show gabe_neut
                g "So, want to get to cooking? I brought all the ingredients."
                d "Yes! Let's go."
                scene bg_d_kitchen
                show a_day2
                show gabe_neut
                g "I brought everything we need to make your favorite noodle soup!"
                d "You know me too well! Thank you so much Gabriel!"
                hide gabe_neut
                show gabe_happy
                g "Please, it's nothing."
                hide gabe_happy
                show gabe_neut
                g "How about I start with preparing the broth? Then you can already get to chopping the vegetables."
                d "Perfect."
                #Skips to right before they're done.
                "*Knock Knock*"
                d "Shoot! Gabe can you go see who it is quickly? I just put the chicken in the pan."
                g "Yeah of course. One second."
                hide gabe_neut
                #Achievements glitch but no altered text
                g "Huh? Doesn't seem to be anyone there!"
                g "I'll have a look if they're still outside!"
                #Achievements glitch but no altered text
                d_t "Oh right! The knocking. I wonder who it is."
                show gabe_conf
                g "Weird. There wasn't anyone outside. I checked the hallway but I couldn't see anyone there either."
                d "Strange."
                d "It was probably just some doordashers. My neighbour recently mentioned something like that."
                g "Possible."
                g "I wouldn't put it past those little kids from floor 2 to go around pranking people."
                d "Tell me about it. I always hear them screaming and running around when I get back from work."
                d "Hey! The soup's almost done! Want to hand me those spring onions you chopped?"
                g "Here. I'll go set the table."
                #skips to after theyve eaten.
                
    
                jump day3
            label dinnerfor2cat:
                scene bg_d_kitchen
                show a_day2
                d "Alrighty! Here we are."
                c_n "mrrr"
                d "Make yourself at home [catname]."
                d "But don't you dare go around destroying things alright?"
                c_n "Meowww!"
                d "What's the matter?"
                d "Oh! You must be hungry! Let's see what I have for you."
                d "Hmmm. Looks like I have some tuna in my pantry."
                d "Do you like tuna?"
                c_n "MEEEwr!"
                d "Haha, someone's enthusiastic!"
                d "Let me get a plate to put it on."
                d "Wow, now that I'm thinking about it, I'm starving too!"
                d "I barely had anything to eat today."
                d "And you had me running around half the block."
                d "Time to make myself some dinner too, no?"
                d "Since the can's already open, how about a tuna sandwich?"
                c_n "Prrrr"
                d "Now that's a happy cat. Here [catname], enjoy."
                d "You're really taking care of the achievements for me today..."
                d_t "And here I thought I could actually evade them for once."
                d_t "This isn't quite what I imagined when I read \"Dinner for two\""
                d_t "But I suppose that's to be expected by now. It's not like they were any more straight forward yesterday."
                c_n "MreEEEau"
                d "Done already?"
                d "You must have been starving!"
                d "Here, let me just take that plate over to the sink so I can wash it later."
                "*Knock Knock*"
                d_t "Huh?"
                d_t "I'm not expecting anyone."
                d_t "Oh right. The last achievement.\"knock knock\""
                c_n "Mrrauw?"
                d "It's alright."
                d "You stay here [catname]."
                scene bg_d_corridor
                show a_day2
                d_t "Who it could be-"
                hide a_day2
                show a_day2_dontopen
                #Achievements glitch to Don't open the door.
                d "!"
                d_t "Wh- What was that?"
                d_t "-"
                d_t "No, I must have just imagined it. I'll just look who's outside the door."
                #look outside (noone)
                d_t "What in the...?"
                d_t "Did they leave already?"
                d_t "Maybe they-, I cant see from here I'll have to go and check-"
                c_n "HSSSr!"
                hide a_day2_dontopen
                show a_day2_dont
                #screen permanently glitches to DONT
                d_t "EHM?" 
                d_t "WHAT!?"
                d_t "Wh- What is THAT? How is it-"
                d_t "I knew I saw something!"
                #Glitches to dont open it. and be quiet
                c_n "mEEEwr"
                d_t "What the F-"
                d "{i}Shhh. [catname] it's ok. Quiet.{/i}"
                c "{i}mrrrr{/i}"
                d "{i}What is this?{/i}"
                menu:
                    "Open the door.":
                        $ open_door= True
                        d "Screw it I'm not going to be scared by that stupid screen!"
                        d "You can't tell me what to do."
                        #Opens door
                        #Achievements permanently glitch unreadable
                        d "He- Hello? Is someone there?"
                        "..."
                        d "No one?"
                        d_t "..."
                        d_t "They didn't leave anything either..."
                        d_t "No package, no letter."
                        d "Hello?!"
                        "..."
                        d_t "Nothing..."
                        #goes back in
                        c_n "HrshSSSS"
                        d "What's wrong [catname]? There's no one there."
                        c_n "Meowww!"
                        d "You're right let's go back."
                        d "This is rediculous. This whole thing is starting to scare the heck out of me."
                        d "This stupid screen told me to keep the door closed but there was no one there."
                        d "What is it trying to keep me from?"
                        d_t "Who?"
                        d "Why does the text suddenly start changing now!?"
                        c_n "mEEEwr"
                        d "Ok ok I'm coming. I want to get away from that door just as much as you do."
                        d_t "Who was that?"
                        d_t "What does that weird screen know that I don't?"
                        d "That door staying closed for the rest of the night."
                        d_t "And locked for as long as possible."

                    "Keep it closed":
                        d_t "Oh hell no! What the hell is going on!?"
                        d_t "I'm not opening that door."
                        d_t "This is crazy!"
                        d_t "Why does the text suddenly start changing now?"
                        d_t "Who was that?!"
                        d_t "What does this-"
                        #Glitches to stay inside. Don't go out again.
                        d_t "I- I"
                        d_t "Why is this happening to me?"
                        d_t "What is it trying to keep me from?"
                        d_t "Who?"
                        d_t "I-"
                        c_n "mrrwm"
                        d "[catname]?"
                        c_n "Meow"
                        d "I'm sorry [catname], l-let's go back."
                        d_t "And keep that door locked for as long as possible."
                jump day3
    #DAY 3
    label day3:
        label dream3:
            scene dream3
            x "He was here!" 
            d "Who was-"
            x "You can't trust him Destiny! You have to stay away from him. He's dangerous."
            d "Who are you!?"
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
            d "No, don't go!"
            x "-"
            jump morning3
        label morning3:
            scene bg_black
            "Ping!"
            if dinner_plans==False:
                scene bg_d_window
                show a_day3
                d "AH!"
                d "Not again!"
                d "It's the girl from last time!"
                d_t "I knew there was something stragne about that dream yesterday."
                d_t "Didn't it mention something about knowing what is going to happen?"
                d_t "No. I can't forget it this time!"
                d_t "She was trying to tell me something. Warn me. Something like he was here..."
                d_t "That's right! She said I coulnd't trust him and that he was here."
                d_t "Yesterday? The knocking?"
                d_t "Who was here? Urgh why is this so hard to remember. She must have meant the knocking"
                d_t "..."
                d_t "Get help..."
                d_t "I should... get help?"
                d_t "Who is this person?"
                d "!"
                d "The achievements!"
                #look at achievements
                d_t "\"Make the right call\""
                d_t "The girl in my dream said I should get help. Does that mean call for help?"
                d_t "Are these achievements and those strange dreams connected?"
                d_t "She was saying someone was here. And the screen knew that too. Am I going crazy?"
                d_t "This has to be connected somehow. Maybe I can figure out what is causing both and finally make it go away."
                d_t "I don't even feel safe in my own home anymore."
                d_t "I thought it might just be in my head. But that knocking yesterday was real."
                d_t "What if she was right and there really was someone here?"
                d_t "I think I should call someone..."
                menu:
                    "Call Gabriel.":
                        jump callgabealone
                    "Call the police.":
                        $ call_police= True
                        jump callpolice
            else:
                d "AH!"
                d "Not again!"
                d "It's the girl from last time!"
                d_t "I knew there was something stragne about that dream yesterday."
                d_t "Didn't it mention something about knowing what is going to happen?"
                d_t "No. I can't forget it this time!"
                d_t "She was trying to tell me something. Warn me. Something like he was here..."
                d_t "Who was here?"
                d_t "Gabe? Gabe was here. But he's here all the time. Maybe she meant the knocking?"
                d_t "Argh why is this so hard to remember. She said something else too."
                d_t "What was it..."
                d_t "He's dangerous..."
                d_t "Oh. Right... She said something about him trying to get close to me."
                d_t "That he's dangerous..."
                d_t "She can't have meant Gabriel right? He was here to help."
                d_t "He saw that I wa stressed and wanted to help me."
                d_t "And the dinner yesterday was so nice."
                d_t "Ugh, why am I even thinking about this so much. It was just a stupid dream."
                d "!"
                d "The achievements!"
                d_t "Right! They'll still tell me what's going to happen!"
                d_t "Eh, creepy..."
                d_t "Let's see here."
                #look at achievements
                d_t "\"Make the right call\""
                d_t "Well I was planning on calling Gabriel anyways. Sounds like that's exactly the right idea!"
                jump callgabedinner
        label callgabedinner:
            "Click"
            g "Oh hi Destiny! What a surprise to hear form you so early. It's not even 7 yet."
            d "Hi Gabe. Sorry, I didn't realize it was still so early. Did I wake you?"
            g "No no, dont worry. What's up?"
            d "Not much actually. I just had a weird dream. But anyways. I was just wondering if you'll be there at the office gettogether?"
            g "Oh! Yeah for sure. I don't have any other plans yet so I'll probably come by."
            g "Do you want to meet up later and go together?"
            d "I was just about to ask that. I think I'll need a little support to stand a chance agains Matthew today."
            g "Ouch. I almost forgot. Yeah he's still out to get you isn't he?"
            d "Oh yeah. Maybe I can avoid him a little from now on though. I'm starting on Simons team today remember?"
            g "Right! I hope that goes well for you. But I'm sure you'll fit in great."
            d "Thank you Gabe! I'll do my best."
            g "Hey, since I'm already up now I'll probably try to get a little work done before going in to the office."
            g "Talk to you later then?"
            d "Of course. See you Gabe."
            g "Bye Destiny."
            "Click"
            d_t "See, he's so sweet. I don't know what I was thinking. I just have to clear my head. These dreams are getting a little under my skin."
            d_t "Are they connected to the achievemnts somehow?"
            d_t "I mean they did show up around the same time..."
            d_t "Oh yeah! Speaking of achievements. Let's check what's in store for today."
            jump achievements3
        label callgabealone:
            $ gabe_hints + 1
            "Click"
            g "Oh hi Destiny! What a surprise to hear form you so early. It's not even 7 yet."
            d "Hi Gabe. Sorry, I didn't realize it was still so early. Did I wake you?"
            g "No no, dont worry. What's up?"
            d "I'm so glad to hear your voice right now. Yesterday was just... I'm scared Gabe."
            g "Whoa whoa! Hold on, what's wrong Destiny? Did something happen?!"
            d "I- I feel like someone followed me home yesterday."
            d "I heard knocking but then there was no one there. I-, what if someone wanted to get into my apartment?"
            g "Destiny, wait. Give me 3 minutes and I'll be there. Then we can talk about this in person ok?"
            d "Yeah, thank you Gabe..."
            g "Alright be right there."
            "Click"
            #A couple minutes later
            scene bg_d_kitchen
            show a_day3
            show gabe_conc
            g "Ok, ok so, did I hear that correctly. You think someone followed you here and tried knocking on your door?"
            d "Yeah..."
            d "Yesterday I had to chase after this cat into a really creepy ally after it grabbed one of my papers."
            d "[catname] is actually still sleeping over there. But when I finally got them back I felt like I was being watched."
            d "There was this weird noise like something was being moved or pushed over so I got out of there as quickly as possible."
            d "But then after I got home and made dinner for me and [catname] someone knocked on my door."
            d "I went to check who it was but there was no one there..."
            d "I know I sound crazy but I'm so scared."
            hide gabe_conc
            show gabe_neut
            g "No, you don't sound crazy at all Destiny."
            hide gabe_neut
            show gabe_conc
            g "Did you see anyone in the ally?"
            d "No."
            hide gabe_conc
            show gabe_conf
            g "And you didn't see anyone outside your door either?"
            d "No, there was no one."
            d "See this is what I meant with crazy."
            hide gabe_conf
            show gabe_neut
            g "Hmmm. Is it possible the cat, uhm what did you say the name was? [catname]? Is it possible [catname] made that noise?"
            d "I- I don't know."
            d_t "Ugh this shouldn't be scaring me this much."
            d_t "If only it wasn't for those horrible dreams and the glitches yesterday."
            d "I'm sorry Gabe, I know I shouldn't be so scared because something like that it's just that-"
            d "That-"
            d "Nevermind. It's stupid!"
            hide gabe_neut
            show gabe_conc
            g "Destiny. You can tell me what's wrong."
            g "If you tell me what's bothering you so much I might be able to help you."
            g "You're clearly very upset over all of this."
            g "I promise you, whatever it is, we can figure it out together. I don't think you're stupid."
            menu:
                "Tell him about the dreams": 
                    $ gabe_hints + 1
                    d "This is going to sound insane but. I've been having these weird dreams lately"
                    d "Every morning when I wake up I can remember seeing this girl, talking to me, warning me."
                    d "She looks scared."
                    d "I think I've seen her before somewhere but I for the life of me can't figure out who she is."
                    g "What does she tell you?"
                    d "Every night she tells me something like \"{i}He's dangerous{/i}\" or \"{i}}He's trying to get you{/i}\""
                    d "I have no idea who {i}He{/i} is but it's scaring me."
                    d "Wh- when I woke up this moring I could remember her saying that {i}He was here{/i}"
                    d "Someone clearly was here. A-and I don't know who it was but she keeps saying that he's dangerous and that I need to get away from him."
                    d "Gabe all of this is scaring me."
                    g "Take a deep breath Destiny. Everything is going to be alright. We're going to figure this out ok?"
                    d "Do you think I'm crazy?"
                    g "No. I don't think you're crazy Destiny."
                    g "I think you've had a lot to deal with yesterday and a lot of stress on top of that lately."
                    g "For what it's worth I would be scared too if I had dreams like that after someone knocks on my door."
                    g "Did you see anything weird when you checked the door?"
                    d "No. Nothing"
                    g "Maybe all of this is just a weird coincidence."
                    d "You think?"
                    g "Could be. I mean can you think of someone who would want to hurt you?"
                    d "Not really..."
                    g "But those dreams do sound strange."
                    g "Have you ever had anything like this happen before?"
                    g "The dreams I mean."
                    d "Dreams that tied into things that happened?"
                    g "Yeah something like that."
                    d "Maybe. I ususally don't remember my dreams all that well."
                    g "You know, sometimes when we think about something a lot during the day or something is is bothering us it can show up in our dreams." 
                    g "I've definetely had that before."
                    g "I was so worked up about something the netire day that I even dreamed about it that night."
                    d "You think this knocking yesterday might've just scared me enough so I dreamt about it?"
                    g "Exactly! That doesn't explain how you've been dreaming about her the past few days though..."
                    d "I'm sorry Gabriel, this is so stupid. You're probably right. I'm blowing this way too out of proportion."
                    g "No, no it's ok. Really."
                    g "But how about you try to relax a bit the next couple of days to see if it gets better."
                    g "And if you want I can come over more often so you won't have to be as sacred that someone is going to follow you while you're alone."
                    d "Thank you so much Gabe. I think I would really appreciate that."
                    g "Any day! Besides then I'll get to see [catname] a little more"
                    g "They look adorable!"
                    d "Haha. They are!"
                    g "You just let me know whenever you feel like something strange or creepy is going on ok?"
                    d "Yes. Thank you Gabriel."

                "Avoid the dreams":
                    d "Really it's nothing. I'm just beating myself up for being so creeped out by all of this."
                    d "I don't ususally get frightened so easily so I'm just confused why this is hitting me so hard right now."
                    d "I feel crazy for even thinking someone followed me here."
                    g "I don't think you're crazy Destiny."
                    g "I think you've had a lot to deal with yesterday and a lot of stress on top of that lately."
                    g "For what it's worth I would be scared too if I felt like someone was watching me and heard knocks on my door that night."
                    d "Yeah..."
                    g "Did you see anything weird when you checked the door?"
                    d "No. Nothing"
                    g "I'm sure this is all just a weird coincidence."
                    d "I know. Sorry"
                    g "Don't be! It's ok to get scared. You don't have to be ashamed of getting spooked."
                    g "But If you want I can come over a bit more in the next couple of days so you don't have to be in here all alone."
                    g "Well."
                    g "Other than with [catname] of course."
                    g "They look adorable!"
                    d "Haha. They are!"
                    g "You just let me know whenever you feel like something strange or creepy is going on ok?"
                    d "Yes. Thank you Gabriel."

            g "Do you think you've calmed down enough to get ready for work?"
            d "Oh right. Yeah I think so."
            g "Great. Because I havent had time to put on my shoes yet... so I'll head back now if thats ok."
            d "Huh?"
            d "HAH! you came here in your socks?"
            g "Maybe..."
            g "Hey, those 3 minutes wouldn't have been enough for shoes."
            d "Alright alright. Go get ready too. I'm glad you came over."
            scene bg_d_corridor
            show a_day3
            g "And remember Destiny. If you feel like you're being watched again feel free to call me."
            d "I will. Thanks. I don't know if I would have been able to calm down all by myself."
            g "Glad to have helped."
            g "See you later?"
            d "See you later."
            scene bg_d_kitchen
            show a_day3
            c_n "Mrrrr"
            d "Oh hey there [catname]."
            d "Did you atleast sleep a little better than I did?"
            c_n "Prrrrrrrr"
            d "Sounds like a yes to me. I'll go look for your home today dont worry."
            d_t "Right after I've taken a look at the other achievements for today."
            jump achievements3

        label callpolice:
            "Click"
            o "Hello? Officer Rogan speaking. How may I help you today?"
            d "H- Hello officer. My name is D-destiny Sullivan. I, Uhm, I'm very sorry to bother you with something like this."
            d "But I have the feeling someone might have followed me to my apartment yesterday."
            d "I-I heard knocking but when I checked no one was there."
            o "Alright miss Sullivan. Let's take a deep breath. Where do you live currently?"
            d "Ehm, I live at Parkerstreet 7. In that big apartment-building, oh er-, on floor 3."
            o "Thank you very much. And what makes you believe you were followed"
            d "It's hard to explain b-but on my way home I had to chase after a stray that had gotten hold of some of my documents."
            d "And after I followed it into an empty ally, I uhm, was starting to get the feeling that I was being watched."
            o "Please continue. What caused that feeling of being watched? Did you see anyone or hear something?"
            d "There was just this thud, like something had been knocked over. Maybe a can."
            d "And, and then that knocking. I- I'm scared someone might have followed me home."
            o "Alright madam, it sounds to me like the knocking you heard might have been a nasty prank or something of the sort. But I understand your concern."
            o "We have had a similar complaint just recently so we will make sure to look into it."
            d "Huh? Someone had this happen too?"
            o "Yes, it seems. I checked the report about your neighbourhood and we have actually had a person reported missing in the last couple of days."
            o "Don't worry, there is already an officer stationed nearby and I will make sure to assign someone to keep a closer eye on your street and building from now on."
            d "Oh, Th- Thank you."
            o "Thank you for notifying us miss Sullivan. It is possible that the knocking might be connected to the recent dissapearence."
            d "You think?"
            o "If I might ask madam. Did you perhaps catch a glance at who might have caused the noise you heard or the person that was knocking at your door?"
            o "If these two incidences really are connected it would be of great help to us to have a description of the person that you suspect might have followed you."
            d "Oh, Uhm. No, I'm sorry. I, I didn't see anyone. At least not that I could remember."
            o "Not to worry miss Sullivan, we are keeping an eye on you, so you can go about your as usual for now."
            o "We would advise however, that you avoid entering more secluded places or walking alone. And of course, you should stay attentive and notify us if there are any more strange occurrences."
            d "Sure. I will call you if I notice anything."
            o "I understand this must be quite a frightning situation for you but we are doing our best to keep you safe."
            d "Thank you officer."
            o "No worries madam. We will also make sure to let you know as soon as we know more."
            o "But for now I hope you have a pleasant and uneventful day miss Sullivan."
            d "Yes."
            d "Again, thank you so much officer. Goodbye."
            "Click"
            d_t "..."
            d_t "Wow..."
            d_t "I think I need a minute."
            d "!"
            c_n "Mrrrr"
            d "Oh hey there [catname]."
            d "Did you atleast sleep a little better than I did?"
            c_n "Prrrrrrrr"
            d "Well at least one of us did..."
            d "Don't worry I promise I'll go looking for your home today."
            d_t "After I've processed what that officer just told me."
            d_t "Oh."
            d_t "And I still have the achievements to check..."
            jump achievements3
                
        label achievements3:
            d_t "One more look at today's achievements..."
            d_t "I can't avoid these can I?"
            d_t "The theory's been thuroughly tested by now I'd say."
            d_t "I didn't have too much time to look at them the past two days though."
            d_t "Maybe third time's the charm."
            d_t "I've got more than enough time to figure out what they mean now anyways."
            d_t "Where should I start."
        label achievements3menu:
            menu:               
                "Restart":
                    d_t "Playing in to the game feeling aren't we."
                    d_t "I could use a restart though..."
                    if dinner_plans == False:
                        d_t "Not just at work. If restarting meant this weird screen and horrible dreams would go away I'd take it in a heartbeat."
                        d_t "As nice as that sounds, I doubt that's actually going to happen."
                    else:
                        pass
                    d_t "I am starting with a new project."
                    d_t "And meeting a new team too."
                    d_t "That's already something. Definitely a restart there. Is there anything else \"Restart\" could mean?"
                    d_t "Ok it could also be quite literal. Refering to restarting a computer or some other device."
                    d_t "Or maybe I mess something up and have to restart..."
                    d_t "That does sound like me..."
                    d_t "Hmmm"
                    d_t "Since I already know I'll be interduced to the new project and team today I don't think it's too unreasonable to assume it's going to be that."
                    d_t "It's pretty safe to bet on that."
                    d_t "But I'm sure it won't hurt to be prepared if I have to start over on something. Like planning in a little extra time for any important tasks I have to do today."
                    jump achievements3menu

                "Ignorance is bliss":
                    if dinner_plans == False:
                        d_t "Great another ominous one. As if I wasn't already creeped out enough."
                        d_t "Could this have something to do with finding out about who was at my door yesterday?"
                        d_t "Or maybe something about the dreams?"
                        d_t "No, I think I wouldn't regret knowing about that. It has to be something else."
                    else:
                        d_t "Great another ominous one. As if I wasn't already creeped out enough."
                        d_t "What do I not know, but don't want to know?"
                        d_t "This could be anything again couldn't it."
                        d_t "Where am I trying to be ignorant?"
                        d_t "Maybe I find out something about these achievements or these dreams."
                        d_t "Or maybe I don't and that's the whole point?"

                    d_t "In any case, I'm probably going to be in a situation in which I don't or didn't know something."
                    d_t "The phrasing that ignorance is bliss is making me hope it's nothing to do with all of the strange happenings recently."
                    d_t "I'd rather not think about all the horrible things that could come with having a floating screen telling me about my future."
                    d_t "What if it predicts an accident or something worse..."
                    d_t "..."
                    d_t "No, now I'm scaring myself."
                    d_t "I should just try to find out what the other achievemnts mean. If I really am Ignorant now then I can't even know about what it would be so why try?"
                    d_t "I'll just have to see what comes. Then I can still decide what I do with that information."
                    jump achievements3menu

                "Hands up everyone":
                    d_t "Hands up?"
                    d_t "As in the police kind of hands up or the party kind of hands up?"
                    if call_police == True:
                        d_t "Well I did call the police."
                        d_t "Are they going to arrest someone?"
                        d_t "Oh god this is making me nervous. Are they going to come to the office?"
                        d_t "I hope it was the right decision to tell the police about this..."
                        d_t "What if I'm just overreacting and now I've just made the mess even bigger."
                        d_t "No! It was the right call! They'll help keep me safe."
                    else:
                        d_t "There's that party at the office today..."
                        d_t "Maybe we'll have something to celebrate about."
                        d_t "That would be a nice change of pace."
                        d_t "I hope it's not the police."
                        d_t "Hands... It sounds like this is about multiple people. If it's trying to warn me about the police, they'd have to come to the office right?"
                        d_t "With the timing and all."
                        d_t "..."
                        d_t "A robbery?"
                        d_t "Ok, no. Now I'm just making up things. I doubt anyone would come to a marketing firm to steal anything."
                        d_t "Not that we'd have anything to steal in the first place."
                        jump achievements3menu

                "Where is waldo?":
                    d_t "\"Where is waldo\". Isn't that the kids book where you have to find the striped man?"
                    d_t "What does this have to do with anything?"
                    if dinner_plans==False:
                        d_t "Could I be looking for that guy that the girl said at my door?"
                        d_t "Waldo is probably someone else."
                        d_t "Waldo hides in plain sight right?"
                        d_t "Oh no. Is am I going to have to look for someone in a crowd somewhere?"
                        d_t "What if it is that man though"
                        d_t "The party tonight..."
                        d_t "Anyone could be hiding in plain sight."
                        d_t "I'll have to be extra careful."
                        d_t "But what should I even be looking out for? If it really is the same person that knocked then I'm screwed."
                        d_t "I don't even know what the darn guy looks like."
                        d_t "It's not like he's going to show up in a red and white striped shirt."
                        d_t "Definitely not. Why does it always tell me things in the most obscure way possible."
                        d_t "Waldo. Stupid kids book. Like that's actually going to give me anything to work with."
                        d_t "Great sense of humor it's got there."
                        d_t "If it wasn't for it's insane accuracy and scary messages I'd say it's just trying to mess with me."
                    else:
                        d_t "Am I going to lose someone in a crowd?"
                        d_t "It's possible. There's going to be a lot of people at the office party tonight."
                        d_t "Maybe I'll have to look for Gabe sometime during the event."
                        d_t "I guess this just means I'll have to keep an extra eye on him."
                        jump achievements3menu
                "Start the day":
                    pass
            d_t "Why do I always feel dumber after looking at these?"
            d_t "Checking them yesterday helped a little but I still got surprised by some. I hope today will be better."
            d_t "I should get ready to go now. If I'm there a little early I can get a head start on whatever it is Simon will have me work on from now on."
            if dinner_plans== False:
                c_n "Meooow"
                d "Don't worry [catname]. I haven't forgotten about you either. Let's get you something to eat. What do you say?"
                c_n "MRRREW"
                d "Oh wow. You're so energetic today!"
                d "I'll have to look for your owners tomorrow I'm sorry. I completely forgot that we have that dinner tonight."
                d "I'm sure we'll find them eventually."
                d "I'll make sure to bring home some tasty cat food though. Promise."
                c_n "Prrrr"
            else:
                pass
            jump work3
        label work3:
            scene bg_office_hallway
            show a_day3
            d "Hey Simon!"
            s "Oh! Hi there Destiny!"
            s "Wow, you came in real early. I think you've got to be the first one here today."
            s "It's only your first day and you're already outdoing the entire team!"
            d "Haha, no no it's nothing like that. I just didn't want to be late on my first day on the team that's all."
            d "And besides I woke up really early today anyways. Might as well just go to work you know."
            s "I see. I'm just teasing you don't worry."
            d "You're here too! You look a little tired though. Do you always get here so early."
            s "Well I did get home quite late yesterday, so I am a bit tired. But yes I usually try to come in a little earlier than everyone so I can plan out the meetings and such for the day."
            s "I just got here though. You almost beat me to it!"
            s "I have to admit I am quite impressed. It's great having such an ambitious personality on our team again."
            s "I'm sure your fresh motivation will rub off on the others."
            s "You're very simmilar to Kai in that way actually."
            d "Really?"
            s "Yeah. She was also usually the first one to come in funnily enough. And she always had this relentless optimism."
            s "It's like something's been missing since she left..."
            s "But I see Matthew found the perfect replacement for me!"
            d "Wow. I hope I can fill such big shoes!"
            d "It sounds like everyone really liked her. I'll try my best to live up to the expectations haha."
            d "The more I hear about her the more I'm getting curious why she's quit. It sounds like she really found her place here."
            s "Yeah, it was a shock to us all. She just came in one morning and told me she was done."
            s "I tried asking her why but the next day she didn't come in anymore."
            d "Strange."
            s "I heard she went to talk to Matthew but it doesn't look like he was able to change her mind."
            s "We still have her desk set up and everything..."
            s "Actually! That brings me to our next to do."
            s "It's no use to dwell on the past now."
            s "Since Kai already started on the designs you will be working on I thought it would be a good idea for you to take over her desk."
            s "You can pick up right where she left off!"
            s "She still has all of her files and notes over there. You should be able to find everything on her computer or somewhere on the desk."
            s "I haven't really had time to take a look at everything yet but since you'll be working on those designs anyways I thought it would be a perfect way to start for you."
            s "That way you can jump right in by taking a look at everything and familiarising yourself with the style of work she's done so far."
            s "From what I've seen you should be able to pull it off with ease."
            d "You want me to take her desk? I can still work at my old one that's fine I have everything set up there it's really not a problem."
            s "No no. Please I insist. It'd be easier. She's got everything you need."
            d "If you say so! That sounds great."
            d "I'm sure looking at her work will help me to get a clear idea of what it is I have to do."
            d "I have to admit, I don't think I've seen any of her work yet. So I'm really looking forward to finding out what she's done already."
            s "Fantastic!"
            s "In that case what are we waiting for!"
            s "I'll show you to your new desk and you can get cracking at it."
            s "It's just over there. Right next to my office."
            s "I'll be here almost the entire day so if you have any questions or any trouble feel free to come over and let me know."
            s "I am busy over lunch but I'll stop by in the afternoon again to see how things are going."
            s "Does that sound alright with you?"
            d "Yes, definetly. Thank you so much Simon."
            s "It's no trouble. I'm just making sure you feel welcome as our new member."
            s "Alright, I'll leave you to it now. Again, if anything should be the matter hit me up."
            d "Of course. In that case I'll see you later then."
            scene bg_office_computer_kai
            show a_day3
            d_t "Wow, this desk is nice. There's so much to look at. She really didn't take anything with her."
            d_t "I should try to take a look at everything."
            d_t "But what should I look at first?"
            default deskfold_c= False
            default deskcomp_c= False
            default deskcard_c= False

            label kaidesk:
                if deskfold_c== True and deskcomp_c== True and deskcard_c== True:
                    jump kaideskdone
                else:
                    menu:
                        "Folder":
                            $ deskfolderc = True
                            jump deskfold
                        "Computer":
                            $ deskfolderc = True
                            jump deskcomp
                        "Postcard":
                            $ deskfolderc = True
                            jump deskcard
            label kaideskdone:
                menu:
                    "Folder":
                        jump deskfold
                    "Computer":
                        jump deskcomp
                    "Postcard":
                        jump deskcard
                    "Finish looking":
                        jump donewithdesk
            label deskfolder:
                d_t "Simon said she kept some of her designs in this folder."
                d_t "I'm curious to see what her style is like."
                "Shuffle"
                d_t "Wow! These are amazing!"
                d_t "She's really talented. Man I have big shoes to fill."
                d_t "No wonder everyone on the team was so fond of her."
                "Flip"
                #CHange drawing
                d_t "Whoa. This one looks, different..."
                d_t "I-"
                d_t "This wasn't for work."
                d_t "..."
                d_t "I shouldn't be looking at this. These are her personal sketches."
                d_t "But..."
                "Shuffle"
                #CHange drawing
                d_t "Did Simon look at these before telling me to look at them?"
                d_t "No. He wouln't tell me to look at something like this."
                d_t "This doesn't fit the Kai they've been describing at all."
                d_t "And these were recent."
                d_t "Something must have seriously been going wrong right before she left."
                d_t "This one is dated to the last day Simon said she'd come to work..."
                d_t "Poor Kai."
                d_t "I should put this back. I think I've seen enough. Maybe there's some oher designs on the computer."
                

            label deskcomputer:
                d_t "Let's see what she has saved on her computer."
                d_t "Wow, clean desktop. I'm impressed."
                d_t "Alright. Most of this just looks like work in progresses for previous projects."
                d_t "She does have some notes right here though."
                "Click"
                d_t "Hmm some about the Project they're working on. It looks like she was planning out some Ideas."
                d_t "Oh and there's some messages she started to the others!"
                d_t "Maybe she left some notes about her thoughts on the designs."
                d_t "Oh yeah! I found Gold. She's describing what she thought she'd do for one of the designs that are still missing!"
                d_t "Let's- oh! That sounds doable!"
                d_t "For sure."
                d_t "Huh?"
                d_t "What's this about taking time off?"
                d_t "It's adressed to Matt directly!"
                d_t "She's bold."
                d_t "Hold on. But didn't Simon say Kai quitting came out of nowhere?"
                d_t "This text would explain why she wanted to talk to Matt before leaving. But neither of them ever mentioned her wanting time off."
                d_t "Did they lie?"
                d_t "Matt said she quit. There was nothing about a known time off from work."
                d_t "Why would he lie about that if he knew. I would have taken the position anyways."
                d_t "Did she change her mind?"
                d_t "It doesn't look like she ever sent it. Did they talk about something else then?"
                d_t "Why did she go directly to Matt? I'm sure Simon would have asked him for time off for her if she'd told him about it."
                d_t "I'm sure he would have understood."
                d_t "That's usually not something you go directly to the head of department for. I'm sure Matt would have been less than pleased."
                d_t "What was going on?"
                d_t "She seems so desperate."
                d_t "It looks like someone from work was making her uncomfortable."
                d_t "Very uncomfortable..."
                d_t "Why didn't she just go talk to Simon about feeling unsafe? Something as serious as this should be reported imeduately!"
                d_t "No stop it Destiny!"
                d_t "I shouldn't even be looking into this. It's none of my business."
                d_t "I got the notes I was looking for."
                d_t "This is still her Computer. I shouldn't be looking for more than strictly work related stuff."
                d_t "Maybe she quit to get away from it all..."
                

            label deskpostcard:
                d_t "Oh, a postcard. I probably shouldn't snoop in other peoples things."
                d_t "But..."
                d_t "She did leave it here though..."
                d_t "Screw it. Maybe this will tell me a little bit about her. I am curious to know what she was like as a person. Not just her work."
                d_t "Wait. Is this her on the picture!?"
                d_t "..."
                d_t "But isn't that-"
                d_t "It's the girl from my dreams!"
                d_t "But how is that even possible? I can't remember ever seeing her before she started appearing in my sleep."
                d_t "We've never even talked."
                d_t "But she looks exactly like her..." 
                d_t "No, that is her alright. I remember that Face."
                d_t "Why is she suddenly haunting and telling me that someone is after me?"
                if dinner_plans ==True:
                    d_t "I really do have a weird subconcious. It's kind of freaky."
                else:
                    d_t "Were they really just dreams?"
                    d_t "Can they be? I mean, it's clearly her. Even though I've never seen her from so close before."
                    d_t "I couldn't have possibly known what she'd look like until now."
                    d_t "Kai's the one warnign me about all of this."
                    d_t "Is she-"
                    d_t "Does she know about the achievements?"
                d_t "-"
                d_t "Hold on. What does it say on the back?"
                d_t "\"Have a great summer this year! Make sure you bring home lot's of good memories when you visit again. -Love, Mom\""
                d_t "Aw, Sweet."
                d_t "!"
                d_t "Hey! That's my street!"
                d_t "The adress."
                d_t "She lives really close to me!"
                if dinner_plans ==True:
                    d_t "Whoa, it gets even more freaky. Jeez these weird coincidences keep piling up."
                    d_t "Did I maybe see her on my way home?"
                    d_t "That would explain how I know what she looks like..."
                    d_t "Maybe that's it. I mean it's possible I forgot I ever even saw her since I had nothing to do with her."
                    d_t "The mind works in mysterious ways doesn't it."
                else:
                    if call_police == True:
                        d_t "Oh no."
                        d_t "She hasn't come in to the office."
                        d_t "She didn't tell anyone why she was leaving."
                        d_t "She left all her things."
                        d_t "And that girl that went missing lived close to me..."
                        d_t "Kai didn't know she wouldn't be coming back."
                        d_t "She didn't leave."
                        d_t "She was taken!"
                        d_t "Kai is the one the police are looking for!"
                        #Ignorance is bliss glitches to was bliss
                        d_t "!"
                        d_t "So it's true."
                        d_t "But how-"
                        d_t "Why haven't they questioned Matthew and Simon yet? Shouldn't the police ask her employers? They're the ones in charge of this department."
                        d_t "I'm sure the police has talked to them by now. Wouldn't they have to ask the team if anyone knew anything?"
                        d_t "Simon said she suddenly wanted to quit and wouldn't talk about it. It has to have been someone from work."
                        d_t "Even talking to Matthew seemingly didn't change her mind."
                        d_t "Is that \"he\" she keeps mentioning working here?"
                        d_t "..."
                        d_t "Is he after me now...?"
                        d_t "He was at my apartment yesterday."
                        d_t "Oh my god. She's been trying to warn me about this. It's happening to me too now."
                        d_t "It's happening to me too now."
                        d_t "Maybe this is how it all started for her too."
                        d_t "I have to find a way to change whatever it is she sais is going to happen!"
                        d_t "There has to be a way to get out of this."
                        d_t "I can't just lock myself in at home"
                        d_t "That's not going to keep me safe."
                        d_t "Plus I really need this job."
                        d_t "I have to tell the police about this."
                        d_t "I have to figure this out along side work somehow. I can't mess this up."
                    else:
                        d_t "Oh no."
                        d_t "That knocking-"
                        d_t "She's been warning me."
                        d_t "She hasn't come in to the office."
                        d_t "She didn't tell anyone why she was leaving."
                        d_t "She left all her things."
                        d_t "Kai didn't know she wouldn't be coming back."
                        d_t "She didn't leave."
                        d_t "She was taken!"
                        #Ignorance is bliss glitches to was bliss
                        d_t "!"
                        d_t "So it's true."
                        d_t "But how-"
                        d_t "She's been trying to warn me about someone."
                        d_t "Simon said she suddenly wanted to quit and wouldn't talk about it. It has to have been someone from work."
                        d_t "Even talking to Matthew seemingly didn't change her mind"
                        d_t "Is that \"he\" she keeps mentioning working here?"
                        d_t "..."
                        d_t "Is he after me now...?"
                        d_t "He was at my apartment yesterday."
                        d_t "Oh my god. She's been trying to warn me about this and I've ignored all of it." 
                        d_t "It's happening to me too now."
                        d_t "Maybe this is how it all started for her too."
                        d_t "I have to find a way to change whatever it is she sais is going to happen!"
                        d_t "There has to be a way to get out of this."
                        d_t "I can't just lock myself in at home"
                        d_t "That's not going to keep me safe."
                        d_t "Plus I really need this job."
                        d_t "I have to figure this out along side work somehow. I can't mess this up."
                jump kaidesk

                

            label donewithdesk:
                if dinner_plans == true:
                    d_t "I can't get the thought out of my head that she didn't just quit."
                    d_t "I feel kind of uneasy sitting at this girls desk. Something's telling me it's not safe here..."
                    d_t "Was she stalked?"
                    d_t "No one knows where she is. Almost like she just dissappeared."
                    d_t "It's possible someone from work did something to her."
                    d_t "I'm sure whoever it was wouldn't like me taking her place."
                    d_t "I have to be a more careful. That knocking that we heard yesterday. Gabe said no one was there."
                    d_t "But the fact that Kai hasn't shown up and lived really close to me is giving me the shivers."
                    d_t "Maybe this whole thing is connected somehow."
                elif call_police == true:
                    d_t "Someone here wanted to hurt Kai."
                    d_t "It doesn't feel right sitting at this her desk. She dissapeared and now I'm taking her place."
                    d_t "I'm next."
                    d_t "What happened to her?"
                    d_t "The police are still looking for her."
                    d_t "No one knows where she is..."
                    d_t "I don't believe that."
                    d_t "Someone here knows."
                    d_t "Someone did something to her"
                    d_t "I have to be a more careful. That knocking yesterday... I'm glad I called the police."
                    d_t "Maybe all of this will help them find her."
                    d_t "And find whoever did this to her..."
                    d_t "..."
                    d_t "I don't want to end up like Kai."
                    d_t "I have to figure out how to stop this."

                else:
                    d_t "Someone here wanted to hurt Kai."
                    d_t "It doesn't feel right sitting at this her desk. She dissapeared and now I'm taking her place."
                    d_t "I'm next."
                    d_t "What happened to her?"
                    d_t "No one knows where she is..."
                    d_t "I don't believe that."
                    d_t "Someone here knows."
                    d_t "Someone did something to her"
                    d_t "I have to be a more careful. That knocking yesterday..."
                    d_t "It was him. I have to be more alert and figure out who did this to her"
                    d_t "I don't think she just quit."
                    d_t "..."
                    d_t "I don't want to end up like Kai."
                    d_t "I have to figure out how to stop this."
                
                d_t "I don't know if it will help but I should go talk to Simon..."
                d_t "I think he should know about these-"
                d_t "Strange notes."
                d_t "It doesn't look like she ever got the chance to tell him."
                d_t "I'll go meet him over lunch."
                d_t "For now all I can really do is just continue were she left off."
                jump afternoon3

            label afternoon3:
                scene bg_office_hallway
                d "Gabe!"
                d "Where were you at lunch? I didn't see you anywhere."
                g "Sorry I totaly forgot to tell you. I brought something to eat today."
                g "The stuff they were serving at the cafeteria today looked wreched."
                d "Yeah..."
                d "Have you seen Simon anywhere?"
                g "Simon?"
                g "I saw him leave around lunch time. But since then? No."
                d "Oh ok. Thank you."
                d "Well he did say he was going to be busy..."
                g "Did you want to talk to him?"
                d "Yeah. I wanted to ask him about something."
                d "But I'll just have to wait until he's back."
                g "What do you want to ask him?"
                d "I'll tell you later ok? I think I should get back to work."
                g "Oh."
                g "Sure. Don't want to be caught slacking on your first day."
                d "Yeah."
                jump party
                   


           
        label party:
            scene bg_office_cafeteria
            if open_door == True and call_police == False:
                g "Destiny!"
                g "There you are!"
                g "Ive been looking for you. And? How was your first day in the new Team?"
                d "Oh, It was fine. I got to- eh take a look at Kai's designs and style."
                g "Was something wrong with them? You don't look too pleased."
                g "I thought something was off before too. What's wrong?"
                d "No, no the drawings were great. I just found some of her other things too."
                d "And... She didn't seem too happy before she left."
                d "Something seemed off."
                g "Oh"
                g "What did you see?"
                d "There were some notes and drawings..."
                g "Did she not clear her computer before she left?"
                d "No..."
                d "It all seemed quite sudden. All of her things were still there."
                g "What!?"
                g "She didn't take anything with her?"
                d "No."
                g "That does sound weird."
                g "Have you told Simon about it?"
                d "No that's why I was looking for him. I wanted to go talk to him about it but he wasn't there."
                d "He said he'd be there almost the entire day but I guess something must have come up."
                g "Aw man. That sucks."
                g "Were you at least able to start on the designs they want you to do?"
                d "A little bit yeah."
                d "..."
                g "Come on Destiny. Relax, it's going to go great."
                g "A little bump in the road isn't going to mean the end of this Project."
                d "That's not what I'm worried about..."
                g "Oh?"
                g "What's the matter?"
                d "I don't feel safe here."
                d "Those things I saw on her computer and her just dissapearing leaving everything behind."
                d "It just doesn't sit right with me."
                d "I shouldn't just be replacing her."
                d "She said someone from work was pressuring her and now these strange things are starting to happen to me too."
                d "I think I should just go home."
                d "But with the things that happened yesterday..."
                d "I'm scared someone here wants to do the same things to me that they did to her."
                g "Do you think she was-"
                g "Kidnapped?"
                d "Maybe..."
                g "Oh Destiny. Why didn't you tell me about this sooner. If you don't feel comfortable being here, then there's no need to stay."
                g "This isn't an obligatory event. And even work isn't worth being in danger for."
                d "I'm scared to go alone."
                g "Who said you'd be going alone."
                g "I'll keep you company untill you're home."
                g "Do you want to call the police?"
                d "No. Not tonight. Maybe tomorrow morning but right now I just want to go home."
                g "That's ok."
                g "Let's get you Home. And once you're there you'll lock the door and try to get some sleep."
                g "If you want I can come over and we can call the police tomorrow."
                d "Thank you Gabriel."
                g "Don't worry about it. I'd be scared too if I was in your position."
                g "Now let's go."
                jump catmissing



            else: 
                g "Destiny!"
                g "There you are!"
                g "Ive been looking for you. And? How was your first day in the new Team?"
                d "Oh, It was fine. I got to- eh take a look at Kai's designs and style."
                g "Was something wrong with them? You don't look too pleased."
                g "I thought something was off before too. What's wrong?"
                d "No, no the drawings were great. I just found some of her other things too."
                d "And... She didn't seem too happy before she left."
                d "Something seemed off."
                g "Oh"
                g "What did you see?"
                d "There were some notes and drawings..."
                g "Did she not clear her computer before she left?"
                d "No..."
                d "It all seemed quite sudden. All of her things were still there."
                g "What!?"
                g "She didn't take anything with her?"
                d "No."
                g "That does sound weird."
                d "That's not all. She had-"
                "Bump!"
                s "Oh sorry! Didn't see you there."
                g "No worries! You're Simon am I right?"
                s "Yes. How did you know? I don't think we've been interduced yet."
                g "I'm Gabriel! Destiny here told me she'd be working with you from now on."
                s "Ah, Destiny! Lucky seeing you here!"
                s "I didn't take you as much of a party person."
                d "Eh, every once in a while is fine."
                s "I'm glad I ran into you again actually!"
                s "I was hoping we'd get to talk a bit more during the day but the meeting eh- took a little longer than expected..."
                s "I wanted to stop by afterwards. But it was already so late then. I'm terribly sorry."
                d "Don't worry. I was able to settle in fairly well."
                g "Destiny has told me all about your generous offer to let her take up the task of designing for your team."
                g "I heard it had to be quite a hasty desicion"
                s "Oh yeah. It's a shame. The woman that was working for us before quit recently. We're still trying to figure everything out." 
                s "But I'm sure Destiny will be a fine replacement as far as I'm concerned."
                s "Did you find Kai's designs?"
                d "Actually about that. Gabe could you give us a moment? I have something I'd like to ask Simon."
                g "Sure go ahead I'll be waiting over by the snacks if you need me."
                d "Thank you."
                s "Oh? What the matter? You sounds rather serious."
                d "Maybe. I wanted to ask you about the time before Kai left."
                s "Oh?"
                s "Go ahead."
                d "The thing is, I found some of her old notes on her computer. They were kind of... unnerving."
                d "There was also a message she wanted to send to Matthew right before she quit I think."
                s "You found what?"
                d "Yeah. In the message she was requesting time off from work."
                s "..."
                s "That was on her computer?"
                d "Yeah. You seem surprised."
                s "Well yes. That's the first I've heard of it."
                d "Matthew never mentioned anything to you?"
                s "No. I'd remember something like that."
                s "I really should have taken a closer look before..."
                s "I'm sorry."
                d "Do you think Matt knows why she quit?"
                s "I know she went to talk to him the day before. But he never said anything about such a request."
                s "He never told me anything about their conversation at all actually. Said it was private."
                s "I don't get it. She should have come to me first. What went wrong?"
                d "I'm sure she had a reason."
                s "Oh sorry. Did I say that out loud?"
                s "It's just so unusual for her."
                s "If she'd wanted time off I'd have been glad to negotiate the terms with her."
                s "She was one of the most hardworking members on our team. Of course I'd have given her time off."
                s "Are you sure that's what you read?"
                d "Pretty sure yes. But I don't think she ever sent it."
                d "I just thought, since you mentioned she went to talk to Matt, he knew about her request."
                s "Hmm. Possible."
                s "Did she write why she wanted time off?"
                d "There was something about someone making her uncomfortable."
                s "Oh."
                s "Did she say who?"
                d "No. It was really vague. I don't think she wanted Matthew to know who it was."
                s "I'll go talk to him about it."
                s "If he knows something about why she quit so suddenly or where she went then I should know about it as well."
                s "I'm a bit shocked he didn't tell me."
                d "Yeah, I don't know why he wouldn't."
                s "Thank you for letting me know!"
                s "I'll have to confront him about it. I think he's here too tonight."
                d "Of course."
                d "I was able to start picking up her work as well by the way."
                s "Really! Thats awesome. We'll take a look at it tomorrow moring ok?"
                d "Sure."
                if call_police == True:
                    "Ring!"
                    d "Oh! Sorry! That has to be mine."
                    s "Take it. I'll go talk to Matthew while you're busy."
                    d "Thanks!"
                    "Click"
                    d "Destiny Sullivan. Who is this?"
                    o "Evening miss Sullivan. This is officer Rogan. Do you have a moment to talk?"
                    d "One second please."
                    scene bg_office_hallway
                    d "So, you were saying?"
                    o "Yes. Sorry for disturbing you madam."
                    o "But we felt it was necessary to inform that a suspicous individual has been spotted wandering around your apartment today."
                    o "One of our officers caught sight of a hooded figure entering the building and inspecting the mailboxes, seemingly looking for something."
                    o "They quickly left however as soon as the officer went to approach them."
                    o "We believe it was a younger man but would confirm your suspisions miss Sullivan."
                    d "Were they able to see who it was?"
                    o "No. The person was wearing a facemask and had a hood on."
                    o "We will investegate this person further however."
                    o "Going off accounts from neighbours we suspect this might the same individual responsible for the recent dissapearance."
                    o "Since we now have reason to believe these two cases are connected we would like to collect any information you have about a woman called Kai Amari."
                    d_t "It is her!"
                    o "Does the name sound familiar to you?"
                    d "Yes! We work at the same company. Well, she quit unexpectedly a few days ago."
                    o "Did you know her?"
                    d "No not really. I don't think I've heard of her before two days ago. I was offered to take her position since they needed someone to fill her place."
                    o "And since then you've been noticing feeling followed?"
                    d "Yes. It started when I was offered to switch to her team."
                    d_t "The dreams started the day I heard the news from Matt."
                    d_t "How can I tell him I think she's been captured without telling him about my crazy dreams."
                    o "You two never had any relations before that?"
                    d "No."
                    o "Did anyone you know ever talk about miss Amaris dissapearence?"
                    d "Well, my boss and my new team leader both told me she quit suddenly and then never came in again."
                    d "I was assigned her desk to look through her started work. When I looked through her notes I found some disturbing images."
                    o "Please, continue."
                    d "She drew about s man stalking and pressuring her. She wrote about being uncomfortable around certain people in the office."
                    d "There was a message to one of the executives requesting time off because of it."
                    o "Such a request was never mentioned to you when you were offered her position?"
                    d "No."
                    o "Did you ask any higherups about it?"
                    d "I did, yes. He said that the person the message was for never mentioned anything about her request to him."
                    d "That was just now actually. He said he is going to ask him about it."
                    o "Thank you miss Sullivan. We would like to look into these drawings and individuals further. Could we have the names of you boss and team leader?"
                    d "Matthew Ledger and Simon Harris."
                    o "We will come collect the information early tomorrow and keep you informed about any happenings."
                    o "There is a police officer stationed at your building but we would still advise you to have someone you trust accompany you home tonight."
                    d "I will."
                    o "If you notice anything strange alert us imediately."
                    d "Yes. Thank you officer."
                    o "We will likely have to call you again. But untill then, goodbye miss Sullivan."
                    d "Goodbye officer Rogan."
                    "Click"
                    d_t "He was there again!"
                    d_t "He was at my apartment again!"
                    d_t "The knocking was real."
                    d_t "Kai was right. He's after me now."
                    d_t "God, I should have been listening to her"
                    d_t "Did she leave any other hints?"
                    d_t "She's been trying to talk to me. These achievements. They're her trying to talk to me."
                    d_t "Urgh! Why can't I figure these out. Every time it's something completely different than I expected."
                    d_t "What can I do?"
                    d_t "The police will get her stuff tomorrow..."
                    d_t "Will the message to Matt and the drawings really be able to help them?"
                    d_t "I hope so. I can't really do anything else right now."
                    d_t "What's left for today?"
                    #look at achievements
                    d_t "I think this call must've been the hands up."
                    d_t "So that means..."
                    d_t "Only the where is Waldo one is left."
                    d_t "Great of course. The one I was able to decipher the least."
                    d_t "I haven't had to look for anyone yet."
                    d_t "Kai's notes do make it seem the guy she kept warning me about in my dreams works here."
                    d_t "And if this Waldo is supposed to be him then I can technically find him tonight right?"
                    d_t "If that's true then I'd be able to narrow it down a bit by looking at who's here tonight."
                    d_t "Well."
                    d_t "That doesn't really make my sample size that much smaller now that I think about it."
                    d_t "Oh well it's worth keeping in mind."
                    d_t "I should go back in."
                    jump mattconvop
                else: 
                    s 2If you'll excuse me I think I just saw him over there.'
                    d "Good luck!"
                    d_t "I need a moment away from these people."
                    scene bg_office_hallway
                    d_t "Much better."
                    d_t "Jeez I hate crowds."
                    d_t "Oh! Now that I have a moment to myself."
                    d_t "What's left for today?"
                    #look at achievements
                    d_t "Well the ignorance was definitely bliss."
                    d_t "Ouch. But after that?"
                    d_t "Nothing police related has happened yet. Is this really just the party then?"
                    d_t "Hmm it could also still happen later."
                    d_t "I doubt it though. Especially because of that last one."
                    d_t "\"Where is Waldo\""
                    d_t "That one pretty much requires a crowd." 
                    d_t "Great. The only one left is the one I was able to decipher the least."
                    d_t "So far no one has stuck out to me. But maybe that's exactly the point."
                    d_t "Kai's notes do make it seem the guy she kept warning me about in my dreams works here."
                    d_t "And if this Waldo is supposed to be him then I can technically find him tonight right?"
                    d_t "If that's true then I'd be able to narrow it down a bit by looking at who's here tonight."
                    d_t "Well."
                    d_t "That doesn't really make my sample size that much smaller now that I think about it."
                    d_t "Oh well it's worth keeping in mind."
                    d_t "I should go back in."
                    jump mattconvo

            label mattconvo:
                scene bg_office_cafeteria
                m "Well if it isn't miss Sullivan."
                d "Oh. E- Evening Matthew."
                m "{i}Evening.{/i} I heard you settled in fine in your new position."
                d "Uhm. Yeah I have. Simon gave me Kais old desk."
                m "That much is apparent."
                d "Did. Ehm, Simon come to talk to you about her?"
                m "Just now? Yes."
                m "Not that that's any of your business. Thank you for that."
                d "But her message to you-"
                m "A Message! Now you're just insulting me. Do you really think I wouldn't inform my staff about such imprtant manners?"
                d "What?"
                m "I don't know what you are talking about but the situation with Kai is something between Simon and me."
                m "I don't know what motivated him to interogate me again about the conversation we had just before she quit. Because that's behind us now. I thought it was done the first time it came up."
                m "But since you're just there to fill her place I don't know why you should be concerned with any of it."
                d "Sorry. I just-"
                m "You what? Thought you should be even more intrusive than reading the personal notes of a coworker you don't even know?"
                m "Has it ever occured to you that some things are not meant to be read by others?"
                m "It seems you two really similar. Only difference was that Kai knew when to be professional." 
                m "Trying to make a good first impression are we? That does not excuse you making up stories and throwing dirt on my name."
                m "I don't know why Simon didn't correct you on your unacceptable behavior."
                m "I can somewhat understand his frustration about her coming to talk to me instead of him. But I thought we settled that. You should leave your nose out of it."
                d "I-"
                m "If you were still under my supervision snooping in others personal data would not slide."
                d "I wasn't trying to. I- I was just looking for more information about the current project."
                d "I didn't think this would turn into such a big thing."
                m "Of course you didn't."
                m "That seems to be a reoccuring theme with you."
                m "And don't think I've forgotten about our little misshap."
                m "If I hear about one more action against my name. You'd better be sure the consequences will be grave."
                m "If you would excuse me. I would like to preserve my nerves tonight and grab a bite to eat."
                m "{i}For which I will definitely not need your help.{/i}"
                menu:
                    "Leave and join Gabe":
                        g "Jeez what was that? First Simon now you?"
                        g "Matt's on a killing spree tonight."
                        d "Yeah..."
                        d "Something's strange about this whole situation."
                        g "Really? What's up?"
                        d "You remember how I was telling you before that Kai didn't seem too happy before she left?"
                        g "Yeah what about it?"
                        d "Well she wrote a message to Matt about someone making her uncomfortable. But it seems she never sent it."
                        g "She wrote one directly to Matt?"
                        g "That's some nerves!"
                        d "Yeah. But the weird thing is Matt is denying ever having known about any of that even though she went to talk to him right before she quit."
                        g "Wait they talked?"
                        d "Yep."
                        g "She must have changed her mind then."
                        d "Maybe..."
                        g "Simon seemed stressed too though. What was his problem with Matt?"
                        d "Really?"
                        g "Yeah. After they talked he stormed off into the hallway."
                        d "Well, he also went to Matt to ask about that message. But I think in the end he was more interested in what they actually talked about that day."
                        g "Why would he get so worked up about that?"
                        d "I don't know. I guess he thought she should have told him first. But it didn't look like it bothered him that much when I told him about it."
                        d "Maybe he told him something but I'm nost sure. Must be something between him and Matt I guess."
                        g "It's probably some form of rivalery."
                        g "Who knows, maybe he secretly wants Matts position and doesn't like people choosing Matt over him."
                        d "Oh shut up, he's not like that at all."
                        d "Besides. If anyone chose to talk to Matt over me I'd be pretty offended too."
                        g "Wanna go grab something to eat? I saw some tasty treats over at the snack bar."
                        d "Maybe in a minute. Matt's there right now and I don't want to risk running into him again."
                        if call_police==True:
                            jump simonconvop
                        else:
                            jump simonconvo
                        

                    "Press on":
                        d "Did you even get a message form Kai?"
                        m "Excuse me?"
                        d "Did Kai ever ask for time off?"
                        m "Neither did I get a message from Kai nor do I know of her ever asking for time off."
                        m "She came to me on the day that she quit saying that she didn't want to work here anymore. And that I should wait to tell Simon until the next day."
                        m "Whatever sentimental messages she wrote on her computer, I never saw any. All I did was do my job."
                        m "I don't know why you are both now accusing me of having witheld important information. But like I already told Simon she had no oblegation to inform him in the first olace. And neither did I."
                        d "Oh."
                        m "I'll be going now thank you."
                        d "..."
                        #goes over to gabe
                        g "Jeez what was that? First Simon now you?"
                        g "Matt's on a killing spree tonight."
                        d "Yeah..."
                        d "Something's strange about this whole situation."
                        g "Really? What's up?"
                        d "You remember how I was telling you before that Kai didn't seem too happy before she left?"
                        g "Yeah what about it?"
                        d "Well she wrote a message to Matt about someone making her uncomfortable. But it seems she never sent it"
                        g "She wrote one directly to Matt?"
                        g "That's some nerves!"
                        d "Yeah. But the weird thing is Matt is saying she never mentioned any of that."
                        g "Wait they talked?"
                        d "Yep. She went to go talk to him before she quit but it seems like he doesn't want anyone to know what they actually talked about."
                        g "That is weird."
                        d "He sais we're accusing him of something, but he's the one making such a big deal out of us asking him."
                        d "All I wanted to know was if she'd sent the message."
                        g "Well, I wouldn't put it past Matt to take you two both asking him about something he doesn't know as a personal offence. But I admit, this is a little extreme even for him."
                        d "Yeah..."
                        g "Hey! You know what will cheer you up?"
                        g "Let's go grab something to eat? I saw some tasty treats over at the snack bar."
                        d "Maybe in a minute. Matt's there right now and I don't want to risk running into him again."
                        if call_police==True:
                            jump simonconvop
                        else:
                            jump simonconvo
                        

            label simonconvo:
                s "Ah, Destiny! I'm glad I caught you again tonight."
                s "Is something the matter? You look tense."
                d "Don't worry it's nothing. I'm just a little exhausted that's all."
                s "Had a long day huh?"
                d "Yeah. I can't wait to just get home and relax."
                s "You live on Parkerstreet right?"
                d "Oh! Yeah we talked about it briefly at the beginning of the week, right. I'm surprised you remembered that."
                s "It's a lovely area. I think I looked at some apartments there too once. That's why I was so interested."
                s "Isn't that the one with the really bad bus connection?"
                d "Well, it's not that bad. I just have to walk to the next busstop from the office since my bus doesn't go all the way here."
                d "Actually! That reminds me. I wasn't planning on staying too long today. Let me check what time it is-"
                d "Oh no! My phone!"
                s "What's up?"
                d "I must have left my phone somewhere!"
                s "Want me to help you look for it?"
                d "No it's fine. I don't want to take up even more of your time. I'll go look for it myself."
                s "As you wish. See you tomorrow then."
                d "See ya!"
                jump findphone
                
                
            label simonconvop:
                s "Ah, Destiny! I'm glad I caught you again tonight."
                s "Is something the matter? You look tense."
                d "Don't worry it's nothing. I'm just a little exhausted that's all."
                s "Who was that on the phone there before?"
                d "Oh that? Uhm, no one special. Just ehm-"
                menu:
                    "The landlord":
                        d "It was my landlord. Er- He wanted to know if I'd experienced any doordashers recently..."
                        s "Your landlord?"
                    "A neighbour":
                        d "It was my neighbour. Er- He wanted to know if I'd experienced any doordashers recently..."
                        s "Your neighbour?"

                d "Yeah. I think there were some kids uhm, going around the past few days."
                s "Really?"
                d "Or so I've heard."
                s "Doordashers? That's rare these days. These aparment buildings are so I guess anyone can stroll in."
                s "You live on Parkerstreet right?"
                d "Oh! Yeah we talked about it briefly at the beginning of the week, right. I'm surprised you remembered that."
                s "I've looked into getting an apartment there too once actually. That's why I was so interested when you mentioned it."
                s "You live in that big block right in front of the park right?"
                d "Yeah exactly."
                s "I think I checked that one out too. Great views. But the bus connection is quite bad isn't it."
                d "Well, it's not that bad. I just have to walk to the next busstop from the office since my bus doesn't go all the way here."
                d "Actually! That reminds me. I wasn't planning on staying too long today. Let me check what time it is-"
                d "Oh no! My phone!"
                s "What's up?"
                d "I must have left my phone somewhere!"
                s "Want me to help you look for it?"
                d "No it's fine. I don't want to take up even more of your time. I'll go look for it myself."
                s "As you wish. See you tomorrow then."
                d "See ya!"
                jump findphone

            label findphone:
                g "Hey!"
                g "Are you looking for something? You've been running around the room like a madwoman."
                d "I can't find my phone!"
                d "I think our last bus leaves soon but I can't leave without my phone."
                g "I'll help you look for it. Together we'll be quicker."
                g "I'll go check in the hallway."
                d "Thank you Gabe"
                #couple minutes later
                g "Found it!"
                d "Really!?"
                d "Oh thank god."
                d "Where did you find it? I thought I looked everywhere."
                g "It was on the desk of one of those offices right beside the entrance."
                d "I must have left it there when I went out..."
                g "You'd lose your head if it wasn't attached."
                g "Did you check the time by the way? I think we've got to get going soon."
                d "Oh, you're right!"
                d "Let's go."
                jump night

        label night:
        label catmissing:
            scene bg_d_corridor
            g "There we are. Feeling better?"
            d "Yeah. Thank you for bringing me home."
            g "Oh don't worry it's nothing. I want you to be safe."
            g "Lord knows there's enough creeps out there."
            g "You should go in now though. And make sure you lock your door."
            g "Double check it"
            d "Yeah yeah. I will."
            d "Triple check it even."
            d "Get home safe too Gabe. Or I'll feel even worse for making you do all this."
            g "Don't worry about me. I'll be home in no time."
            g "Night Destiny."
            d "Goodnight Gabe."
            "Lock"
            d_t "Finally."
            d_t "No one's getting in now."
            "Rustle"
            d_t "Oh right, [catname]! Shoot I forgot to get them catfood."
            d "[catname]! I'm home."
            "..."
            d "Sorry I'm so late. I've got some bad news for you little buddy..."
            d "[catname]?"
            d "You were so lively yesterday. Are you mad at me for leaving you all alone for so long?"
            scene bg_d_kitchen
            d "[catname]?!"
            d "Where-"
            d "AHHH!"
            scene bg_black
            "Thud"
            d "MHHHM"
            s_k "Stop squealing you little brat."
            d "MRRH"
            s_k "URGH, Stop that!"
            s_k "I thought I told you to {i}shut up.{/i}"
            "Whack!"
            jump worst



    label day4:
        label dream4:
            scene dream4
            k "Destiny!"
            k "I don't have much time."
            d "Kai! I can remember you! What happened to you?"
            k "We don't have much time Destiny. He's tracking you."
            d "What?"
            d "Who's tracking me? How do you know?"
            k "It's your phone. He's tracking your phone. You can't have it with you tomorrow."
            d "How do you know that?"
            k "You have to trust me on this Destiny."
            k "He's going to come here again tomorrow."
            k "He's keeping me locked away. I don't know where but you can!"
            d "How? What do you mean."
            k "He only comes here every couple of days. He has to to make sure I'm still here."
            k "Tomorrow night. He's planning to follow you on your way home and bring you here too."
            d "He's going to kidnap me!?"
            k "Beat him with his own tactics Destiny!"
            d "His tactics? What do you mean? Are you crazy?!"
            k "You can't let him know where you are. Trust me. Play along. He won't expect you to do what he would."
            d "That's insane!"
            k "Please. I don't want it to end here. This is the only way I know how to get out of this place."
            k "You're the only person that can find me."
            k "If he knows he can't track you he won't risk it."
            d "Who-"
            k "If he knows it won't work he'll come here alone. You can find out where he goes. I can helq .Y 0_- "
            d "Who!?"
            k "YOu'l/ k N. w -*"
            d "KAI!"
            k "_.*- ,"
            d "No! Stay!"
            d "Wait!"


        label morning4:
            scene bg_black
            "Ping!"
            scene bg_d_window
            d "Kai!"
            d "Tell me"
            d "Who-"
            d "..."
            d "He's tracking me!"
            if dinner_plans==False:
                c_n "Hsss!"
                d "Sorry [catname]."
            d "!"
            d_t "\"You remember me don't you\". I do!"
            d_t "Kai, I remember you! I have to find her!"
            d_t "But..."
            d_t "How am I going to do that?"
            d_t "She said he's tracking me. My phone."
            d_t "How would he-"
            d_t "I forgot it in the hallway yesterday!"
            d_t "Oh no."
            d_t "Gabe said it was still laying near one of the cubicals."
            if call_police == True:
                d_t "I must have forgotten it there when I went out to talk to officer Rogan"

            else: 
                d_t "I must have forgotten it there when I went out to take a break from all the people."

            d_t "He probably bugged it while we were looking for it."
            d_t "Wait, how would they even know I'd lose it?"
            d_t "That's pure chance."
            d_t "And how would Kai even know that?"
            d_t "What she's asking me is insane! I can't just present myself to this creep and go about my day as if nothing happened."
            d_t "Beat him with his own tactics?"
            d_t "Do what he would?"
            d_t "He's just stalking me apparently."
            d_t "I can't just follow him. That's crazy."
            d_t "..."
            d_t "How do I know she's not the one leading him to me!"
            d_t "Kai's plan is way too dangerous."
            d_t "How can she be so certain it's going to work?"
            d_t "Is she the one behind all of this?"
            d_t "Or could he be using her to get to me?"
            menu:
                "Trust Kai's plan":
                    $ trust_kai = True
                    d_t "This is the only way I can help her..."
                    d_t "He's the only one that knows where she is."
                    d_t "But following someone to god knows where would be way too dangerous."
                    d_t "That can't be what she meant."
                    d_t "How could I use his tactics against him?"
                    d_t "..."
                    d "Of course! That's it!"
                    d "I can find out where he goes by using a tracker! Just like he did."
                    d "-"
                    d_t "I don't even know who to track!"
                    d_t "I'll know. Yeah right. I still have no idea who took her, other than that it's a guy"
                    d_t "And he has to have known Kai."
                    d_t "That's still too many..."
                    d_t "Matt seemed unusually pissed off yesterday when I mentioned the message I found."
                    d_t "He's always harsh but this was more than his usual selfimportant attitude."
                    d_t "He almost looked, well, nervous."
                    d_t "Or maybe not nervous but definitely not happy that it came out that he kept this information from Simon."
                    d_t "I can imagine Simon is also quite pissed."
                    d_t "He should have been the first to know right?"
                    d_t "Then why did Kai not tell him about any of what was happening."
                    d_t "Why did she go straight to Matt?"
                    d_t "She kept her message really vague. It's clear she didn't want Matt to know who it was. Maybe it was someone close to Simon."
                    d_t "Or maybe her and that creep used to be close."
                    d_t "I'm sure Simon would have been able to figure out who she was talking about if she'd talked to him."
                    d_t "I didn't get the chance to look at all of her notes yesterday."
                    d_t "Stupid! I should have just gone through all of them."
                    d_t "I'll have to look through all her things again today. I have to find something that will tell me who it is!"
                    if dinner_plans==False:
                        c_n "Meow!"
                        d "Morning [catname]"
                        d "Sorry for screaming before."
                        c_n "Prrrr"
                        d "See I'm just a little lost on what to do right now."
                        d "I have to find a way to track someone but I don't even know who or how."
                        c_n "Maaauw"
                        d "I know. I know. You don't know what to do either."
                        d "You must be hungry."
                        c_n "Mrrw" 
                        d "I presume that was a yes."
                        d "I have some more tuna but only one more can."
                        d "I'll bring home some propper cat food today."
                        d "{i}If I make it through today...{/i}"
                        d "I think I also have to pick up some other cat supplies anyways. I don't think you're going away anytime soon."
                        d "There's a petshop on my way to work. I bet they have-"
                        d "Chips!"
                        d "I can use the chip from one of those cat-tracking collars!"
                        d "That's it!"
                        d "Thank you [catname]! You're a genius!"
                        c_n "Pwrrrw"
                        d_t "I don't have that much time left but maybe I can look at some of the achievements before I go."
                        jump achievements4
                    else:
                        d_t "And I have to find a way to track them too."
                        d_t "How am I going to do that?"
                        d_t "I don't just have a live tracking device laying around my apartment."
                        d_t "Where do you even get one of those?"
                        d_t "I doubt you can buy one in a normal supermarket."
                        d_t "What's something that the average person would need to be able to track?"
                        d_t "Hmm..."
                        d "Pets!"
                        d "I can use the chip from one of those cat-tracking collars!"
                        d "That's it!"
                        d "That's genius!"
                        d "There's a petshop on my way to work. I can just hop in there and get one."
                        d "Phew at least that's sorted out now."
                        d_t "I don't have that much time left but maybe I can look at some of the achievements before I go."
                        jump achievements4

                "Doubt Kai's words":
                    d_t "I can't trust her. I can't trust anyone."
                    d_t "I don't know if what she's saying is even true."
                    d_t "If I leave my phone at home I won't be able to call the police if something happens."
                    d_t "I'll be completely defenceless."
                    d_t "I can't risk it."
                    d_t "If I fail I'll end up just like her. And for what?"
                    d_t "I didn't even know her before all of this started."
                    d_t "I'm not responsible for what happened to her. I have nothing to do with all of this. I have to keep myself safe first."
                    d_t "I don't even know who this {i}he{/i} is. She never told me who was doing this to her."
                    d_t "So how could I use his tactics against him?"
                    d_t "I can't do that. I have to go to work today but I'm sure as heck not leaving my phone here."
                    d_t "Nothing seems wrong with it anyways. I'm not like Kai. If anything seriously bad happens I'll tell Simon or call the police."
                    d_t "I'll be surounded by so many people all day. There's no chance anyone could take me without someone noticing."
                    d_t "I'll be careful."
                    #achievements glitch
                    d "No I'm not looking at you anymore stupid screen!"
                    d "You're only going to make me more scared. I have to just get through today. Then Everything will be fine"
                    d_t "It has to be."
                    jump work4doubt

            label achievements4:
                menu:
                    "You remember me don't you?":
                        d_t "Yeah I do this time..."
                        d_t "I remember you."
                        d_t "I'll get you out of this Kai."
                        jump achievements4

                    "Taste your own medicine":
                        d_t "I'll do it Kai."
                        d_t "I'll make him taste his own medicine."
                        d_t "This has to work."
                        jump achievements4

                    "Too close for comfort":
                        d_t "I'll meet him?"
                        d_t "I guess I'll have to get very close to him to plant the tracker."
                        d_t "I have to be careful"
                        d_t "I can't get caught. If he knows I'm trying to find Kai's location I'll be in big trouble."
                        jump achievements4

                    "Not alone anymore":
                        d_t "What?"
                        d_t "Who's not alone anymore?"
                        d_t "Does she mean me or herself?"
                        d_t "Should I tell someone?"
                        d_t "Maybe I can get someone to help me."
                        if call_police==True:
                            d_t "If I tell the police my plan now they're going to try to dissuade me."
                            d_t "But if I already know where she is they might be able to help rescue her."
                        else:
                            d_t "Who can I even trust anymore..."
                        jump achievements4

                    "The lions den":
                        d_t "The lions den. I'll find it."
                        d_t "It has to be where Kai's being kept."
                        d_t "I really hope I find the right person."
                        jump achievements4

                    "Start the day":
                        jump work4track
        label work4track: 
            scene bg_office_hallway
            s "Good morning Destiny!"
            s "Here early again I see."
            d "Morning Simon."
            d "Yeah, I wanted to- ehm have enought time to look over what I did yesterday before we talk about it."
            s "Oh, sure"
            s "Take your time. Just come over to my office once you're ready."
            d "Yes. See you then."
            s "See you later Destiny."
            scene bg_office_computer_kai
            d_t "I have to find more clues."
            d_t "I'm sure she left more than what I found yesterday."
            if call_police== Tue:
                d_t "I have to find them before the police get here."
                d_t "I'm sure they're going to confiscate all of it."
                d_t "Oh god. I really should have told Simon I called them."
                d_t "This will cause such a scene."
                d_t "I hope they can at least find something."
            else:
                pass
            "Click"
            d_t "-"
            d_t "What?! But how can this be?"
            d_t "It was all right here yesterday!"
            d_t "No!"
            d_t "Where is it?"
            d_t "This can't-"
            d_t "It's all gone!"
            d_t "No no no!"
            d_t "How could they just have dissapeared!?"
            d_t "..."
            d_t "It was him."
            d_t "Oh god, it was him."
            d_t "He deleted everything."
            d_t "He-"
            d_t "The only people that even know about the notes are Matt and Simon"
            d_t "And I told Gabe about them..."
            d_t "Nobody else knew about these notes-"
            d_t "Nobody else could have even known these even existed."
            d_t "If he would have known about them he would have deleted them right away!"
            d_t "It has to be one of them!"
            d_t "But who-"
            d_t "I can't believe any of them would do such a thing."
            d_t "Matt, Simon, Gabe..."
            d_t "One of them is doing all of this."
            d_t "One of them is keeping Kai hostage."
            menu:
                "It's Matthew":
                    $ track_who = 0
                    d_t "It has to be Matthew."
                    d_t "He won't tell us what happened in that conversation before Kai quit. And sais he never even got a message."
                    d_t "She must have realized it would be too risky."
                    d_t "And he's saying we're accusing him when all we did was ask."
                    if call_police== True:
                        d_t "He didn't talk to the Team even once about Kai's dissapearence even though I'm sure the police would have contacted him."
                    else:
                        pass
                    d_t "He knows where I live..."
                    d_t "He can look at all of our information. He would have known where Kai lived. He has all the power to be pulling the strings."
                    d_t "That's why she didn't want to specify who was making her uncomfortable..."
                    d_t "She couldn't have told him."
                    d_t "It was him."
                    d_t "And he was also the one that was trying to change Simons mind about asking me to be on his team."
                    d_t "I bet he didn't want anyone to snoop around in Kais stuff."
                    d_t "He has the key he could have deleted it whenever he wanted."
                    d_t "Maybe the reason Simon got so mad was because he suspected something. Him and Kai were really close."
                    d_t "She probably didn't want to tell him because it would have meant trouble for him too."
                    d_t "She was trying to protect Simon from having to face Matt."
                    d_t "Why didn't she just call the police on him?"
                    d_t "I guess they would have believed Matt more than her."
                    d_t "Trying to frame your super rich boss for something there's no evidence of?."
                    d_t "I bet that wouldn't have gone over too well."
                    d_t "He got away with it the first time but I'm going to find where he's keeping Kai and then he's goint to pay."
                    d_t "I can't let him know I figured him out though. I have to do what Kai said. Play dumb and make sure he knows he can't track me."
                    d_t "For now I'll keep working. But if I pretend to give an apology for yesterday maybe I can get close enough to slip the tracker into his coat or pockets."
                    d_t "It's going to be risky."
                    if call_police==True:
                        d_t "And I have to do it before the police get here."
                        jump trackmatt
                    else:
                        jump trackmatt
                
                "It's Simon":
                    $ track_who = 1
                    d_t "It's Simon isn't it?"
                    d_t "That's why Kai went directly to Matt."
                    d_t "She couldn't ask Simon for time off because he was the reason she wanted it."
                    d_t "That's why he was so shocked when I told him about it. He thought she didn't know it was him."
                    d_t "Simon's been acting like nothing was wrong with her because he was the one making her miserable. He had to make sure I wouldn't know."
                    d_t "She kept saying in my dreams that he's trying to get close to me. Simon put me at her desk right next to his office. And he's been nothing but friendly and overly helpful."
                    d_t "That conversation we had yesterday... I knew something rubbed me the wrong way."
                    d_t "As soon as I mentioned the reason for her message something changed about him. The bubbly exterior cracked. It was almost like he was nervous or scared..."
                    d_t "He imediately wanted to go talk to Matt too."
                    d_t "I bet he was scared she really did say something about him afterall."
                    d_t "And then storming off to the offices. It all makes sense now. My phone was still out in the hallway when he went there!"
                    d_t "He was the first one here again today too. He had all the time in the world to delete everything."
                    d_t "I should have known!"
                    d_t "All of those questions he asked me about where I live..."
                    d_t "God, I was so stupid and naive. He was just trying to figure out how to get to me. It was him at my door."
                    if call_police== True:
                        d_t "And it was him that the police saw. Stuck in a meeting all afternoon. Yeah right. He left before lunch and wasn't back for ages."
                        d_t "The police had him busy."
                        d_t "He knows the police are up to something."
                        d_t "That's why he had to delet everything before they get here."
                    else:
                        pass
                    d_t "I gave him everything he needed..."
                    d_t "He knows where I live, what route I take, when my busses drive."
                    d_t "He even knows that I saw Kai's notes."
                    d_t "I trusted him!"
                    d_t "I should have listened to Kai. I should have stayed away from him!"
                    d_t "I'm not letting this happen a second time!"
                    d_t "I'm going to find Kai and he's going to pay fro what he's done"
                    d_t "I can't let him know I figured him out though. I have to do what Kai said. Play dumb and make sure he knows he can't track me."
                    d_t "For now I'll keep working. But if I pretend I have a question about work maybe I can get close enough to slip the tracker into his coat or pockets."
                    d_t "It's going to be risky."
                    if call_police==True:
                        d_t "And I have to do it before the police get here."
                        jump tracksimon
                    else:
                        jump tracksimon

                "It's Gabriel":
                    $ track_who = 2
                    d_t "It's Gabriel-"
                    d_t "He was the one that brought me my phone yesterday!"
                    d_t "And he's been with me almost every day."
                    d_t "He's been the closest anyone has been these past days. Kai was trying to warn me."
                    if dinnerplans== True:
                        d_t "Oh God. When Kai said that he was at my apartment she didn't mean the knocking..."
                        d_t "The knocking was never anything dangerous!"
                        d_t "Gabe was!"
                    else:
                        pass
                    d_t "He knows almost everything about my life."
                    d_t "He knows where I live, what route I take, when our busses drive."
                    d_t "He knows the apartments like the back of his hand."
                    if call_police== True:
                        d_t "He wasn't at lunch either yesterday..."
                        d_t "He said he brought something but for all I know he could have been at my apartment looking for something."
                        d_t "Looking for an easy way in maybe."
                    d_t "Home isn't safe anymore."
                    d_t "And Kai lived so close to us too..."
                    d_t "It would have been so easy for him."
                    d_t "I trusted him!"
                    d_t "I should have listened to Kai. I should have stayed away from him!"
                    d_t "I'm not letting this happen a second time!"
                    d_t "I'm going to find Kai and he's going to pay fro what he's done"
                    d_t "I can't let him know I figured him out though. I have to do what Kai said. Play dumb and make sure he knows he can't track me."
                    d_t "For now I'll keep working. But if I act as if I want to talk maybe I can get close enough to slip the tracker into his coat or pockets."
                    d_t "It's going to be risky."
                    if call_police==True:
                        d_t "And I have to do it before the police get here."
                        jump trackgabe
                    else:
                        jump trackgabe
            

        label trackmatt:
            #later that morning
            scene bg_office_hallway
            "Knock"
            d "Matthew?"
            m "What are {i}you{/i} doing here?"
            d "I- I wanted to apologize for yesterday. And also what happened before..."
            m "Yeah right."
            d "No. Seriously. I shouldn't have looked through Kai's things. But I also shouldn't have jumped to conclusions so quickly yesterday."
            d "I'm sure you had your reasons for acting the way you did and I should have respected that. I'm very sorry."
            m "Mhm..."
            m "Look, I don't know what you're trying to achieve here. But if you think you can just make everything undone with some halfhearted apology then you're mistaken."
            m "We're going to have to talk about this with Simon now {i}thanks to you{/i}. But I clearly have other more important things to do right now."
            d "If you want I can put a date in my calendar right now!"
            d "Hold on let me just-"
            d "Oh no."
            d "I forgot. I left my phone at home today!"
            m "..."
            d "I'll just have to write it down then."
            m "Sure."
            m "Tuseday next week."
            m "At 10:30. Got that?"
            d "Oh. But I don't have a pen. Wait I'll just-"
            "Rustle"
            m "What are you-!"
            d "There! You don't mind if I quickly borrow this pen from your bag right?"
            m "You-"
            m "Hmpf! Fine!"
            m "Tuseday at 10:30. Make sure to let Simon know."
            m "And stop rummaging through other peoples belongings! {i}Give that back.{/i}"
            "Yank!"
            d "Oops. Sorry!"
            d "I'll go tell Simon right away."
            m "Thank god."
            scene bg_office_computer_kai
            d_t "That was nerve wrecking!"
            d_t "I hope he didn't see I slipped the chip in there when I took the pen out..."
            d_t "Now I'll just have to wait and pray everything works as planned"
            d_t "Thinking about how he's acting so innocent after the things he did is making me sick."
            jump work4

        label tracksimon:
            #later that morning
            scene bg_office_hallway
            "Knock"
            d "Simon?"
            s "Oh! Destiny. What's up. Can I help you with anything?"
            d "Yeah. I actually wanted to ask you what your thoughts would be on an idea I had."
            d "Can I sit there?"
            s "Sure let me just get my jacket-"
            d "Oh don't worry I'll do it."
            "Rustle"
            d "There."
            d "So! What I wanted to know is how you think it would look if I combined the designs Kai already made and added onto some of them to create sort of a gradient between our styles?"
            s "That sounds like a fantastic idea!"
            d "Wait I can just show-"
            d "Oh shoot I forgot."
            s "?"
            d "I left my phone at home today!"
            s "You did?"
            d "Ah, I can quickly go get the designs if you want."
            s "..."
            s "Sure."
            #goes to get the designs
            d "Alright. I started on this one already."
            s "Looks great."
            s "Are you going to keep working on these today?"
            d "That was the plan. I can keep you updated if I make any significant changes."
            s "Sure, I'm here all day again."
            d "Great! Then I'll probably see you again later."
            s "Of course whenever you need anything."
            scene bg_office_computer_kai
            d_t "That was nerve wrecking!"
            d_t "I hope he didn't see I slipped the chip in there when I hung up his jacket..."
            d_t "Now I'll just have to wait and pray everything works as planned."
            d_t "Thinking about how he's acting so innocent after the things he did is making me sick."
            jump work4
            
        label trackgabe:
            scene bg_office_hallway
            d "Gabe?"
            g "Over here!"
            g "What's up? Need help with something?"
            d "Kind of haha."
            g "What is it?"
            d "I really need some coffee right now. But I was in such a rush this morning that I forgot I hadn't packed my bag yet this morning..."
            d "I kind of left all of my things including my phone and wallet at home..."
            g "You even forgot your phone?"
            g "Second time in a row. That's a new record!"
            d "I know... Can I maybe borrow a bit of money to go get a coffee? I swear I'll pay you back."
            g "Don't worry about it. Of course!"
            g "One second. My wallet's in my jacket-"
            d "I got it!"
            "Rustle"
            d "Thank you so much Gabe."
            g "Any time!"
            g "Do you want to go out to maybe go grab a coffee together again sometime next week?"
            g "I'd have time pretty much any day."
            d "Sure! We can go on Monday if you want."
            g "Sweet! See you around today?"
            d "Probably. Thanks again. See you later Gabe."
            g "See ya!"
            scene bg_office_computer_kai
            d_t "That was nerve wrecking!"
            d_t "I hope he didn't see I slipped the chip in there when I took out his wallet..."
            d_t "Now I'll just have to wait and pray everything works as planned."
            d_t "Thinking about how he's acting so innocent after the things he did is making me sick."
            jump work4


        label work4:
            scene bg_office_computer_kai
            d_t "I can check if the tracker works..."
            #Show tracker screen
            "Ping"
            d_t "It works!"
            d_t "That's him. That's where he's at right now!"
            d_t "Yes!"
            d_t "Alright, Kai was right. This will work. I'm sure of it"
            d_t "What do I do now though?"
            d_t "I have to act as normal as possible."
            d_t "Might as well just get some work done then."
            d_t "Maybe I can distract myself a little."
            if call_police== True:
                scene bg_office_hallway
                o "Excuse me Madam."
                d "!"
                o "You're miss Sullivan I presume. I'm officer Rogan. We talked yesterday on the phone."
                d "Officer Rogan! Thank you for your effort. How can I help you?"
                o "I am here with a collegue today to look into what you mentioned on the phone."
                o "He is currently talking to the people you mentioned might be involved in miss Amari's dissapearence."
                o "I came to take a closer look at the images and messages you spoke of yesterday."
                d "I-"
                d "I'm really sorry. I should have sent them to you yesterday but I wasn't sure if it was the right thing to do."
                d "But this morning... When I got here everything was gone."
                d "All of it. Someone deleted it."
                o "Are you sure?"
                o "None of it is on this device anymore?"
                d "N-no. Truly, I tried everything but it's just gone!"
                o "You didn't by chance take a picture of any of it or made a copy?"
                d "No... I'm so sorry officer. I should have-"
                o "It's alright miss Sullivan. I believe you. May I take a look at the computer anyways?"
                o "Maybe we can find some other information that will aid us in finding miss Amari."
                d "Sure go ahead."
                "..."
                o "Alright so it does seem like some files were deleted yesterday evening around seven or eight."
                o "Do you have any idea who might have had access to this computer during that time frame?"
                d_t "I can't tell them yet. If they know who I'm suspecting they'll surely take him down to the police station to question him."
                d_t "If he knows they're on to something he won't risk going to Kai tonight."
                d_t "I have to stay vague again just one more time."
                d "We had a party here last night. There were so many people present yesterday. And everything was open, it could have been anyone."
                o "I understand."
                o "I would like to make a copy of the drive of this computer for further investigations and take the rest of the drawings left by her."
                d "Of course. Take what you need."
                o "Thank you miss Sullivan. I'm sure we will speak again as soon as we have been able to process the information we have been able to gather here today."
                o "As far as your safety goes, have you had any more strange happenings? Maybe at the party or on your way home?"
                d "No not really. Yesterday was alright."
                o "That's good to hear. As always if anything were to happen make sure to call us."
                d "Will do officer."
                o "ALright with that I think we're done here for now."
                o "I'll take this copy back to the station and my collegue will surely be done soon as well."
                o "We will notify you of our findings as soon as possible. Have a good day miss Sullivan."
                d "You too officer."
            else:
                pass
            #later that day
            d_t "It's getting late..."
            if track_who == 0:
                d_t "I'd ususally leave in about an hour to catch my bus. But it's possible Matt knows that and will still try to get me on my way home"
            elif track_who ==1:
                d_t "I'd ususally leave in about an hour to catch my bus. But it's possible Simon knows that and will still try to get me on my way home"
            else:
                d_t "I'd ususally leave in about an hour to catch my bus. But it's possible Gabe knows that and will still try to get me on my way home"
            d_t "Either I leave now and catch him off guard by going early or I wait until after he's gone."
            menu:
                "Leave now.":
                    d_t "Leaving now is the safer option. If I wait there might not be anyone around anymore at some point."
                    d_t "He might take the chance to wait until it's just us two left."
                    d_t "He can't do that if I leave early. Then I'll have enough time so see where he goes."
                    jump night4
                "Wait until he's gone.":
                    d_t "Leaving now might be a little too suspicious. If he sees me he might know something is up."
                    d_t "I can pack up and \"leave\" when I usually would but then wait somewhere in the bathroom until I see he's left the office."
                    d_t "As soon as he's gone I'll head straight home and check where he went."
                    jump night4

        

        label work4doubt:
            scene bg_office_hallway
            s "Good morning Destiny!"
            s "Here early again I see."
            d "Morning Simon."
            d "Yeah, I wanted to- ehm have enought time to look over what I did yesterday before we talk about it."
            s "Oh, sure"
            s "Take your time. Just come over to my office once you're ready."
            d "Yes. See you then."
            s "See you later Destiny."
            scene bg_office_computer_kai
            d_t "I just have to get throught this."
            d_t "Nothing bad is going to happen. I'm safe here"
            if call_police== Tue:
                d_t "The police will handle this as soon as they get here."
                d_t "Then I won't have to deal with her weird notes anymore either."
                d_t "I'm sure they're going to confiscate all of it."
                d_t "Oh god. I really should have told Simon I called them."
                d_t "This will cause such a scene."
                
            else:
                pass
            d_t "I'll just ignore the notes for now. I wasn't supposed to see them anyways."
            "Click"
            d_t "-"
            d_t "What?! But-"
            d_t "They're gone?!"
            d_t "This can't-"
            d_t "It's all gone!"
            d_t "Did I do something with them yesterday?"
            d_t "How could they just have dissapeared?"
            d_t "..."
            d_t "They were real. Right? They had to be."
            d_t "I wasn't imagining the messages."
            d_t "{i}Was I?{/i}"
            d_t "No. They were real!"
            if call_police==True:
                d_t "I told the police about these messages!"
                d_t "What are they going to do when they get here and there's nothing?"
                d_t "I'm going to look like a crazy fool-"
            else:
            d_t "Where did they go?"
            d_t "Did someone delet them?"
            d_t "But why? There wasn't anything destinctive on them."
            s "Destiny?"
            d "Ah!"
            "Crash"
            d "Sorry!"
            s "No I'm sorry! I didn't mean to startle you like that! Are you alright?"
            d "Oh! Simon? Yeah I'm ok."
            d "What is it?"
            s "Well, I just wanted to ask if you could maybe send me what's left of previous projects on Kai's computer. I want to be able to archive and date all of it correctly."
            d "S-sure I can do that."
            d "Right now?"
            s "If you don't mind. That would be great thank you."
            d "Of course. I'll send it in a minute."
            s "Fantastic. Thank you Destiny."
            d "Any time..."
            d_t "I have to get my act together. No one's here to hurt me. This is still the same office I've worked at for the past year."
            d_t "As long as I just do my work as usual and stay collected it's going to be fine."
            #Achievements start to glitch

        label night4stalk:
            #Later that day
            d "Gabe! There you are!"
            d "Let's go."
            g "Whoa, why in such a hurry all of a sudden?"
            d "Today was awful. I just want to go home..."
            g "What happened? Is there a problem with the project?"
            d "No, nothing like that."
            g "Oh?"
            g "What's the matter then?"
            d "I don't feel safe here."
            d "Those things I saw on her computer. They were all gone this morning."
            d "And no one knowing where she is..."
            d "It just doesn't sit right with me."
            d "I shouldn't just be replacing her."
            d "She said someone from work was pressuring her and now these strange things are starting to happen to me too."
            d "I think I should just go home."
            d "I'm scared someone here wants to do the same things to me that they did to her."
            g "What they did to her? What do you think happened?"
            g "Do you think she was kidnapped?"
            d "I don't know!"
            g "Oh Destiny, I'm sorry."
            g "Why didn't you tell me about this sooner. If you don't feel comfortable being here, then there's no need to stay."
            g "It's just work. You can take a day off if that's what you need."
            g "You could have told Simon you weren't feeling well."
            d "But I'm scared to go alone."
            g "I understand. How about I bring you home. I'll keep you company until you're in your apartment."
            g "I'll make sure no one does anything to you."
            g "Let's get you Home ok? And once you're there you can lock the door and try to get some sleep."
            d "Thank you Gabriel..."
            g "Don't worry about it. I don't mind at all. Besides, I'd be scared too if those things happened to me."
            g "Now let's go."
            scene bg_d_corridor
            g "There we are. Feeling better?"
            d "Yeah. Thank you for bringing me home."
            g "Oh it's nothing. I want to know you're safe too."
            g "Lord knows there's enough creeps out there."
            g "You should go in now though. And make sure you lock your door."
            g "Double check it."
            d "Yeah yeah. I will."
            d "I'll Triple check it even."
            g "I'm sure you'll feel a lot safer once you're in the comfort of your own 4 walls again."
            d "Get home safe too Gabe. Or I'll feel even worse for making you do all this."
            g "Don't worry about me. I'll be home in no time."
            g "Night Destiny."
            d "Goodnight Gabe."
            "Lock"
            d_t "Finally."
            d_t "No one's getting in now."
            d_t "And nothing bad happened."
            d_t "I was just overthinking things as per usual."
            d_t "I should go make myself some dinner."
            "Rustle"
            if dinner_plans== False:
                d_t "Oh right, [catname]! Let's get them some dinner too."
                d "[catname]! I'm home."
                "..."
                d "I've got some good news! It's dinner time."
                d "?"
                d "[catname]?"
                d "You were so lively yesterday. Are you mad at me for leaving you all alone again for so long?"
                scene bg_d_kitchen
                d "[catname]?!"
                d "Where-"
            else:
                d_t "What?"
                d_t "Did I leave the window open?"
                scene bg_d_kitchen
                d_t "There's no breeze-"
            d "AHHH!"
            scene bg_black
            "Thud"
            d "MHHHM"
            s_k "Stop squealing you little brat."
            d "MRRH"
            s_k "URGH, Stop that!"
            s_k "I thought I told you to {i}shut up.{/i}"
            "Whack!"
            jump worst
        
        label night4:
            scene bg_d_kitchen
            d_t "That worked like a charm."
            #Achievement glitches to im not alone anymore
            d_t "!"
            d_t "It's Kai! The Achievement meant her!"
            d_t "He's there! I have to see where he went."
            #Check screen
            if track_who==0:
                d_t "That's right behind the office!"
                d_t "She was so close the entire time?"
                d_t "What's even back there?"
                d_t "..."
                d_t "Sound labs?"
                d_t "That doesn't seem like Matt at all."
                d_t "But maybe that's the point! No one would expect him to go there. That's the perfect place to hide someone."
                d_t "You can rent it out for however long you like and everything is sound proof."
                d_t "And it's so close. It wouldn't take long at all to get there directly from the office!"
                d_t "The lions den is a recording studio!"
                d_t "Tomorrow's the day. I can get her!"

            elif track_who==1
                if dinner_plans== True:
                    d_t "That's not too far from my ususal bus stop st the office!"
                    d_t "In the allyway..."
                else:
                    d_t "That's the ally where I found [catname]!"
                d_t "What could even be back there?"
                d_t "..."
                d_t "There's a storage unit!"
                d_t "He must have rented a storage unit to keep her locked up. No one checks on those."
                d_t "The lions den is a storage unit!"
                d_t "The lions den is a recording studio!"
                d_t "Tomorrow's the day. I can get her!"

            else:
                d_t "That's really close!"
                d_t "..."
                d_t "But that-"
                d_t "Isn't that where those really dingy apartment no one wants are?"
                d_t "The ones with barely any sunlight or windows..."
                d_t "Of course he would choose one of those to hide Kai!"
                d_t "They're cheap and really close. And no one even really lives there. So nobody would notice a thing."
                d_t "The lions den is an apartment!"
                d_t "The lions den is a recording studio!"
                d_t "Tomorrow's the day. I can get her!"
            
            
    label day5:
        label dream5:
            scene dream5
            k "You listened!"
            d "I did. I tried my best. I did what you told me to."
            d "I remembered you Kai."
            k "Thank you Dest i ny."
            k "F or givIng me hope."
            d "Was he there last night? Did your plan work."
            k "Yes he was he re. I did my b*st to let you k now."
            d "So it is you! The screen!"
            k "Screen... is tHat how it-_"
            k "It doesn't matTer now. He was h_re. You're- you have t0 follow through wi*th it."
            k "I, I don''t know h0w much more I can help you."
            k "I'm so tIred De*tiny."
            d "Just a little longer. Please, hold on! I'm going to get you out of there!"
            d "What do I have to do tomorrow to make sure everything works?"
            k "I, you... yOu have to Trust yourse7f. I trusf you Destiny."
            k "Pl3ase. {i}Th is has to work.{/i}"
            k "If_it doe sn't-"
            d "It will!"
            d "It will work Kai."
            d "All of your plans and tips have worked so far!"
            d "We'll get through this."
            d "You'll get through this."
            k "I-"
            d "You'll be ok!"
            k "Thank you."
            jump morning5

        label morning5:
            scene bg_black
            "Ping!"
            scene bg_d_window
            d_t "This is it!"
            d_t "It's all come to this. I can't mess this up."
            d_t "The screen's still here..."
            d_t "Thank you Kai."
            d_t "With your help I'll get you out of there today."
            #look at achievements
            d_t "\"This is it\""
            default a5_1= False
            default a5_2= False
            default a5_3= False
            default a5_4= False
            label achievements5:
                if a5_1==True and a5_2==True and a5_3==True and a5_4==True:
                    d_t "It will work." 
                    jump getready5
                else:
                    menu:
                        "A known loner":
                            $ a5_1= True
                            if track_who==0:
                                d_t "I have to get Matt to not be at his hideout. I have to get Kai to be alone in there."
                            elif track_who==1:
                                d_t "I have to get Simon to not be at his hideout. I have to get Kai to be alone in there."
                            else:
                                d_t "I have to get Gabe to not be at his hideout. I have to get Kai to be alone in there."
                            d_t "If I make it seem like I'll be alone tonight he's sure to want to follow me."
                            d_t "He's still tracking my phone so if I tell him I'll be alone on my way home he's probably going to follow that to get to me."
                            d_t "Just like he planned to yesterday."
                            d_t "If I find a way to make it look like I'm leaving like normal that will hopefully distract him for long enough to go find Kai."
                            if call_police==True:
                                d_t "I could get the police to help me trick and catch him."
                                d_t "If he follows them there will be enough time to free Kai."
                                d_t "I'll tell him I'll be alone then secretly leave earlier. By the time he'll have figured out that it's not me it'll be too late and the police can arrest him."
                            else:
                                d_t "I could sneak it into someones pocket while at work."
                                d_t "Someone that usually leaves around the same time as me."
                                d_t "I'll tell him I'll be alone then secretly leave earlier. By the time he'll have figured out that it's not me I'll hopefully already be gone with Kai."
                            jump achievements5
                        "Who can you trust?":
                            $ a5_2= True
                            if call_police == True:
                                d_t "I'll explain myself to the police once I've set everything up."
                                d_t "If I can get officer Rogan to help me we can get Kai and arrest him at the same time."
                                d_t "I just have to get them to trust me too..."
                            else:
                                if track_who == 2:
                                    d_t "I can't trus anyone."
                                    d_t "I don't know who I could even tell."
                                    d_t "No one would believe me..."
                                    d_t "I'll have to do this alone."
                                else:
                                    d_t "Maybe I can get Gabe to help me..."
                                    d_t "If I had someone to take my phone that knows what's going on they could trap him while he thinks he's following me."
                                    d_t "Gabe could alert the police once I have Kai and they could arrest him for good."
                                    d_t "I just don't knoe if Gabe will trust me..."
                            jump achievements5
                        "Back on square one":
                            $ a5_3= True
                            d_t "Back on square one?"
                            d_t "Am I going to fail?"
                            d_t "..."
                            d_t "No, I can't think like that. It's going to work."
                            d_t "I don't know how Kai knows what is going to happen. But I have to trust that what she is telling me will work and that her messages are there to help me."
                            d_t "Square one could be anything."
                            if track_who==0:
                                d_t "Maybe it's square one for Matt."
                            elif track_who==1:
                                d_t "Maybe it's square one for Simon."
                            else:
                                d_t "Maybe it's square one for Gabe"
                            d_t "Maybe things will finally go back to the way they were..."
                            jump achievements5
                        "You reap what you sow":
                            $ a5_4= True
                            d_t "It all comes down to this doesn't it."
                            d_t "If I do everything right I'll get to free her."
                            d_t "But if I don't..."
                            jump achievements5
            
        label getready5:
            scene bg_d_kitchen
            if dinner_plans ==True:
                d_t "If there was ever a day for coffee then it's today."
                d_t "We won't have anymore stains this time around though. I'll make sure of that."
                jump work5
            else:
                d "Good morning [catname]."
                d "Today's going to be a stressful day..."
                c_n "Prrrrr"
                d "Thank you [catname]. I know you don't really have a choice. But you being here makes me feel a little more secure."
                d "You're just a little kitty but you've really grown on me. I'll miss you when we finally find your real owners."
                c_n "Meeauw"
                d "We'll find them. Just like we'll find Kai today."
                c_n "Mrrm"
                d "Now let me get you some food. I bet you're hungry already."
                c_n "MEaUW!"
                d "Haha now thats my little [catname]. Food really gets you going huh?"
                jump work5


        label work5:
            scene bg_office_hallway
            s "Morning!"
            d "Morning Simon. I see you're here early again as usual."
            s "Well, you to I suppose."
            s "Great work yesterday by the way! I saw what you sent in and it looks fantastic!"
            s "I'm really looking forward to see what else you'll bring to the table."
            d "Thank you. I'm glad it's to your liking."
            d "And I'm glad I found a way to incorprate Kai's work into it too. {i}I hope she doesn't mind...{/i}"
            s "What was that?"
            d "Oh it's nothing. I'm just glad I can live up to the standard that Kai set. That's all."
            s "We'll you're doing more than fine so far. Keep it up!"
            d "I will!"
            s "As always if you need anything or are unsure about anything you can always come to me for help."
            d "Thank you Simon."
            scene bg_office_computer_kai
            if track_who== 0:
                d_t "I have to find a reason to talk to Matt again. I have to somehow subtly let him know that today's the day he should make his move."
                d_t "Without it seeming weird or completely out of left field..."
                d_t "I can't just go up to him and tell him \"Hey! I'll be going home totaly alone today. Oh you know. Just in case you feel like kidnapping me tonight!\""
                d_t "It has to seem natural."
                d_t "And I should buy myself more time by saying I'll go quite late."
                d_t "Actually!"
                d_t "What if I ask him about coming in on the weekend."
                d_t "I could ask him if the office is open on Saturdays. Then I could \"finish an important design\"."
                d_t "That would give a reason and make it seem more natural to mention that I'd also be working late today."
                d_t "That sounds good. I'll tell him that."
                jump trickmatt
            elif track_who== 1:
                d_t "I have to find a reason to talk to Simon again. Maybe something about work again, like last time?"
                d_t "I have to somehow subtly let him know that today's the day he should make his move."
                d_t "Without it seeming weird or completely out of left field..."
                d_t "I can't just go up to him and tell him \"Hey! I'll be going home totaly alone today. Oh you know. Just in case you feel like kidnapping me tonight!\""
                d_t "It has to seem natural."
                d_t "And I should buy myself more time by saying I'll go quite late."
                d_t "He ususaly stays quite late as well anyways."
                d_t "Actually!"
                d_t "What if I just let him know that I'm working on something and am planing to send it to him in the evening."
                d_t "If I mention that it's probably going to get a bit later he'll know I'm staying without it seeming suspicious."
                d_t "Yeah, I'll do that."
                jump tricksimon
            else:
                d_t "I have to find a reason to talk to Gabe again. I have to somehow subtly let him know that today's the day he should make his move."
                d_t "Without it seeming weird or completely out of left field."
                d_t "I can't just go up to him and tell him \"Hey! I'll be going home totaly alone tonight. Oh you know. Just in case you feel like kidnapping me tonight!\""
                d_t "It has to seem natural."
                d_t "It's not like I'd have anyone else to walk home with anyways. But still I should make it clear that I'm planning to even go without him."
                d_t "The easiet way would probably be to tell him I'll stay late. He usually likes leaving a little early."
                d_t "That would also buy me a little more time to find Kai before he catches on."
                d_t "Actually."
                d_t "I think I can just pay him back for the coffee from yesterday and then add I'll be working late afterwards. That wouldn't be out of character and I think it should do the trick."
                jump trickgabe
                
        label trickgabe:
            #Later that day
            scene bg_office_hallway
            d "Hey, Gabe."
            g "Oh! Destiny. What are you doing here? Need a break from work?"
            d "After the last couple of days definetely. But no, that'll have to wait for the weekend."
            d "I actually just wanted to quickly pay you back for the coffee you payed for yesterday. You know. Because I forgot my wallet."
            g "Oh, right! You don't need to do that. Keep it! It's my treat."
            d "Are you sure? It's really no problem I have it right here."
            g "Yeah I'm being serious. You don't have to pay me back for that. See it as a token of our friendship."
            g "Besides, it wasn't that much anyways. What was it? Like 3 bucks?"
            d "Thank you Gabe that's so kind of you."
            g "It's my pleasure."
            d "Oh! By the way. I'll be working late again today. We probably won't see eachother on our way home. I still have something I want to finish before the weekend."
            g "Again? Wow, you're really putting in the work for this new Project."
            g "What time are you planning to leave then?"
            d "I don't know yet. But definitely later than usual."
            g "Make sure you're not overdoing it ok?"
            d "Yeah I know. I'll take more time off next week. I just have to make sure I make a good first impression you know."
            g "I think they're all very impressed already. But I understand. Don't get home too late."
            g "With everything you told me happened recently I just don't like the thought of you staying here so late..."
            d "It's going to be fine. I'll be around other people most of the time."
            d "And if something happens I'll call you."
            g "Okay..."
            g "But only if you promise!"
            d "I promise!"
            g "Alright. Then goodluck tonight."
            d "Thanks. Have a good night too!"
            g "I sure will."
            d_t "We'll see about that."
            jump allies


        label trickmatt:
            #Later that day
            scene bg_office_hallway
            d "Uhm. Matthew?"
            m "Again? What is it this time? Can't make it on that day?"
            d "No, no it's nothing like that. I actually wanted to ask if it's possible I come here to work tomorrow?"
            m "Excuse me?"
            d "I have something to finish and I don't think I'll get it done today."
            d "I've already decided that I'll stay longer tonight but being able to come in tomorrow as well would really help to get this done."
            m "You're staying late and you want to work on a Saturday?"
            d "Yes."
            m "You, Destiny Sullivan. Always last minute Sullivan want to come in on a Saturday?"
            d "Yes."
            m "..."
            m "Sure. Be my guest. Simon must have really done a number on you if you're willing to work on your weekend."
            m "The doors lock at around 9 tonight but I would imagine by then you'll be gone already."
            m "Tomorrow morning the front door should be locked but I can give you a temporary code so you can get in."
            d "Fantastic!"
            m "{i}What's up with you?{/i}"
            d "Huh?"
            m "Nothing. Not that it matters. I'll send you the code tomorrow morning."
            m "Don't get yourself locked in tonight. What time are you planning to leave?"
            d "I wont. Don't worry. But I'm not quite sure yet. Thank you Matthew."
            m "Whatever you say. {i}I don't know what you're trying to pull.{/i}"
            d "I just want to start out strong that's all."
            m "Yeah, of course..."
            m "Is that all?"
            d "Yeah. Thanks again. I'll be going then."
            m "Bye."
            d_t "Oh no he senses something is up. I have to be really careful from now on."
            jump allies

            
        label tricksimon:
            d "Hey, Simon. You got a minute?"
            s "Yeah sure what's up?"
            d "I started on that idea I showed you yesterday. I'll be on it for a while though."
            s "Sure that's not a problem. Take your time."
            d "I just thought since the weekend is coming up and I want to get this done this week I'll be staying a bit later today."
            s "Oh?"
            d "Yeah. I'll send it to you once I'm finished but it will probably be a bit later than ususal."
            s "That's fine. I'll be here a little longer too. But even if I'm gone by then I'll have a look at it as soon as I get the chance."
            s "Around what time are you planning to leave?"
            d "I'm not quite sure yet but later than usual that's for certain."
            s "Alright, thank you for letting me know."
            s "I have to say you've been really throwing yourself into work these past few days. You've really got a fire for this it seems."
            d "It's just important to me to do this right. Since I'm picking up on someone elses work."
            s "Ah, I understand. Don't worry I'm sure Kai would be very happy with the choices you've made so far."
            d_t "I'm sure she would..."
            d "Thanks. I'll get back to work then."
            s "Good luck!"
            jump allies

        label allies:
            if call_police==True:
                scene bg_office_computer_kai
                d_t "I have everything I need now. The plan is set up."
                d_t "I should try to get officer Rogan on my side now."
                d_t "I'm sure that if I tell him everything that's happened and why I didn't tell him right away he'll help me."
                d_t "I can't tell them about the dreams but I can tell them I got a message from Kai somehow."
                d_t "I'll have to explain everything but their help would be essential to getting Kai out of there and getting him arrested."  
                d_t "I hope he believes me..."
                d_t "I have to atleast try!"
                "Ring"
                o "Miss Sullivan! This is officer Rogan speaking. How may I assist you?"
                d "I have something I need to tell you..."
                #after explaining everything    
                o "I see. So you felt you had to act this way to ensure the location of miss Amari could be found..."
                d "I'm sorry I wasn't completely honest before but I believe I have figured out who is the cause of Kai's dissapearence and where he is keeping her."
                d "I have used a tracking device to locate her. My phone is being tracked as well."
                d "Which is why I made a plan to misslead him by giving my phone to someone else and use that time to free Kai."
                o "And you've waited this long to inform us of this plan?"
                d "Again I'm really sorry I've kept this from you for so long but if you could help me I think this plan could work!"
                o "I am finding it hard to understand why you have waited this long to inform us but I admit that your plan could indeed work."
                o "If the location you have found is accurate we could send a squad there to look for miss Amari while using another female officer to lure the culprit somewhere we can safely arrest him."
                d "Yes! Thank you so much officer."
                o "I can send over one of my fellow officers to come pick up your phone and get you out of there safely."
                o "We'll have someone escort you home then."
                d "Would it be possible I join the team that will look for Kai?"
                o "Madam I assure you. We are trained safety personnel. We can handle things form this point onwards." 
                d "I know it's just..."
                d "If they really find her then I have to talk to her..."
                d "I know what she went through. She messaged me. Maybe I can help find her."
                o "I understand your concern miss Sullivan. But such a mission is very dangerous and not suited for civilians."
                d "I know. But I would rather be there when she's found. I'm sure she would also appreciate seeing the person she contacted there when she gets out."
                o "You might have a point but I'll repeat. It will be dangerous."
                d "I understand what you're trying to warn me about. I was prepared to do this on my own but I have the police to help me now. I want to be there."
                o "Fine. But you will need to wait to talk to miss Amari until we have made sure it is safe."
                d "Thank you officer! I don't know what I would do without your help."
                o "This is my duty miss Sullivan. I will call you once the officers have arrived."
                o "We will have to be very cautious."
                d "Understood. I'll be waiting."
                "Click"
                jump trustpolice
            else:
                if track_who==2:
                    jump trustnoone
                else:
                    d_t "I have everything I need now. The plan is set up."
                    d_t "I should tell Gabe about this"
                    d_t "Maybe if I tell him everything he'll be willing to help me."
                    d_t "I'll have to explain everything to him. But with Gabe's help getting Kai out of there and making sure that psycho gets arrested would be so much easier."
                    d_t "I wouldn't have to do it alone..."  
                    d_t "I hope he believes me."
                    d_t "I'm going to sound absolutely crazy. But I have to atleast try!"
                    scene bg_office_hallway
                    d "Gabe? Can I talk to you for a minute. It's important."
                    g "What is it? You look worried."
                    d "Can we go somewhere else to talk.? Somewhere more private."
                    g "Uhm, Y-yeah. Sure."
                    scene bg_office_printer
                    g "What's going on. What do you want to talk to me about?"
                    d "I have something to admit to you."
                    d "About what's been happening this week. With Kai and also some other things..."
                    #after explaining everything  
                    g "Ok ok wait!"
                    g "You have been seeing this floating screen the entire week. Telling you what is going to happen on that day."
                    g "And you've been seeing Kai in your dreams telling you she was kidnapped and helping you figure out who it is?"
                    d "I know it sounds crazy but you have to believe me! All of this weird stuff that's been happening. The knocking and Kai's creepy sketches."
                    d "That message she wrote"
                    if track_who==0:
                        d "It's Matt. He did this to her. And I finally know where he took her."
                    else:
                        d "It's Simon. He did this to her. And I finally know where he took her."
                    d "I know how I can get her out of there but I don't know if I can do it on my own..."

                    if gabe_hints==3:
                        $ gabe_ally= True
                        g "I- "
                        g "I believe you Destiny."
                        g "None of this makes any sense to me but I believe you. If you're telling me that's what you know then I have to trust that that's true."
                        g "I just-"
                        g "How did it come to this?"
                        g "Why would he do such a thing?"
                        d "I don't know Gabe."
                        d "I'm scared too."
                        d "But that's why I need your help."
                        d "I can't do this alone."
                        g "What can I even do?"
                        d "I need you to take my phone. He's tracking it but once he figures out you have it he'll know we're onto him and won't risk hurting you."
                        d "You have to leave the office a little later than ususal. I made him think that's what I'd do."
                        d "While he's waiting for who he thinks is me I'll already be on my way to where he's keeping Kai."
                        if track_who==0:
                            d "By the time Matt would even get the chance to figure out that he's been tricked we'll both already be long gone."
                        else:
                            d "By the time Simon would even get the chance to figure out that he's been tricked we'll both already be long gone."
                        d "Once Kai is free we can call the cops on him and this whole nightmare will be over!"
                        g "Are you sure this is going to work?"
                        d "I- it has to. This is the only way I know to get Kai out of there. If we don't stop him I don't know what would happen to me-"
                        d "She's always been right so far. It's going to work!"
                        g "I trust you Destiny."
                        if track_who==0:
                            g "If you need my help I'll be there. I'll try to stall for you as much as I can. I'll try to lead Matt away from where you're going."
                        else:
                            g "If you need my help I'll be there. I'll try to stall for you as much as I can. I'll try to lead Simon away from where you're going."
                        g "But I can't keep him distracted forever."
                        g "Here take my phone. That way I can contact you if I think he's figured out it's not you he's following."
                        g "And as soon as you've freed Kai you call me. Ok? I'll let the police know where you are and tell them everything."
                        g "Try to stay safe Destiny."
                        d "Thank you Gabriel. I'll do my best. I don't know what I'd do without you."
                        g "Be careful out there."
                        d "I will."
                        jump trustgabe

                    else:
                        g "I- "
                        g "None of this makes any sense. Why are you telling me this all of a sudden?"
                        g "I can't believe this. Psychic dreams? A screen?"
                        g "I've never heard of anything like this."
                        if track_who==0:
                            g "And you think Matt kidnapped Kai? He would never do such a thing!"
                        else:
                            g "And you think Simon kidnapped Kai? He would never do such a thing!"
                        g "What would he gain from it?"
                        d "I don't know!"
                        d "You have to believe me Gabe! I'm not crazy."
                        d "I've seen these things. They're real. Kai talked to me. I can get her out of there."
                        g "Out of where? You don't even really know what is in that place."
                        g "Destiny, I don't think you're crazy but this isn't right. I think you're scared and overworked and have been for too long now."
                        g "These nightmares you're discribing. They're making you paranoid. This sounds like some crazy movie plot. Do you have any evidence for what you're claiming he did?"
                        d "I-"
                        g "Did you see him at the door? Or did you find the tracker she said he put on your phone?"
                        d "I don't-"
                        g "This is all so sudden. I'm worried about you Destiny. I don't think you're ok."
                        g "If you really think someone is after you we can go to the police together. But I'm not helping you execute some crazy plan to free a woman you don't even know for certain was kidnapped."
                        d "Gabe..."
                        g "I'll come to the police station with you tonight. Then we can figure this out with them."
                        g "I'm sorry Destiny but I don't think-"
                        d "You don't have to explain it to me. I understand. I know I sound crazy..."
                        g "Destiny-"
                        d "No, you're right. It's probably just paranoia. I don't know why any of this is happening to me. I'm scared."
                        d "I think I need to go talk to someone about this..."
                        g "Do you want me to take you home?"
                        d "No. It's fine. I'll stay here. I'm sorry I made you worry."
                        g "Please, Destiny. If you're not feeling well then take a break."
                        d "Yeah... I'll be fine."
                        d "See you later Gabe."
                        g "See you Destiny..."
                        scene bg_office_computer_kai
                        d_t "I have to do this on my own."
                        d_t "That was so stupid!"
                        d_t "I should have known he wouldn't believe me!"
                        d_t "It sounds absolutely insane. I don't blame him for thinking I'm going crazy. Anyone would."
                        d_t "I mean even I think I might slowly be going crazy."
                        d_t "But I can't go back now. I have to follow through wit the plan."
                        d_t "I have to get Kai out of there. Even if that means I'll have to do it all by myself."
                        jump trustnoone
        
        label trustgabe:
            scene bg_office_computer_kai
            #check phone
            d_t "It's about time I prepare to go..."
            d_t "4:30PM. Yeah, it's go time."
            #text gabe I'm going now good luck
            if track_who==0:
                jump studiogabe
            else:
                jump storagegabe


        label trustpolice:
            if track_who==0:
                jump studiopolice
            elif track_who==1:
                jump storagepolice
            else:
                jump apartmentpolice

        label trustnoone:
            scene bg_office_cafeteria
            #at lunch
            d_t "I need to slip my phone to someone that will stay here for a little longer than I'd usually work."
            d_t "Someone that doesn't move around too much..."
            if track_who==1:
                d_t "I can give it to Matt. He's quite stationary. And his office is pretty close to mine."
            else:
                d_t "I can give it to Simon. He's quite stationary. And his office is right next to mine."
            d_t "I'll slip him the phone and then go back to my desk. Leaving now would be too suspicious. I can't risk getting caught not being here while my phone is here."
            d_t "I'll have to wait until the afternoon to start the plan."
            #later that day
            scene bg_office_computer_kai
            #check computer
            d_t "It's about time I prepare to go..."
            d_t "4:30PM. Yeah, it's go time."
            if track_who==0:
                d_t "The sound studio is right here so I won't have too much of a buffer."
                d_t "That just means I have to make sure everything has to go smoothly."
                jump studioalone
            elif track_who==1:
                d_t "The storage rental is not too far away so I won't have too much of a buffer."
                d_t "That just means I have to make sure everything has to go smoothly."
                jump storagealone
            else: 
                d_t "The apartment is quite a good distance away so I'll have a bit of a buffer."
                d_t "But if Gabe figures out I'm gone while I'm still on my way there I could be in a fair bit of trouble."
                d_t "That just means I have to make sure everything has to go smoothly." 
                jump apartmentalone          
        
        
        label storagealone:
            scene bg_ally
            d_t "It's back here."
            d_t "Jeez this place is even creepier than the first time..."
            d_t "I hope no one is here."
            d_t "That's the storage units!"
            d_t "I found it!"
            d_t "Shoot! There's so many..."
            d_t "Which one is he keeping her locked up in? I can't go through all of them."
            #achievements glitch to square ONE
            d_t "Unit one?"
            d_t "Are you here Kai?"
            d_t "I have to try unit one!"
            "Creak"
            d "Urgh!"
            d_t "This stupid door won't-"
            "Crash!"
            d "Finally!"
            scene bg_room
            d "Kai?"
            k "Destiny!"
            d "Kai!"
            k "You came!"
            k "You really came!"
            d "I found you!"
            d "You were right. All of it was right!"
            k "I'm- Thank you. "
            d "So it really was you. You helped me. In those dreams"
            k "Dreams..."
            k "You heard me?"
            d "I did. I don't know how you did it but I saw you Kai. And the screen. It was you wasn't it."
            k "I don't know how-"
            k "It worked."
            d "Yes, it worked!"
            d "I can get you out of here."
            d "We have to get you to a hospital! You're completely dehydrated."
            k "I-"
            d "It's alright. I'll help you out of here."
            d "As soon as we're down at the street we can ask someone to call you an ambulance."
            d "Tell them everything."
            k "Everything?"
            d "Everything!"
            d "They can make sure you're safe there."
            d "They can even get the police involved. But first we have to get you somewhere safe."
            d "Let's go!"
            #after calling a cab
            scene bg_street
            d "I'm sorry Kai they said I can't ride along. But I've already called a cab and I'll be there with you soon. I promise."
            k "Destiny. Thank you."
            k "Thank you so much."
            k "I don't know what I would have-"
            d "It's ok Kai. You're safe now. Simon can't hurt you anymore."
            k "Just, thanks."
            d "I'll see you later."
            k "Bye Destiny."
            "Slam!"
            "*Siren*"
            d_t "I'll be there soon."
            d_t "Don't worr-"
            scene bg_black
            "Wrap"
            d "MHHHM"
            s_k "{i}Stop squealing you little brat.{/i} We can handle this nice and quiet."
            "Rustle"
            d "MRRH"
            s_k "URGH, Stop that!"
            s_k "You thought I wouldn't notice?"
            d "MPHF"
            s_k "Didn't I tell you to {i}shut up.{/i}"
            "Whack!"
            jump bad

        label storagegabe:
            scene bg_ally
            d_t "It's back here."
            d_t "Jeez this place is even creepier than the first time..."
            d_t "I hope no one is here."
            d_t "That's the storage units!"
            d_t "I found it!"
            d_t "Shoot! There's so many..."
            d_t "Which one is he keeping her locked up in? I can't go through all of them."
            #achievements glitch to square ONE
            d_t "Unit one?"
            d_t "Are you here Kai?"
            d_t "I have to try unit one!"
            "Creak"
            d "Urgh!"
            d_t "This stupid door won't-"
            "Crash!"
            d "Finally!"
            scene bg_room
            d "Kai?"
            k "Destiny!"
            d "Kai!"
            k "You came!"
            k "You really came!"
            d "I found you!"
            d "You were right. All of it was right!"
            k "I'm- Thank you. "
            d "So it really was you. You helped me. In those dreams"
            k "Dreams..."
            k "You heard me?"
            d "I did. I don't know how you did it but I saw you Kai. And the screen. It was you wasn't it."
            k "I don't know how-"
            k "It worked."
            d "Yes, it worked!"
            d "I can get you out of here."
            d "We have to get you to a hospital! You're completely dehydrated."
            k "I-"
            d "It's alright. I'll help you out of here. I have to tell Gabe I found you!"
            #phone text gabe
            d "As soon as we're down at the street we can ask someone to call you an ambulance."
            d "Tell them everything."
            k "Everything?"
            d "Everything!"
            d "They can make sure you're safe there."
            d "They can even get the police involved. But first we have to get you somewhere safe."
            d "Let's go!"
            #after calling a cab
            scene bg_street
            "Ring"
            d "Gabe!"
            d "Are you ok? What happened?"
            g "You were right! Simon followed me. I tried leading him into a dead end and hiding the phone and it worked!"
            g "I called the police after ehm- well, I tried to pin him down."
            d "You did what!?"
            g "He tried to get away but I got him on the ground. I think I might have black eye now but the police arrived just in time."
            d "Gabe!"
            g "I'm fine. Trust me. But you were right."
            g "I can't believe it."
            g "Simon?"
            d "Yeah..."
            d "Thank you Gabe. I don't think words can describe how grateful I am right now."
            g "You got her!"
            d "Yeah, I did!"
            d "It all worked. Kai's plan worked."
            d "I still can't believe it. She's on her way to the hospital now. she was really dehydrated."
            g "That's good. I'm on my way home now."
            g "I told the police everything and they said they'd take care of the rest."
            d "I'll be going to the hospital to accompany Kai but I'll text you when I get home."
            g "Tell her I wish her a fast recovery."
            d "I will."
            d "See you later tonight maybe. But just in case. Good night."
            g "You too Destiny. See ya."
            "Click"
            k "Who was that?"
            d "That was Gabe. My friend. He helped me get you out."
            d "Simon's gone now."
            k "What?"
            d "The police arrested Simon. He can't hurt you anymore."
            k "You got him?"
            d "Yeah. He won't be able to do that to anyone anymore."
            k "Destiny. Thank you."
            k "Thank you so much."
            k "I don't know what I would have-"
            d "It's ok Kai. You're safe now. It's over."
            k "Just, thanks."
            d "I'll see you later."
            d "They said I can't ride along. But I've already called a cab and I'll be there with you again soon. I promise."
            k "Bye Destiny."
            "Slam!"
            "*Siren*"
            jump best
            
        label storagepolice:
            #at the scene with the cops.
            scene bg_ally
            "*Police radio noises*"
            o "They're at the storage units now. Which unit is she in."
            d "I-"
            #achievements glitch to square ONE
            d "It's unit one!"
            d "She's in unit one."
            o "Alright.{i} Unit one everyone. Be careful there could be traps or sensors.{/i}"
            d "Are they going in now?"
            o "Yes they're entering the building now. It shouldn't take too long for them to get to the right unit."
            o "We'll have to be patient and wait for their response. As soon as they've found something they'll let us know."
            d "She has to be there..."
            "{cps=1}...{/cps}"
            "*Radio noise*"
            d "Did they find her?!"
            o "Yes she's there!"
            o "They were able to locate miss Amari! She looks exhausted and seems dehydrated but ultimately she seems to be in stable health."
            d "I have to talk to her!"
            d "Please! Can I go in?"
            o "One moment. They're checking the rest of the unit right now."
            o "Once they're done it's safe for you to go in."
            d "I have to see her. I have to know she's safe."
            o "Alright. We can go in."
            scene bg_room
            d "Kai?"
            k "Destiny!"
            k "You came!"
            k "You really came!"
            k "Thank you..."
            d "So it really was you. You helped me. In those dreams"
            k "Dreams..."
            k "You heard me?"
            d "I did. I don't know how you did it but I saw you Kai. And the screen. It was you wasn't it."
            k "I don't know how-"
            k "It worked."
            o "I'm sorry to interrupt your reunion but we should get miss Amari to a hospital to get her vitals checked and a forensics team here to take care of this place."
            d "Yes of course officer."
            k "Thanks."
            o "We'll take care of the rest."
            o "Miss Sullivan. We'll take you back to your apartment now."
            d "But-"
            o "You'll be pleased to hear that our other team was able to arrest mister Harris."
            o "Your intuition was right. He followed us right into the trap."
            o "Thank you for your help miss Sullivan."
            d "They have him?"
            o "Yes. He's in police custody now."
            k "They got Simon-"
            d "He's not going to hurt anyone anymore."
            k "I'm safe."
            o "You're safe miss Amari."
            o "So, are you ready to go?"
            o "We will acompany you both to your destinations. And as for you miss Sullivan there will be an officer stationed at your apartment."
            o "For your safety and just in case any problems should arise."
            d "Let's get going then."
            jump best

        label apartmentalone:
        label apartmentpolice:
            #at the scene with the cops.
            scene bg_street
            "*Police radio noises*"
            o "They're at the building now. Which apartment is she in."
            d "I-"
            #achievements glitch to square ONE
            d "It's number one!"
            d "She's in apartment one."
            o "Alright.{i} Apartment one everyone. Be careful there could be traps or sensors.{/i}"
            d "Are they going in now?"
            o "Yes they're entering the apartment now. It shouldn't take too long for them to get to the right room."
            o "We'll have to be patient and wait for their response. As soon as they've found something they'll let us know."
            d "She has to be there..."
            "{cps=1}...{/cps}"
            "*Radio noise*"
            d "Did they find her?!"
            o "They said the place was empty..."
            o "No trace of miss Amari anywhere."
            d "Did Gabe move her? Was I not careful enough?"
            d "How could I let this happen!"
            d "I have to see for myself. Please, can I enter the apartment?"
            o "Hmmm"
            o "I suppose since there is no one there it should be fine."
            scene bg_room
            d "Kai?!"
            "..."
            o "She's not here miss Sullivan. They've checked everywhere. The place is empty."
            d "But that can't be- She has to be here!"
            "*Radio noise*"
            o "{i}What?{/i}"
            d "What is it? What did they say?"
            o "They've arrested the person that was behind all of this. Your intuition was right. He followed us right into the trap."
            o "The only problem is it wasn't mister Anderson they caught..."
            d "What?"
            o "It was Simon Harris"
            d "Simon?!"
            d "I-"
            d "Oh no..."
            d "Kai!"
            d "He's the only one that knows where she is!"
            d "She won't survive in there much longer. We have to find her!"
            o "Calm down miss Sullivan. I promise you we'll look for miss Amari."
            o "Thanks to your help we now have her captor."
            d "But that's nit enough! She's still out there. He's not going to tell you where she is."
            d "What if you don't find her in time?"
            o "We are doing our best to get to her location but for now there is nothing more we can do here."
            o "We'll take care of the rest. But you sould be brought back to your apartment now."
            o "An officer will drive you home and make sure you get there safely."
            d "But-"
            o "Thank you for your help miss Sullivan."
            o "You won't need to worry about mister Harris anymore. He's in police custody now."
            d "He's not going to hurt anyone anymore?"
            o "You're safe now miss Sullivan."
            d "He's gone.."
            o "Are you ready to go?"
            o "There will also be an officer stationed at your apartment tonight."
            o "For your safety and just in case any problems should arise."
            d "Let's go..."
            jump good

        label studioalone:
        label studiogabe:
        label studiopolice:
            #at the scene with the cops.
            scene bg_street
            "*Police radio noises*"
            o "They're at the building now. Which studio is she in."
            d "I-"
            #achievements glitch to square ONE
            d "It's number one!"
            d "She's in studio one."
            o "Alright.{i} Studio one everyone. Be careful there could be traps or sensors.{/i}"
            d "Are they going in now?"
            o "Yes they're entering the corridor now. It shouldn't take too long for them to get to the right room."
            o "We'll have to be patient and wait for their response. As soon as they've found something they'll let us know."
            d "She has to be there..."
            "{cps=1}...{/cps}"
            "*Radio noise*"
            d "Did they find her?!"
            o "They said the place was empty..."
            o "No trace of miss Amari anywhere."
            d "Did Matt move her? Was I not careful enough?"
            d "How could I let this happen!"
            d "I have to see for myself. Please, can I enter the apartment?"
            o "Hmmm"
            o "I suppose since there is no one there it should be fine."
            scene bg_room
            d "Kai?!"
            "..."
            o "She's not here miss Sullivan. They've checked everywhere. The place is empty."
            d "But that can't be- She has to be here!"
            "*Radio noise*"
            o "{i}What?{/i}"
            d "What is it? What did they say?"
            o "They've arrested the person that was behind all of this. Your intuition was right. He followed us right into the trap."
            o "The only problem is it wasn't mister Ledger they caught..."
            d "What?"
            o "It was Simon Harris"
            d "Simon?!"
            d "I-"
            d "Oh no..."
            d "Kai!"
            d "He's the only one that knows where she is!"
            d "She won't survive in there much longer. We have to find her!"
            o "Calm down miss Sullivan. I promise you we'll look for miss Amari."
            o "Thanks to your help we now have her captor."
            d "But that's nit enough! She's still out there. He's not going to tell you where she is."
            d "What if you don't find her in time?"
            o "We are doing our best to get to her location but for now there is nothing more we can do here."
            o "We'll take care of the rest. But you sould be brought back to your apartment now."
            o "An officer will drive you home and make sure you get there safely."
            d "But-"
            o "Thank you for your help miss Sullivan."
            o "You won't need to worry about mister Harris anymore. He's in police custody now."
            d "He's not going to hurt anyone anymore?"
            o "You're safe now miss Sullivan."
            d "He's gone.."
            o "Are you ready to go?"
            o "There will also be an officer stationed at your apartment tonight."
            o "For your safety and just in case any problems should arise."
            d "Let's go..."
            jump good
        
        
    label outro:
        label worst:
        label bad:
        label good:
        label best:

        

    

    # This ends the game.

    return
