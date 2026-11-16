## =====================================================================
## cq_prologue.rpy
## ---------------------------------------------------------------------
## CONTINUES script.rpy. That file ends with Teach saying:
##     "Alright, class. Quick history first..."
## and then jumps here, so this file starts at the whiteboard.
##
## Covers: history timeline -> CIA triad -> risk -> the CyberState Bar
## Exam -> CyberGenie's first appearance. Then jumps to Scenario 1.
##
## Characters (mc, g, t) are defined in script.rpy. Student and Boss are
## in cq_characters.rpy.
##
## Tags used in comments (find them with Cmd+Shift+F in VS Code):
##   # ART:        an image is shown here (placeholder for now)
##   # AUDIO:      music/sound goes here (line is commented out)
##   # WRITERS:    something the script team should fill in or confirm
##   # DIRECTION:  a stage direction from the script, kept for context
## =====================================================================


## ---------------------------------------------------------------------
## Whiteboard contents (kept up here so the scene below stays readable)
## ---------------------------------------------------------------------
define CQ_HISTORY_LINES = [
    "1971  -  \"Creeper\" hops between computers",
    "1971  -  \"Reaper\" chases it: the first antivirus",
    "1988  -  The Morris Worm slows the early internet",
    "2000  -  The ILOVEYOU virus",
    "Today -  AI, ransomware, and phishing",
]

define CQ_RISK_RESPONSE_LINES = [
    "RISK = THREAT x VULNERABILITY x IMPACT",
    "",
    "1. MITIGATE: Reduce it. (Install a lock.)",
    "2. TRANSFER: Share the burden. (Buy cyber insurance.)",
    "3. AVOID: Stop doing the risky thing.",
    "4. ACCEPT: Live with it, knowingly.",
]


## ---------------------------------------------------------------------
## Bar exam questions.
## WRITERS: the script only says "a multiple-choice test on CIA and
## other things", so these 7 are placeholders built ONLY from what Teach
## covers in class. Replace or reword freely.
## "answer" is the position of the correct choice, counting from 0.
## ---------------------------------------------------------------------
define CQ_BAR_EXAM_PASSING_SCORE = 5

define CQ_BAR_EXAM = [
    {
        "prompt": "A hacker reads a hospital's private patient records. Which part of the CIA triad was violated?",
        "choices": ["Confidentiality", "Integrity", "Availability"],
        "answer": 0,
    },
    {
        "prompt": "Someone secretly changes your grade from an A to an F. Which principle was attacked?",
        "choices": ["Confidentiality", "Integrity", "Availability"],
        "answer": 1,
    },
    {
        "prompt": "A store's website crashes during a huge sale because of a DDoS attack. Which principle was attacked?",
        "choices": ["Confidentiality", "Integrity", "Availability"],
        "answer": 2,
    },
    {
        "prompt": "Which equation did Teach write on the board?",
        "choices": [
            "RISK = THREAT + VULNERABILITY + IMPACT",
            "RISK = THREAT x VULNERABILITY x IMPACT",
            "RISK = IMPACT - THREAT",
            "RISK = VULNERABILITY / THREAT",
        ],
        "answer": 1,
    },
    {
        "prompt": "Steve from accounting keeps all his passwords on a sticky note on his monitor. In the risk equation, that sticky note is a...",
        "choices": ["Impact", "Threat", "Vulnerability"],
        "answer": 2,
    },
    {
        "prompt": "Your company buys cyber insurance. Which risk response is that?",
        "choices": ["Accept", "Avoid", "Transfer", "Mitigate"],
        "answer": 2,
    },
    {
        "prompt": "What was the name of the world's first antivirus program, written in 1971?",
        "choices": ["Reaper", "Creeper", "Morris", "ILOVEYOU"],
        "answer": 0,
    },
]

# `default` sets a variable's starting value for a new game, and Ren'Py
# saves and restores it automatically.
default cq_exam_score = 0
default cq_exam_total = 0
default cq_q_index = 0
default cq_q = None


## =====================================================================
## PROLOGUE, PART 2
## =====================================================================
label cq_prologue_part2:

    # Teach and MC are already on screen from script.rpy, and the
    # background is already "bg classroom", so this picks up mid-scene.

    # --- History timeline on the whiteboard ---
    # DIRECTION: Whiteboard shows a timeline with doodles.
    # ART: a real whiteboard image can replace the cq_whiteboard screen.
    show screen cq_whiteboard("A Brief History of Cyber Villains", CQ_HISTORY_LINES)

    t "1971: A programmer makes \"Creeper,\" a program that hops between computers displaying: \"I'M THE CREEPER, CATCH ME IF YOU CAN!\""
    t "It was harmless, just rude."
    t "1971, same year! Someone writes \"Reaper\" to chase it down. Congratulations, that's the world's first antivirus."
    t "1988: The Morris Worm accidentally slows down a big chunk of the early internet."
    t "The creator only meant to measure its size. Moral: always test your code."
    t "2000: The ILOVEYOU virus arrives in millions of inboxes."
    t "People opened it because, honestly, who doesn't want to be loved?"
    t "Today: Attackers use AI, ransomware, and phishing. And YOU are the ones who have to stop them."
    t "The lesson: attackers have been creative for 50+ years. Defenders must be MORE creative."
    t "Now, onto the holy trinity of cybersecurity!"

    # --- Whiteboard flips: C. I. A. ---
    # AUDIO: play sound sfx_board_flip
    show screen cq_whiteboard("C.   I.   A.")

    t "No, it's not that CIA. Nobody here is getting sunglasses and a black van. Yet."

    # DIRECTION: A student raises a hand.
    # MC is at right, so the student stands further left.
    show student at Position(xalign=0.72) with dissolve
    student "Is it related to the movies?"
    t "Only the ones where somebody types really fast and says \"I'm in.\""
    hide student with dissolve
    hide screen cq_whiteboard

    # --- NOTEBOOK ON SCREEN ---
    # `window hide` + `pause` hides the dialogue box so the player can
    # read the notes, then one click continues.
    show screen cq_notebook_cia with dissolve
    window hide
    pause
    window show

    t "Confidentiality: Imagine your secret pizza topping preference."
    t "If everyone knows you like pineapple, that's a confidentiality breach."
    t "We protect secrets with encryption, strong passwords, and multi-factor authentication..."
    t "...which is basically a bouncer asking for ID AND a secret handshake."

    t "Integrity: If I tell you the test is at 9:00 AM and someone secretly edits the message to say 9:00 PM, that's an integrity attack."
    t "You show up to an empty classroom, and the real test is already over. Moral of the story: trust but verify."

    t "Availability: If a system is secure but nobody can use it, it's like a vault that's locked forever. Very safe. Very useless."
    t "Attackers love knocking systems offline with DDoS attacks, which is basically ten thousand people trying to walk through one door at the same time."

    hide screen cq_notebook_cia with dissolve

    $ write_note(CQ_CIA_NOTES)
    show screen notebook_notify("Notes updated")

    # DIRECTION: Teach writes "C + I + A = a balancing act."
    show screen cq_whiteboard("C + I + A = a balancing act.")

    t "You can't max out all three at once."
    t "A system locked down so tight that nobody can use it fails Availability. Security is about balance."

    # --- Whiteboard flips: RISK in giant red letters ---
    # AUDIO: play sound sfx_dramatic   (DIRECTION: Dramatic music sting)
    show screen cq_whiteboard("RISK", ["RISK = THREAT x VULNERABILITY x IMPACT"], heading_color="#c1121f")

    t "And now, the finale. The word that keeps security professionals awake at night: RISK."
    t "Threat: Something that could cause harm. A hacker. A storm. Steve from accounting."
    t "Vulnerability: A weakness. An unpatched system. A password that's \"password123.\" Steve's sticky note with all his passwords on his monitor."
    t "Impact: How bad it hurts if it happens. Losing a cat video vs. losing a hospital's patient records."
    t "So what do we do about risk? Four options, class. Memorize them:"

    show screen cq_whiteboard("RISK", CQ_RISK_RESPONSE_LINES, heading_color="#c1121f")

    t "1. MITIGATE: Reduce it. Install a lock."
    t "2. TRANSFER: Share the burden. Buy cyber insurance."
    t "3. AVOID: Stop doing the risky thing. Don't plug in mystery USB sticks from the parking lot."
    t "4. ACCEPT: Live with it, knowingly. The risk is small, and the fix costs more than the problem."
    t "No system is ever 100\% secure. Your job isn't to eliminate risk. It's to MANAGE it wisely."

    hide screen cq_whiteboard

    $ write_note(CQ_RISK_RESPONSE_LINES)
    show screen notebook_notify("Notes updated")

    # DIRECTION: Notebook closes. Back to MC.
    # ART: bg mc_bedroom
    scene bg mc_bedroom with dissolve
    show mc at center with dissolve

    mc "Threat, vulnerability, impact... mitigate, transfer, avoid, accept... Confidentiality, Integrity, Availability..."
    mc "You know what, I feel like I'm ready for the big test tomorrow!"

    # -----------------------------------------------------------------
    # EXAM DAY
    # -----------------------------------------------------------------
    scene black with fade
    centered "The next day..."

    # ART: bg classroom reused for exam day (a separate "bg exam_room"
    #      is optional if art wants one).
    # AUDIO: play sound sfx_crowd   (DIRECTION: Everyone is talking)
    play sound sfx_crowd 

    scene bg classroom with fade
    show t at left with dissolve

    t "Settle down, settle down!"
    t "I know every student has worked their butts off to make it big in the world."
    t "And today will be proof of that work."
    t "Those who pass this test will be able to do great things in this world."
    t "I expected big things from each and every one of you."
    t "Specifically, from whoever passes the test, of course!"
    t "Now, begin!"

    play music bgm_stress fadeout 1.0 fadein 1.0 # CyberQ1 starts

    # The story only continues once the player passes.
    call cq_bar_exam

    stop music fadeout 1.0 # CyberQ1 ends

    # {nw} means "no wait": the line shows and the game moves on by
    # itself, so the Genie literally interrupts MC mid-word.
    mc "Yes! I did it! I actually passed. I can't beli{nw}"

    # -----------------------------------------------------------------
    # CYBERGENIE APPEARS, TIME IS FROZEN
    # -----------------------------------------------------------------
    play sound sfx_magic volume 0.35     #(DIRECTION: Sounds of magic)
    # AUDIO: play music bgm_genie fadein 1.0

    play music bgm_genie fadeout 1.0 fadein 1.0

    # zorder decides stacking: the blue tint (50) covers the classroom
    # and Teach, and the Genie (60) draws on top of the tint.
    show timefreeze_overlay zorder 50 with cq_flash
    show g at right zorder 60 with dissolve
    

    mc "W-w-w-w...."
    mc "WHAT?"
    mc "Who are you?"
    g "I am CyberGenie, keeper of time and protector of cybersecurity."
    g "I see you have passed the bar exam."
    g "Things... are going in order..."
    mc "What do you mean?"
    g "This is exactly as the prophecy foretold."
    mc "What?"
    g "You have the power to save us from the dark timeline..."
    mc "But, how?"
    g "A serious event shall unfold in your lifetime."
    g "Your phone will ring, it will be a concerned citizen."
    g "You, with your set of skills, will learn of their issues."
    g "You shall study what went wrong."
    g "And make it right."
    mc "But..."
    mc "How?"
    g "That, is for you to learn..."
    mc "No, please explain!"
    g "I have overstayed my welcome!"
    g "I must go now."

    # DIRECTION: He vanishes.
    # AUDIO: stop music fadeout 1.0

    stop music fadeout 1.0

    hide g with cq_flash
    hide timefreeze_overlay with dissolve

    mc "Woah, what just happened?"
    mc "Anyways! Time to go on with my day..."
    mc "I guess..."

    jump cq_scenario1_phishing


## =====================================================================
## THE CYBERSTATE BAR EXAM
## Reached with `call cq_bar_exam`, so `return` comes back to the line
## right after that call. Asks every question in CQ_BAR_EXAM, then
## either returns (passed) or restarts the exam (failed).
## =====================================================================
label cq_bar_exam:
    $ cq_exam_score = 0
    $ cq_q_index = 0
    $ cq_exam_total = len(CQ_BAR_EXAM)

    window hide
    while cq_q_index < cq_exam_total:
        $ cq_q = CQ_BAR_EXAM[cq_q_index]
        call screen cq_multiple_choice("CyberState Bar Exam", cq_q["prompt"], cq_q["choices"], cq_q_index + 1, cq_exam_total)
        if _return == cq_q["answer"]:
            $ cq_exam_score += 1
        $ cq_q_index += 1
    window show

    if cq_exam_score < CQ_BAR_EXAM_PASSING_SCORE:
        # WRITERS: the script has no "you failed" scene. Placeholder lines:
        "You scored [cq_exam_score] out of [cq_exam_total]. You need at least [CQ_BAR_EXAM_PASSING_SCORE] to pass."
        "Take a deep breath, and try the exam again."
        jump cq_bar_exam

    "You scored [cq_exam_score] out of [cq_exam_total]!"
    return
