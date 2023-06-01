# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Destiny", color="#30D5C8")
define d_t = Character("Destiny", color="#30D5C8", what_italic=True)
define g = Character("Gabriel", color="#AED628")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    "PING"
    scene bg_d_window
    d_t "What was that?"
    d_t "Ugh. What time is it even. Feels like I’ve only just fallen asleep."
    scene bg_phone
    d_t "Oh come on It’s my day off."
    d_t "Screw this. I can’t fall asleep again anyways."
    d_t "Coffee!"
    scene bg_d_kitchen
    d_t "Oh! right" 
    d_t "that message." 
    d_t "Wait. But I don’t even have any other messages." 
    d_t "What was that? Maybe something outside?"
    d_t "Jeez I really have to clean this up soon." 
    d_t "Where did those papers even come from?"
    d_t "Or that bottle. Actually, I don’t think I've ever seen that screen of Achievements before."
    d_t "WAIT. ACHEIVMENTS!? "
    d_t "what in the-"
    show Achievement
    d "Heh. Heh he..."
    d_t "Really?"
    d_t " Oh god. No more games before bed." 
    d_t " What’s next. Some NPC walks through my door? As if. "
    d_t "This can’t be serio-"
    d "AH!"
    g "Is everything alright in there?"
    scene bg_d_corridor
    g " I’m sorry. Am I too early?"
    d "No, no. All good. One second"
    d_t "Oh god this shirt is ruined. YES. That sweater will have to do"
    show concern
    g "Are you sure you’re alright?"
    d "Oh shut it."
    show smile
    d "You almost scared me to death"




    # This ends the game.

    return
