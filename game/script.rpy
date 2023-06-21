# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Destiny", color="#2ace9f")
define d_t = Character("Destiny", color="#2ace9f", what_italic=True)
define g = Character("Gabriel", color="#AED628")
define m = Character("Matt", color="#639af9")
define s = Character("Simon", color= "#ff6961")
define x = Character("?", color"#cdcdcd", what_italic=True )

# The game starts here.

label start:
    label Morning1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

        scene bg_black
        x "Destiny..."
        x "Destiny!"
        x "You have to listen to me."
        x "Something bad is going to happen if you don't listen to me"
        x "Please."
        x "You're in danger"
        x "I can help you."

        "Ping!"
        d_t "What was that?"
        d_t "*Ugh* What time is it even. Feels like I've only just fallen asleep."  
    # (phone appears(see Her reminder Project due tomorrow, Day and time: Sun 06:27). 
        d_t "Oh come on, already?"  

    # (back to blackspace for a little while) 
        d_t "Why can't it be like 4."
        d_t "Ugh does'nt matter. If I stay in bed now I'll be late."  
        
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

        d_t "Jeez I really have to clean this up soon."
        d_t "When did I even wear that shirt? God even my desk is filled."
        d_t "Actually, I don't think I've ever seen that screen of Achievements over there before."
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
        d_t "A display." 
        d_t "Really?" 
        d_t "Oh god. No more games before bed."
        d_t "What's next. Some NPC walks through my door? As if."
        d_t "This can't be serio-" 
        "*Knock knock*." 
        d "AH!" 
    #(cup falls and shatters and spills). 
    #(shattered mug). 
        g "Is everything alright in there?"   

        scene bg_d_corridor 
        g "I'm sorry. Did I startle you?"  
        d "No, no. It's fine! One second."  
        d_t "Oh god this shirt is ruined. That blouse will have to do."  
    #(Short black wipe). 
    #(opens door, Gabriel enters). 
        g "Are you sure you're alright?"  
        d "Oh, shut it. You almost scared me to death."   

        scene bg_d_kitchen
        d "Please just ignore the mess." 
        d "I'm working on it I promise."
        d "Oh and don't bother with the mug. I'll clean it up later too."  
        g "Oh no not the chipmunk mug." 
        g "I really liked that one. I think your mom gave you that right?"  
        d "Mhm. Must've been easter or something like that."  
        d_t "Shoot! What am I going to wear now?"  
    #Narrator: Destiny starts rummaging through her room. 
        g "I'll just take care of these shards if that's allright."  
        d "Yes! Found it!" 
        d "Give me a second to throw this on."  
    #(blackspace). 
        g "No worries, I'll do it." 
        g "Our bus leaves in 20 minutes though."  
        d "I'll be quick."  

        scene bg_d_bathroom
    #(Destiny in the mirror, dishevelled). 
        d_t "Let's see how this fits." 
    #(destiny smiles). 
        d_t "Jeez its worse than I thought."
        d_t "Better tidy this mess of a haircut up a bit."
        d_t "I have to find a brush."
        "!" 
        d_t "That screen seriously followed me here?"
        d_t "Stain... "
        d_t "Creepy."
        d_t "How the hell did It know that? That text was there before I even spilled my mug."
        d_t "Oh no I'm going insane."  
        d_t "I really should have slept longer. This can't just be me imagining things right?"
        d_t "But it's right, I don't think that's gonna come out."
        g "Destiny!"
        g "Where's the bin? I can't find it anywhere."  
        d_t "Shit! I have to hurry."  
        d "Be there in a second!"  

        scene bg_d_kitchen
        g "Ready to go?"  
        d "Yes! Sorry for the wait."  
        g "No worries."
        g "We've got enough time. Besides we've got a long enough day ahead of us."
        g "Do you think you'll get done with your design today?" 
        d_t "Oh right. I'm supposed to finish the design for that ad poser this week."  
        d "Hah.. we'll see."
        d "Something's just not right about it yet but I can't figure out what."
        d "And Matt just gave that preach at the last meeting about being stricter with deadlines from now on." 
        d "Im screwed."  
        g "Don't be too hard on yourself Destiny."
        g "You've always found a way to get things done till now."  
        d "Yeah like a day past the due date."  
        g "Oh come on, good work takes time."  
        d "You're right. Thank you."
        d "Now let's get going, before actually end up being late."  

    label Work1:
        scene bg_office_computer
        d_t "And another conspiracy theorist..."
        d_t "\"Watch out! it's the Matrix trying to get me to wake up!\" As if."
        d_t "Is there seriously nothing else to find about something like this?"
        d_t "Maybe it's only a hallucination caused by exessive screen usage"
        d_t "Come on internet do me a soolid won't you?"

#Maybe a section where you can click through "articles". 

        m "Sullivan!"

        scene bg_office_hallway
        d "What!?"  
        d_t "Oh shit. How did I not see him coming."   
        d "Y- Yes?"  
        m "What website is that?"
        m "I don't remember \"bumming around on forums for conspiracy theorists\" being in your job description."
        m "Does this mean you've finally finished the Poster?"
        d_t "Crap" 
        d "No, s-sorry I was just taking a quick break."
        d "It's almost done. I promise"   
        
    




    # This ends the game.

    return
