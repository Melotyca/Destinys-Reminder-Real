﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Destiny", color="#1db78b", what_color="#58deb8")
define d_t = Character("Destiny", color="#1db78b", what_italic=True, what_color="#70a797")
define g = Character("Gabriel", color="#AED628", what_color="#cae66d")
define m = Character("Matthew", color="#639af9", what_color="#98baf7")
define s = Character("Simon", color= "#ff6961", what_color="#ff9e98")
define x = Character("?", color="#b6b2b2", what_italic=True )

# The game starts here.

label start:
    label wakingup1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

        scene bg_black
        x "Destiny..."
        x "Destiny!"
        x "You have to listen to me."
        x "Something bad is going to happen."
        x "Please."
        x "Don't trust him. You're in danger"
        x "I can help you."

        "Ping!"
        d_t "What was that?"
        d_t "*Ugh* What time is it even. Feels like I've only just fallen asleep."  
    # (phone appears(see Her reminder Project due tomorrow, Day and time: Sun 06:27). 
        d_t "Oh come on, already?"  

    # (back to blackspace for a little while) 
        d_t "Why can't it be like 4."
        d_t "Ugh doesn't matter. If I stay in bed now I'll be late."  
        
        scene bg_d_bed
        d_t "Coffee time!"   

        scene bg_d_kitchen
        d_t "Man I really need to get more sleep today." 
    #(phone appears, time now 07:03)
    #unlock)   
    #(home screen, a couple apps, no notifications waits a little). 
    #(gets a message from Gabriel (Omw! Hope you didn’t overseep again ;)), ). 
        d_t "Oh shoot!"
        d_t "I gotta find something to wear."  
    #(destiny looks around, window, corridor back to kitchen/messy).

        d_t "Jeez I really have to clean this up soon. When did I even wear that shirt? God even my desk is filled."
        d_t "Actually, I don't think I've ever seen that screen of Achievements over there."
        d_t "Wait."
        d_t "ACHEIVMENTS!?"   
    #(background gets a bit darker as Achievements stand out.). 
        d_t "What in the-"   

    #(achievement screen: ). 
    #Achievements today:   
    #- That stain is stayin.
    #- Under Matts watch.
    #- This food is flipping good. 
    #- Jam on! 
    # Comforting stroll. 

        d  "Heh. Heh he..."  
        d_t "A display. Really?"  
        d_t "Oh god. No more games before bed."
        d_t "What's next. Some NPC walks through my door? As if."
        d_t "This can't be serio-" 
        "{i}Knock knock.{/i}" 
        d "AH!" 
    #(cup falls and shatters and spills). 
    #(shattered mug). 
        g "It's me, Gabe. Is everything alright in there?"   
        d "Yes yes! On my way."
    #door opens
        scene bg_d_corridor 
        g "I'm sorry. I didn't mean to startle you"  
        d "No, no. It's fine! I just. Uhm. Didn't expect you yet."  
        d_t "Oh god this shirt is ruined." 
        g "Well then, the usual Destiny then." 
        g "But are you sure you're alright Destiny? You look a little shaken."  
        d "Oh, shut it. You almost scared me to death." 
        d "I still have to get ready. Make yourself at home."  

        scene bg_d_kitchen
        d "Please just ignore the mess. I'm working on it I promise." 
        d "Oh and don't bother with the mug. I'll clean it up later too."  
        g "Oh no not the chipmunk mug." 
        g "I really liked that one. I think your mom gave you that right?"  
        d "Mhm. Must've been easter or something like that."  
        d_t "Shoot! What am I going to wear now?"  
    #Narrator: Destiny starts rummaging through her room. 
        g "I don't mind cleaning up a bit. I'll just take care of these shards if that's allright."  
        d "Yes! Found it!" 
        d "Give me a second to throw this on."  
    #(blackspace). 
        g "{i}*chuckle*{/i}. No worries, I'll just go ahead and do it." 
        g "Besides, our bus leaves in 20 minutes."  
        d "I'll be quick!"  

        scene bg_d_bathroom
    #(Destiny in the mirror, dishevelled). 
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
        d_t "Shit! I have to hurry."  
        d "It's next to the counter. Be there in a second!"  

        scene bg_d_kitchen
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
        g "Oh come on, good work takes time."
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
        d_t "How obsessed with a movie do you have to be? \"Watch out! it's the Matrix trying to get you to wake up!\" As if."
        d_t "Is there seriously nothing useful on the internet about something like this?"
        d_t "A medical study on the side effects of Vr games or a rare phenomenon with lack of sleep would really calm my nerves right now."
        d_t "Maybe it's only a harmless little hallucination caused by exessive screen usage"
        d_t "But what if not?"
        d_t "Come on internet do me a solid won't you?"

#Maybe a section where you can click through "articles". 

        m "Sullivan!"

        scene bg_office_hallway
        d "What!?"  
        d_t "Oh shit. How did I not see him coming."   
        d "Y- Yes? Oh, g- good morning Matthew."  
        m "What website is that?"
        d "Huh?"
        m "I don't remember \"bumming around on forums for conspiracy theorists\" being in your job description."
        d_t "Crap" 
        d "Oh that? No, s-sorry I was just taking a quick break."
        m "Does this mean you've finally finished the Poster?"
        m "It'd better be. We can't have you hand in another Project late."
        m "Or last minute like last time. It's still a miracle to me how you somehow managed to get that one printed in time."
        m "Make sure you're ready beforehand this time. I'd highly suggest you print an example tomorrow for us to show to the clients."
        m "Oh, And Sullivan" 
        m "With tomorrow I don't mean 6:30PM. The office closes latest at 7:00. If it's not printed by then you have to figure out how to print it."
        m "Is that undersood?"
        d "Yes. Of course. I'll have it in time this time."
        m "Great! Now to other matters."
        m "I'd like to propose a promising business opportunity to you. And lord knows you need one of those."
        m "Two of them actually, now that I think about it."
        d_t "Ugh. What does he want now."
        m "Firstly, I'd like to introduce you to one of our team leaders Simon."
        d_t "Oh?"
        m "He's looking for someone to fill in as graphic designer for their current project."
        m "The woman that was previously in charge of the designs seems to have quit unexpectedly."
        m "Along with a couple of other names, Simon mentioned you as a possible replacement."
        m "Whatever his reasons might be."
        m "So What do you say Sullivan? I'd say the choice is obvious."
        m "I will send you the application forms later this afternoon if you decide to take this, how do I put it..."
        m "Rather rare opportunity."
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
                jump mattlunchn

            "Oh, sure...": 
                jump mattlunchy 
        
    label mattlunchy:
        m "Wonderfull. I heard today's menu would offer something special."
        "..."
        d "OH! You meant right now?"
        d "Yes! One second please. I need to. Uhm, finish some last tweeks and save my project really quickly."
        m "Alright. I'll just go ahead. Come meet me in the Cafeteria when you're done"
        jump mattlunch

    label mattlunchn:
        m "I'm not really asking Sullivan."
        m "I need to speak with you. Not only about this poster you seem so unexplainably stuck on."
        d "Sorry. Yes of course. Uhm, I need to finish some last tweeks and save my project. But after that I'll come right away."
        m "Fine. I'll just go ahead. Come meet me in the Cafeteria when you're done. Don't make me wait too long."
        jump mattlunch

    label mattlunch:

    label printer1:
        d_t "I can't believe it's this late already. This day has been a desaster."
        d_t "Let's just print this application and get it over with."


    # This ends the game.

    return
