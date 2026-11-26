## =====================================================================
## cq_characters.rpy
## ---------------------------------------------------------------------
## The main three characters are already defined at the top of
## script.rpy, so they are NOT repeated here:
##
##     mc  -> "MC"    (blue)
##     g   -> "Genie"   (purple)
##     t   -> "Teach"   (green)
##
## Defining the same name in two files is not an error, but whichever
## file loads last silently wins, which makes colors and names very
## confusing to debug. One definition per character, one place.
##
## This file adds the rest of the cast the script needs.
## =====================================================================

# The student who raises a hand during Teach's CIA lesson.
define student = Character("Student", color="#b8b8b8")

# MC's boss at the office job, 6 months after graduation.
define boss = Character("Boss", color="#e63946")

# WRITERS: the Mice'N'Boards employee who calls for help in Scenario 1.
# The script never names them. If they get a real name, change it here
# and every line of their dialogue updates automatically.
define caller = Character("Caller", color="#90be6d")
