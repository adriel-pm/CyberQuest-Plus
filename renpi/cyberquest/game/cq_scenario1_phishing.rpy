## =====================================================================
## cq_scenario1_phishing.rpy
## ---------------------------------------------------------------------
## SOURCE: CYBER_QUEST.pdf (the newer, more complete script).
## Covers: "FLASH FORWARD: 6 MONTHS LATER" -> phone call -> Mice'N'Boards
## -> CyberGenie's rules -> 3 minigames -> PikaKeyboard ending.
##
## The case follows CyberGenie's three rules from the script:
##   FIRST   Investigate the email     (MINIGAME 1: click the 3 clues,
##                                      then the CIA question)
##   SECOND  Go back in time and stop   (MINIGAME 2: pick the right
##           the attack                  evidence 3 times in a row)
##   FINALLY Teach prevention           (MINIGAME 3: explain all 4 risk
##                                      responses, in any order)
##
## Tags: # ART:  # AUDIO:  # WRITERS:  # DIRECTION:  (see cq_prologue.rpy)
## =====================================================================

default cq_clues_found = []      # which email clues were clicked
default cq_clue = None           # the clue clicked most recently
default cq_answered = False      # used to repeat a question until it's right
default cq_risk_explained = []   # which risk responses Prem has explained


label cq_scenario1_phishing:

    # -----------------------------------------------------------------
    # SCENE 1: Six months later, Prem's boring job
    # -----------------------------------------------------------------
    scene black with fade
    centered "FLASH FORWARD: 6 MONTHS LATER"

    # ART: bg mc_workplace
    # AUDIO: play music bgm_office fadein 1.0
    # AUDIO: play sound sfx_office   (Sounds of work and business)
    scene bg mc_workplace with fade

    show boss at right with dissolve
    boss "HEY! YOU, GET BACK TO WORK."
    hide boss with dissolve

    # WRITERS: "6 months later" vs "working here for 4 months" is not a
    # bug; Prem could have found the job 2 months after graduating. Confirm.
    mc "I've been working here for 4 months and NOTHING has happened."
    mc "I'm starting to think that CyberGenie was just some STRANGE dream."
    mc "Ugh, back to playing my LinkedIn game."

    # -----------------------------------------------------------------
    # SCENE 2: The phone call
    # DIRECTION: PHISHING: a fake IT security alert that tricks the
    #            employee into giving away their company login credential.
    # -----------------------------------------------------------------
    # AUDIO: play sound sfx_phone_ring
    "RIIING... RIIIIIIIIING" with hpunch

    mc "Woah, finally!"
    mc "A bite!"
    mc "Yellow?"
    caller "HELLOOOOOO? THANK THE STARS YOU ANSWERED, IT'S AN EMERGENCY!"
    mc "Calm down, calm down. What seems to be the problem?"
    caller "I CLICKED A COMPANY EMAIL AND NOW I AM COMPLETELY LOGGED OUT!"
    caller "WHAT DO I DO!??!??!?"
    mc "Alright, I'll be on my way! Where are you located?"

    # -----------------------------------------------------------------
    # SCENE 3: Mice'N'Boards, a computer hardware company
    # -----------------------------------------------------------------
    # ART: bg mnb_office, caller sprite
    scene bg mnb_office with fade
    show caller at left with dissolve

    caller "All I did was click this link..."
    caller "I swear I had no idea, I was so scared of losing my account!"

    # Show the phishing email (display only) while they talk.
    show screen cq_phishing_email() with dissolve

    mc "{i}rookie mistake...{/i}"
    caller "Pardon?"
    mc "Nothing... Let's get down to busine{nw}"

    # -----------------------------------------------------------------
    # TIME FREEZES: CyberGenie explains the rules
    # -----------------------------------------------------------------
    hide screen cq_phishing_email
    # AUDIO: play sound sfx_time_freeze
    show timefreeze_overlay zorder 50 with cq_flash
    show g at right zorder 60 with dissolve

    g "I HAVE AWOKEN!"
    mc "Woah... what in the world is going on here."
    g "I have returned once more to explain to you my powers!"
    mc "Um, go on..."

    # AUDIO: play music bgm_rules_jazz fadein 0.5   (RULES JAZZ MUSIC PLAYS)
    g "So... Ya wanna reach the good future?"
    g "Ya gotta follow some rules."
    g "Every time you meet with a client, they're gonna explain what went wrong."
    g "It's your job to prevent that."
    g "FIRST..."
    g "Take in your surroundings."
    g "You'll have to see what is going on using your provided tools."
    g "Click the screen and you'll be able to analyze each individual issue."
    g "SECOND..."
    g "Go back in time and stop the attack from happening."
    g "Tell the victim what is happening and what to look out for."
    g "FINALLY..."
    g "Teach the company how to prevent further attacks."
    mc "That... sounds like a lot..."
    g "These are all important steps for the future of your civilization!"
    g "Now go save the world!"

    # AUDIO: stop music fadeout 1.0
    hide g with dissolve

    # =================================================================
    # MINIGAME 1: INVESTIGATE THE EMAIL
    # DIRECTION: Time stays frozen. Prem sits down at the computer, takes a
    #            huge magnifying glass and looks at the email.
    # ART: optional close-up of Prem with the magnifying glass here.
    #
    # The loop repeats until all 3 clues have been clicked:
    #   1. call screen -> player clicks a clue -> _return = "sender"/"title"/"link"
    #   2. remember it in cq_clues_found
    #   3. keep the email visible and explain that clue
    # =================================================================
    $ cq_clues_found = []

    while len(cq_clues_found) < 3:
        call screen cq_phishing_email(interactive=True, found=cq_clues_found)
        $ cq_clue = _return
        # AUDIO: play sound sfx_click

        if cq_clue not in cq_clues_found:
            $ cq_clues_found.append(cq_clue)

        # Keep the email on screen (clicked clues now green) while explaining.
        show screen cq_phishing_email(interactive=False, found=cq_clues_found)

        if cq_clue == "sender":
            "Sender's email: You learn that the emails used for this company all use the domain \"@micenboards.com\", therefore you realize that the email is pretending to be inside the company..."
        elif cq_clue == "title":
            "Title: Using \"Urgent\" in the title is a way that phishers create fear in the victim, this furthers the idea that this is a scam..."
        elif cq_clue == "link":
            "Suspicious Link: The link used is a link that takes you to an unknown website, nobody in the company has ever seen it before..."

    hide screen cq_phishing_email with dissolve

    # -----------------------------------------------------------------
    # CIA QUESTION: repeats until the player picks Confidentiality.
    # A say line inside a `menu:` block is shown as the question.
    # -----------------------------------------------------------------
    show g at right zorder 60 with dissolve

    $ cq_answered = False
    while not cq_answered:
        menu:
            g "See the issues? Just to make sure, let me ask you a question... which part of the CIA does this affect the most?"

            "Confidentiality":
                # AUDIO: play sound sfx_correct
                mc "Confidentiality! It can leak information that shouldn't be accessed by everyone!"
                $ cq_answered = True

            "Integrity":
                # AUDIO: play sound sfx_wrong
                mc "Hmm... I don't think this is it, I believe this might let people view information who aren't supposed to see them..."

            "Availability":
                # AUDIO: play sound sfx_wrong
                mc "Hmm... I don't think this is it, I believe this might let people view information who aren't supposed to see them..."

    g "You have learned well... Let's go back to prevent this!"

    # =================================================================
    # MINIGAME 2: BACK IN TIME, STOP THE CLICK
    # DIRECTION: A flash of light; Prem is back BEFORE the caller clicked.
    # `scene` clears everything, including the time-freeze tint and the
    # Genie, so time is running normally again.
    # =================================================================
    # AUDIO: play sound sfx_time_warp
    # AUDIO: play music bgm_office fadein 1.0
    scene bg mnb_office with cq_flash
    show caller at left with dissolve

    # WRITERS: this was a stage direction; shown as narration so the
    # player understands the time jump. Delete if the visuals make it clear.
    "A flash of light appears, and you realize you have teleported back to before the caller clicked the link."

    mc "STOP!!! Do not click the link! There are several issues with this email!"

    # --- Round 1: correct answer = Title ---
    $ cq_answered = False
    while not cq_answered:
        menu:
            caller "But I don't want to get my account deleted! It says Urgent!!!"

            "Email":
                mc "Not quite, I remember the title of the email saying urgent..."
            "Title":
                mc "That's to scare you!!! If it was this important and urgent, there would have been prior emails about this problem."
                $ cq_answered = True
            "Link":
                mc "Not quite, I remember the title of the email saying urgent..."

    # --- Round 2: correct answer = Email (the sender) ---
    $ cq_answered = False
    while not cq_answered:
        menu:
            caller "Okay... but it says it was sent by support? Isn't that safe?"

            "Email":
                mc "The sender is not in your domain! You should always check the sender before opening anything."
                $ cq_answered = True
            "Title":
                mc "I remember something suspicious about the sender's email..."
            "Link":
                mc "I remember something suspicious about the sender's email..."

    # --- Round 3: correct answer = Link ---
    $ cq_answered = False
    while not cq_answered:
        menu:
            caller "I see, but why are you so worried? It is just an email."

            "Email":
                mc "The link seemed suspicious... I should talk about that."
            "Title":
                mc "The link seemed suspicious... I should talk about that."
            "Link":
                mc "Opening suspicious links could have very serious consequences, such as giving away log in credentials!"
                $ cq_answered = True

    caller "Wow, thank you so much! I could have been toast!"
    mc "No problem... Just part of the job."

    # DIRECTION: Prem starts to walk out the door, but CyberGenie appears in front of him.
    # AUDIO: play sound sfx_magic
    show g at right with cq_flash

    g "Not so fast kid! You have only postponed the issue, not fixed it!"
    mc "Really? What do I need to do?"
    g "You must tell him how to prevent this in the future..."
    mc "Makes sense, I need to help him!"

    hide g with dissolve

    # =================================================================
    # MINIGAME 3: TEACH PREVENTION (the 4 risk responses, any order)
    # `"Acceptance" if "accept" not in cq_risk_explained:` means the choice
    # only shows if it hasn't been picked yet, so the menu shrinks each
    # time until all 4 have been explained.
    # =================================================================
    # DIRECTION: Prem turns around.
    mc "Caller! Do you know how to deal with this in the future?"
    caller "Can this happen again?"
    mc "Why yes, it can, and there are four ways to help protect yourself."

    $ cq_risk_explained = []
    while len(cq_risk_explained) < 4:
        menu:
            # WRITERS: instruction line for the player; reword if you like.
            "(Pick a way to protect the company and explain it.)"

            "Acceptance" if "accept" not in cq_risk_explained:
                mc "Acceptance: By accepting that the scams will always happen, and being aware of them, you can continue letting external emails through, while saving money too."
                $ cq_risk_explained.append("accept")

            "Avoidance" if "avoid" not in cq_risk_explained:
                mc "Avoidance: Blocking all senders from outside your domain can stop any unwanted emails in, but also might stop other important emails too."
                $ cq_risk_explained.append("avoid")

            "Mitigate" if "mitigate" not in cq_risk_explained:
                mc "Mitigate: Getting two-factor authentication built into your company email helps stop people from accessing your account, even if they know your email and password."
                $ cq_risk_explained.append("mitigate")

            "Share" if "share" not in cq_risk_explained:
                mc "Share: Getting insurance to cover when your company has been breached is a great way to share the risk with another party."
                $ cq_risk_explained.append("share")

    caller "I see, thank you so much sir! I promise I will be cyber resilient in the future!"
    mc "No problem, it's all part of the job, the cybersecurity job!"

    # -----------------------------------------------------------------
    # ENDING
    # DIRECTION: Prem walks out of the door and into the sunset, realizing
    #            he has finished the job.
    # -----------------------------------------------------------------
    # ART: bg sunset
    # AUDIO: play music bgm_ending fadein 2.0
    scene bg sunset with dissolve
    pause 2.0

    # ART: bg mc_home
    scene bg mc_home with fade

    mc "Wow... That, was kind of crazy."
    mc "But I hope that I saved the world?"
    mc "Yeah, this HAD to have led to the end of the world."
    mc "No other reason for me to go back in ti{nw}"

    # DIRECTION: CYBERGENIE ARRIVES
    # AUDIO: play sound sfx_magic
    show g at right with cq_flash

    g "IT IS I."
    mc "Woooaaah?"
    g "Thank you so much for your help."
    g "If it wasn't for you, I would have never been able to have gotten my favourite keyboard of all time."
    # ART: optional CG of the "PikaKeyboard". Keep it an original
    #      design (no real-franchise characters on it).
    g "The PikaKeyboard."
    mc "You're telling me..."
    mc "That you sent me back in time..."
    mc "For a limited edition keyboard?"

    # DIRECTION: We hear a laugh track as the game ends.
    # AUDIO: play sound sfx_laugh_track
    pause 2.0

    # WRITERS: the script marks this ending as "proof of concept". When
    # Scenario 2 exists, replace `return` with:  jump cq_scenario2_xxx
    return
