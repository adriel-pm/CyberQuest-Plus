# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MC", color="#3a54d4")
define g = Character("Genie", color="#8c3ad4")
define t = Character("Teach", color="#3ad44c")

# NOTE: the rest of the cast (Student, Boss, Caller) is defined in
# cq_characters.rpy, so this file stays small and easy to merge.


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "mc happy.png" to the images
    # directory.

    #show mc

    # These display lines of dialogue.
    # intro dialogue

    "Ahhh... Good morning, beautiful upstate New York!"

    "Tomorrow, I could graduate from CyberState University!"

    show mc at center

    mc "But, darn. I need to make sure I pass that CyberState Bar Exam! I can't afford to fail it!"

    mc "Today, I'll go over my notes on the essential laws of cybersecurity. "

    mc "Gee, I sure hope that I can pass…"

    hide mc

    scene bg classroom

    show t at left

    t "Students, welcome to our final day of class."

    t "I know I know, we've become well acquainted."

    t "Tears have been shared…"

    t "Together."

    t "But, today is my final review class."

    t "As we come to the end of our 10 years of education, I hope that you all go onto do beautiful things."

    show mc at right

    mc "I can hardly wait to get outta here!"

    mc "Let me just check my notes really quickly…"

    t "Alright, class. Quick history first, because every good hero knows the story of the villains."

    # ------------------------------------------------------------------
    # The story continues in cq_prologue.rpy (the whiteboard history
    # lesson picks up from Teach's line above).
    #
    # This replaced the template's "return", which ended the game here.
    # ------------------------------------------------------------------
    jump cq_prologue_part2
