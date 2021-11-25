# Bork, bork, bork!
A hilarious program that translates text in a file to Google's "bork bork bork' language.


## How to use

* Download the main.py file.
* Change the name of the file from ```demofile.txt``` to the file name you want.
* Run the program.

## How was this made?

This Easter egg can be viewed in Google. Go to Settings icon > Languages and select Bork, bork, bork!
The translation dictionary, visible at ```code/dictionary.py``` is a reference:

``` python
dictionary_names = ["sign","in","image","search","shopping","preferences","your","been","save","have","google"]
dictionary_new = ["sine","ing","imege","seerch","shoeppeeng","prefferences","yuoor","beee","sefe","hefe-a","google-a"]
```

It was coded this way:
``` python
for i in len(dictionary_names):
  text = re.sub(dictionary_names[i],dictionary_new[i],text)
  i = i + 1
  ```
