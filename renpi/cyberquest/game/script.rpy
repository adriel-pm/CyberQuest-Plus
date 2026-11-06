# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Prem", color="#3a54d4")
define g = Character("Genie", color="#8c3ad4")
define t = Character("Teach", color="#3ad44c")
define s1 = Character("chud1", color="#d43a3a")


# The game starts here.

#intro for the game, holds dialogue from Setup Day tab
label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black


    "Ahhh... Good morning, beautiful upstate New York!"
    "Tomorrow, I could graduate from CyberState University!"

    scene bg room

    show mc

    mc "But, darn. I need to make sure I pass that CyberState Bar Exam! I can't afford to fail it!"
    mc "Today, I'll go over my notes on the essential laws of cybersecurity. "
    mc "Gee, I sure hope that I can pass…"
    
    hide mc

    #[CLASSROOM. Teach stands at the whiteboard, holding a coffee mug that says "World's Okayest Professor."]

    scene bg classroom

    show t

    t "Students, welcome to our final day of class."
    "I know I know, we\'ve become well acquainted."
    "Tears have been shared…"
    "Together."
    "But, today is my final review class."
    "As we come to the end of our 10 years of education, I hope that you all go onto do beautiful things."

    show mc

    mc "I can hardly wait to get outta here!"
    "Let me just check my notes really quickly…"
    t "Alright, class. Quick history first, because every good hero knows the story of the villains."

    #[Whiteboard: a timeline with doodles.]

    scene bg whiteboard

    hide mc
    hide t
   
    "1971: A programmer makes \"Creeper,\" a program that hops between computers displaying: \"I'M THE CREEPER, CATCH ME IF YOU CAN!\" It was harmless, just rude."
    "1971 (same year!): Someone writes \"Reaper\" to chase it down. Congratulations, that's the world's first antivirus."
    "1988: The Morris Worm accidentally slows down a big chunk of the early internet. The creator only meant to measure its size. Moral: always test your code."
    "2000: The ILOVEYOU virus arrives in millions of inboxes. People opened it because, honestly, who doesn't want to be loved?"
    "Today: Attackers use AI, ransomware, and phishing. And YOU are the ones who have to stop them."

    show t

    t "The lesson: attackers have been creative for 50+ years. Defenders must be MORE creative. Now, onto the holy trinity of cybersecurity!"

    hide t

    #[Whiteboard flips. Giant letters: C. I. A.]

    scene bg flipped_whiteboard

    t "No, it's not that CIA. Nobody here is getting sunglasses and a black van. Yet."

    s1 "Is it related to the movies?"

    t "Only the ones where somebody types really fast and says \"I'm in.\""

    #[NOTEBOOK ON SCREEN. This is what the player sees:]

    scene bg notebook_C

    "CONFIDENTIALITY: Only the right people can see the data.
Example: Your diary has a lock. Your little sibling is the threat.
Tools: passwords, encryption, multi-factor authentication.
"

    scene bg notebook_I

    "INTEGRITY: Data stays accurate and unaltered.
Example: Someone changes your grade from an A to an F. Rude AND an integrity attack.
Tools: hashing, digital signatures, access controls.
"

    scene bg notebook_A
    "AVAILABILITY: Data and systems are there when you need them.
Example: A website crashes during a huge sale. Customers cry.
Tools: backups, redundancy, protection against DDoS attacks.
"

    #[Teach (explaining each one)]
    scene bg flipped_whiteboard

    show t

    t "For confidentiality, imagine your secret pizza topping preference. If everyone knows you like pineapple, that's a confidentiality breach. We protect secrets with encryption, strong passwords, and multi-factor authentication, which is basically a bouncer asking for ID AND a secret handshake."
    t "For integrity, if I tell you the test is at 9:00AM and someone secretly edits the message to say 9:00 PM, that's an integrity attack. You show up to an empty classroom, and the real test is already over. Moral of the story: trust but verify."
    t "For availability, a system that's secure but can't be used is like a vault that's locked forever. Very safe. Very useless. Attackers love knocking systems offline with DDoS attacks, which is basically ten thousand people trying to walk through one door at the same time."

    #[Teach writes: "C + I + A = a balancing act."]

    t "You can't max out all three at once. A system locked down so tight that nobody can use it fails Availability. Security is about balance."

    #[Whiteboard flips. The word RISK appears in giant red letters. Dramatic music sting.]
    scene bg flipped_whiteboard_risk

    t "And now, the finale. The word that keeps security professionals awake at night: RISK."

    s1 "Wait how did you flip the board to RISK? I thought it had a timeline on it?"

    t "I have my ways..."
    t "But focus on the board,"
    "Risk = Threat x Vulnerability x Impact."

    #[show board with the formula on it]
    scene bg flipped_whiteboard_risk_formula

    "Threat: Something that could cause harm. A hacker. A storm. Steve from accounting."
    "Vulnerability: A weakness. An unpatched system. A password that's \"password123.\" Steve's sticky note with all his passwords on his monitor."
    "Impact: How bad it hurts if it happens. Losing a cat video vs. losing a hospital's patient records."

    scene bg classroom

    show t

    t "So what do we do about risk? Four options, class. Memorize them:"
    "MITIGATE: Reduce it. (Install a lock.)"
    "TRANSFER: Share the burden. (Buy cyber insurance.)"
    "AVOID: Stop doing the risky thing. (Don't plug in mystery USB sticks from the parking lot.)"
    "ACCEPT: Live with it, knowingly. (The risk is small, and the fix costs more than the problem.)"

    t "Don't forget, no system is ever 100% secure. Your job isn't to eliminate risk. It's to MANAGE it wisely."

    hide t
    #[Notebook closes. Back to MC.]
    scene bg room

    show mc

    mc "Threat, vulnerability, impact... mitigate, transfer, avoid, accept... Confidentiality, Integrity, Availability... You know what, I feel like I'm ready for the big test tomorrow!"



    # This ends the game.

    return
