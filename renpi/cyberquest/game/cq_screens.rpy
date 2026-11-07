## =====================================================================
## cq_screens.rpy
## ---------------------------------------------------------------------
## Our game-specific UI. These are ADDED ON TOP of Ren'Py's own
## screens.rpy (dialogue box, choice menus, save/load menus...).
## Do not put game UI inside screens.rpy; put it here.
##
## Two ways to use a screen in the story:
##   show screen NAME(...)  -> it stays visible while dialogue keeps going.
##                             Remove it with:  hide screen NAME
##   call screen NAME(...)  -> the story PAUSES until the player clicks a
##                             button that runs Return(value). That value
##                             is then available in the variable _return.
##
## All names start with "cq_" so they never clash with Ren'Py built-ins.
## Sizes assume the default 1920x1080 resolution.
## =====================================================================


## ---------------------------------------------------------------------
## WHITEBOARD: Teach writing on the board.
##   show screen cq_whiteboard("HEADING", ["line 1", "line 2"])
## ART: when a whiteboard image exists, change `background` to it,
##      e.g.  background "images/ui/whiteboard.png"
## ---------------------------------------------------------------------
screen cq_whiteboard(heading, lines=[], heading_color="#1b1b1b"):
    zorder 20
    frame:
        xalign 0.5
        ypos 40
        xsize int(config.screen_width * 0.70)
        padding (50, 35)
        background "#f7f7f2"
        vbox:
            spacing 14
            text heading size 56 bold True color heading_color xalign 0.5
            for line in lines:
                text line size 32 color "#222222"


## ---------------------------------------------------------------------
## NOTEBOOK: the CIA notes the player sees on screen during class.
## Text taken word for word from the script's "NOTEBOOK ON SCREEN".
## ART: swap background for a notebook-paper image later.
## ---------------------------------------------------------------------
define CQ_CIA_NOTES = [
    ("CONFIDENTIALITY", "Only the right people can see the data.",
        "Example: Your diary has a lock. Your little sibling is the threat.",
        "Tools: passwords, encryption, multi-factor authentication."),
    ("INTEGRITY", "Data stays accurate and unaltered.",
        "Example: Someone changes your grade from an A to an F. Rude AND an integrity attack.",
        "Tools: hashing, digital signatures, access controls."),
    ("AVAILABILITY", "Data and systems are there when you need them.",
        "Example: A website crashes during a huge sale. Customers cry.",
        "Tools: backups, redundancy, protection against DDoS attacks."),
]

screen cq_notebook_cia():
    zorder 20
    frame:
        xalign 0.5
        ypos 30
        xsize int(config.screen_width * 0.72)
        padding (50, 30)
        background "#fff8dc"
        vbox:
            spacing 6
            text "My Notes: The CIA Triad" size 40 bold True color "#1d3557" xalign 0.5
            for title, meaning, example, tools in CQ_CIA_NOTES:
                null height 10
                text (title + ": " + meaning) size 30 bold True color "#111111"
                text example size 26 color "#333333"
                text tools size 26 color "#333333"


## ---------------------------------------------------------------------
## MULTIPLE CHOICE: one question at a time. Reusable for any quiz.
##   call screen cq_multiple_choice("Title", "Question?", ["A", "B"], 1, 7)
##   -> _return is the INDEX of the clicked choice (0 = first choice).
## ---------------------------------------------------------------------
screen cq_multiple_choice(title, prompt, choices, number, total):
    modal True
    zorder 100

    # Darken everything behind the question.
    add Solid("#000000aa")

    frame:
        xalign 0.5
        yalign 0.5
        xsize int(config.screen_width * 0.62)
        padding (50, 40)
        background "#1b263b"
        vbox:
            spacing 20
            text (title + "  |  Question " + str(number) + " of " + str(total)) size 26 color "#a8dadc"
            text prompt size 36 color "#ffffff"
            null height 6
            for i, choice in enumerate(choices):
                textbutton ("ABCDEF"[i] + ")  " + choice):
                    xfill True
                    padding (20, 14)
                    background "#ffffff14"
                    hover_background "#ffffff33"
                    text_size 30
                    text_color "#ffffff"
                    text_hover_color "#ffd166"
                    action Return(i)


## ---------------------------------------------------------------------
## PHISHING EMAIL: recreation of the team's example email mockup.
##
##   show screen cq_phishing_email()
##       -> display only, while the caller and MC talk.
##   call screen cq_phishing_email(interactive=True, found=cq_clues_found)
##       -> investigation minigame. The sender, the title and the link
##          become clickable. Clicking one returns "sender", "title"
##          or "link". Clues already found turn green.
##
## ART: a magnifying-glass mouse cursor during the investigation would
##      fit the script ("takes a huge magnifying glass"). That is set
##      with config.mouse once a cursor image exists.
## ---------------------------------------------------------------------

# Helper: a piece of the email that is a clickable clue when
# interactive, and plain text otherwise. Used with `use` below.
screen cq_email_clue(caption, clue_id, interactive, found, font_size=22, is_bold=False, base_color="#ffffff", found_color="#7CFC00"):
    if interactive:
        textbutton caption:
            padding (6, 2)
            background None
            hover_background "#ffd16640"
            text_size font_size
            text_bold is_bold
            text_color (found_color if clue_id in found else base_color)
            text_hover_color "#ffd166"
            action Return(clue_id)
    else:
        text caption size font_size bold is_bold color (found_color if clue_id in found else base_color)


screen cq_phishing_email(interactive=False, found=[]):
    zorder 30
    frame:
        xalign 0.5
        ypos 25
        xsize int(config.screen_width * 0.60)
        padding (40, 26)
        background "#000000"
        vbox:
            spacing 8

            if interactive:
                text ("INVESTIGATE: click anything in this email that looks suspicious.     Clues found: " + str(len(found)) + "/3") size 22 color "#ffd166"
                null height 4

            # Inbox header
            hbox:
                spacing 16
                # ART: Mice"N"Boards app icon (keyboard + mouse), 56x56.
                add Solid("#e0e0e0", xysize=(56, 56))
                vbox:
                    yalign 0.5
                    text "Mice\"N\"Boards" size 28 bold True color "#ffffff"
                    text "Inbox · 1 new message" size 18 color "#9a9a9a"

            null height 6

            # CLUE: the title
            use cq_email_clue("URGENT: Your Mice\"N\"Boards Account Will Be Suspended!", "title", interactive, found, 30, True)

            # CLUE: the sender address
            hbox:
                spacing 6
                text "From: Mice\"N\"Boards IT Support  —" size 20 color "#bdbdbd" yalign 0.5
                use cq_email_clue("security@mice-n-boards-support.com", "sender", interactive, found, 20)
            text "To: Employee" size 20 color "#bdbdbd"

            null height 6
            text "Dear Mice\"N\"Boards Employee," size 22 color "#ffffff"
            text "Our security system has detected unusual activity on your company account." size 22 color "#ffffff"
            text "Your account will be suspended in 15 minutes unless you verify your identity immediately." size 22 bold True color "#ffffff"
            text "Click the link below to confirm your credentials and maintain access to company files." size 22 color "#ffffff"

            # CLUE: the link. (The mockup's "Suspicious link, do not click"
            # caption is left out on purpose: it would give the answer away.)
            frame:
                xfill True
                padding (16, 10)
                background "#f8d7da"
                use cq_email_clue("VERIFY YOUR ACCOUNT NOW", "link", interactive, found, 26, True, "#a4161a", "#1b5e20")

            text "Failure to verify your account may result in permanent suspension and loss of access to company resources." size 22 color "#ffffff"
            text "Regards," size 22 color "#ffffff"
            text "Mice\"N\"Boards IT Security Team" size 22 color "#ffffff"
