import re
dictionary_names = ["sign","in","image","search","shopping","preferences","your","been","save","have","google","advanced","i'm","feeling","lucky","about","more","info","shower","mostly","cloudy","sunny","little","snow","thunderstorm","rain"]
dictionary_new = ["sine","ing","imege","seerch","shoeppeeng","prefferences","yuoor","beee","sefe","hefe-a","google-a","edfunced","ee'm","feeleeng","loocky","ebuoot","mure-a","inffu","showeryguben","moostlee","cloodee","soonee","leetl-a","snoo","doonderstoorm","reen"]

file = open("demofile.txt","r") # Replace demofile with your file
text = file.read()
file.close()

i = 0
for i in len(dictionary_names):
  text = re.sub(dictionary_names[i],dictionary_new[i],text)
  i = i + 1
  
file0 = open("demofile.txt","w") # Replace demofile with your file
file0.write(text)
file0.close()
