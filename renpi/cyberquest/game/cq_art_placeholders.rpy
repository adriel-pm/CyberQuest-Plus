## =====================================================================
## cq_art_placeholders.rpy
## ---------------------------------------------------------------------
## No art exists yet (there is no game/images/ folder), so every image
## the story uses is defined here as a labeled colored box. The game
## runs right now with zero image files.
##
## WHY THIS FILE EXISTS: without it, Ren'Py shows its own grey
## "placeholder" box for any unknown image, which is why script.rpy
## currently works. Those grey boxes all look identical and disappear
## entirely when the game is built for release. These labeled boxes say
## exactly which art is missing and in what scene.
##
## HOW TO SWAP IN REAL ART:
##   Ren'Py turns files in game/images/ into images named after the
##   file, so  game/images/bg classroom.png  becomes the image
##   "bg classroom" (the space in the filename is part of the name).
##   1. Create the folder game/images/ if it does not exist yet.
##   2. Drop the file in, named to match the list below.
##   3. DELETE that image's line in this file.
##   Nothing in the story files has to change.
##
## The names below match what script.rpy already uses: the sprites are
## "mc", "t" and "g" (not "MC"/"teach"/"genie"), so the existing
## `show mc` and `show t` lines keep working untouched.
## =====================================================================

init -1 python:

    def cq_bg_placeholder(label, color="#2b2d42"):
        """A full-screen colored rectangle with a label in the middle."""
        return Fixed(
            Solid(color),
            Text(label, size=44, color="#ffffff", xalign=0.5, yalign=0.4, text_align=0.5),
            xysize=(config.screen_width, config.screen_height),
        )

    def cq_sprite_placeholder(label, color="#457b9d"):
        """A tall rectangle roughly the size of a standing character."""
        return Fixed(
            Solid(color),
            Text(label, size=32, color="#ffffff", xalign=0.5, yalign=0.5, text_align=0.5),
            xysize=(420, 820),
        )


## ---------------------------------------------------------------------
## BACKGROUNDS  (final art: 1920x1080, matching gui.init in gui.rpy)
## ---------------------------------------------------------------------

# Used by script.rpy's opening line. A plain black screen is a fine
# final look, so this one may never need real art.
image bg black = Solid("#000000")

image bg classroom    = "/images/classbg.png" 
image bg mc_bedroom   = "/images/roombg.png" 
image bg mc_workplace = "/images/officebg.jpg" 
image bg mnb_office   = "/images/clientofficebg.jpg"
image bg sunset       = "/images/trainbg.png"
image bg mc_home      = "/images/mc_night_home.jpg"

## ---------------------------------------------------------------------
## CHARACTER SPRITES  (final art: transparent PNG, roughly 600x1000)
##
## Expressions can be added later as separate files, e.g.
## "t happy.png" and "t annoyed.png", then written as:  show t happy
## ---------------------------------------------------------------------
image mc      = "/images/mcshadow.png" 
image t       = "/images/teachershadow.png" 
image g       = "/images/clipster.png" 
image student = "/images/studentsshadow.png"
image boss    = "/images/bossshadow.png"
image caller  = "/images/clientshadow.png"


## ---------------------------------------------------------------------
## EFFECTS
## ---------------------------------------------------------------------
# A see-through blue tint laid over the scene while TIME IS FROZEN.
# Anything shown with a higher zorder (the Genie) draws above it, so the
# world looks frozen and the Genie does not.
# ART/VFX: can later be replaced with a nicer frozen-time effect image.
image timefreeze_overlay = Solid("#1d3557aa")
