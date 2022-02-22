# Copyright (c) 2021 AnAlgorithm

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# --- Init
import re
dictionary_names = ["sign","in","image","search","shopping","preferences","your","been","save","have","google","advanced","i'm","feeling","lucky","about","more","info","shower","mostly","cloudy","sunny","little","snow","thunderstorm","rain"]
dictionary_new = ["sine","ing","imege","seerch","shoeppeeng","prefferences","yuoor","beee","sefe","hefe-a","google-a","edfunced","ee'm","feeleeng","loocky","ebuoot","mure-a","inffu","showeryguben","moostlee","cloodee","soonee","leetl-a","snoo","doonderstoorm","reen"]

# --- Reading text
file = open("demofile.txt","r") # Replace demofile with your file
text = file.read()
file.close()

# --- Making changes to the text
i = 0
for i in len(dictionary_names):
  text = re.sub(dictionary_names[i],dictionary_new[i],text)
  i = i + 1
  
# --- Overwriting file text with new one
file0 = open("demofile.txt","w") # Replace demofile with your file
file0.write(text)
file0.close()
