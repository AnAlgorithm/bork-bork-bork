# --- Init
import re
dictionary = { "sign" : "sine" ,
              "in" : "ing" ,
              "image" : "imege" ,
              "search" : "seerch" ,
              "shopping" : "shoeppeeng" ,
              "preferences" : "prefferences" ,
              "your" : "yuoor" ,
              "been" : "beee" ,
              "save" : "sefed" ,
              "have" : "hefe-a" ,
              "google" : "google-a" }

# ---
# --- Reading text
file = open("demofile.txt","rt")
text = file.read()
file.close()

# ---
# --- Making changes to the text

