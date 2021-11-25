# --- Init
import re
dictionary_names = ["sign","in","image","search","shopping","preferences","your","been","save","have","google","advanced"]
dictionary_new = ["sine","ing","imege","seerch","shoeppeeng","prefferences","yuoor","beee","sefe","hefe-a","google-a","edfenced"]

# ---
# --- Reading text
file = open("demofile.txt","rt") # Replace demofile with your file
text = file.read()
file.close()

# ---
# --- Making changes to the text
i = 0
for i in len(dictionary_names):
  text = re.sub(dictionary_names[i],dictionary_new[i],text)
  i = i + 1
  
# ---
# --- Overwriting file text with new one
file0 = open("demofile.txt","wt") # Replace demofile with your file
file0.write(text)
file0.close()

# ---
