## =====================================================================
## cq_audio_and_effects.rpy
## ---------------------------------------------------------------------
## TRANSITIONS
##   Ren'Py already gives us: fade, dissolve, hpunch, vpunch, and more.
##   Below are the extra ones our script needs.
##
## AUDIO
##   Each line gives a short name to a file path. No audio files exist
##   yet, so every `play` line in the story files is COMMENTED OUT and
##   tagged "# AUDIO:". When the audio team delivers a file:
##     1. Save it at the path listed below (game/audio/...).
##     2. Search the project for its name (e.g. bgm_rules_jazz).
##     3. Delete the "# " in front of the matching play line.
##   Use .ogg files (Ren'Py also accepts .opus and .mp3).
## =====================================================================

# Bright white flash: CyberGenie appearing, time freezing, time travel.
define cq_flash = Fade(0.1, 0.0, 0.5, color="#ffffff")


## ---------------------------------------------------------------------
## MUSIC (loops)
## ---------------------------------------------------------------------
define audio.bgm_morning    = "audio/music/bgm_morning.ogg"     # Prem's bedroom
define audio.bgm_classroom  = "audio/music/bgm_classroom.ogg"   # Teach's review class
define audio.bgm_genie      = "audio/music/bgm_genie.ogg"       # CyberGenie / frozen time
define audio.bgm_office     = "audio/music/bgm_office.ogg"      # Prem's workplace, Mice'N'Boards
define audio.bgm_rules_jazz = "audio/music/bgm_rules_jazz.ogg"  # "RULES JAZZ MUSIC PLAYS"
define audio.bgm_ending     = "audio/music/bgm_ending.ogg"      # sunset / home

## ---------------------------------------------------------------------
## SOUND EFFECTS (play once)
## ---------------------------------------------------------------------
define audio.sfx_magic        = "audio/sfx/magic.ogg"           # "Sounds of magic"
define audio.sfx_time_freeze  = "audio/sfx/time_freeze.ogg"     # TIME FREEZES
define audio.sfx_time_warp    = "audio/sfx/time_warp.ogg"       # going back in time
define audio.sfx_board_flip   = "audio/sfx/board_flip.ogg"      # "Whiteboard flips"
define audio.sfx_dramatic     = "audio/sfx/dramatic_sting.ogg"  # "Dramatic music sting" (RISK)
define audio.sfx_crowd        = "audio/sfx/crowd_chatter.ogg"   # "Everyone is talking"
define audio.sfx_office       = "audio/sfx/office_ambience.ogg" # "Sounds of work and business"
define audio.sfx_phone_ring   = "audio/sfx/phone_ring.ogg"      # "RIIING RIIIIIIIIING"
define audio.sfx_click        = "audio/sfx/click.ogg"           # clicking email clues
define audio.sfx_correct      = "audio/sfx/correct.ogg"         # right answer
define audio.sfx_wrong        = "audio/sfx/wrong.ogg"           # wrong answer
define audio.sfx_laugh_track  = "audio/sfx/laugh_track.ogg"     # ending laugh track
