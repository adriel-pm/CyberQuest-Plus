## Player note book file to create the notebook page that players can use to view past 
# information that they've learned as the game progresses. 
default player_notes = []
default notebook_unlocked = False

# Automatically updates the informatmation list containing each note on the notebook page
init python: 
    def write_note(text):
        if text not in player_notes:
            if isinstance(text, list):
                for part in text:
                    write_note(part)
            else:
                player_notes.append(text)
    config.overlay_screens.append("notebook_button")

    


screen notebook_page():
    zorder 20
    modal True
    frame:
        xalign 0.5
        ypos 30
        xsize int(config.screen_width * 0.72)
        padding (50, 30)
        background "#fff8dc"
        vbox:
            spacing 10
            text "My Notes" size 40 bold True underline True color "#1d3557" xalign 0.5
            for note in player_notes:
                null height 10
                if isinstance(note, tuple):
                    for piece in note:
                        text piece size 23 bold True color "#111111"
                else:
                    text note size 23 bold True color "#111111"

        textbutton "X":
            xalign 1.0
            padding (20, 14)
            background "#ecd4d414"
            hover_background "#ffffff33"
            text_size 30
            text_color "#030202"
            text_hover_color "#ffd166" 
            action Hide("notebook_page")

            
## Player Notebook button only becomes visible after the player makes it to the school scene
screen notebook_button():
    zorder 100
    if notebook_unlocked:
        imagebutton:
            idle "/images/notebook_icon.png"
            padding (20, 14)
            hover_background "#ffffff33"
            action Show("notebook_page")
     
screen notebook_notify(message):
    zorder 110
    style_prefix "notify"
    frame at notebook_notify_fade:
        xalign 0.5
        text "[message!tq]"

    timer 3.0 action Hide("notebook_notify")


transform notebook_notify_fade:
    on show:
        alpha 0.0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
