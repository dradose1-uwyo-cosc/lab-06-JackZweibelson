# Jack Zweibelson
# UWYO COSC 1010
# Submission Date: 10/21/24
# Sources, people worked with, help given to: 
# your
# comments
# here

sentence = input("Say something and I will make it morse code: ")
morse = {'A' : ".- ", "N":"-. ",
'B': "-... ", "O": "--- ",
'C': "-.-. ", 'P': ".--. ",
'D': '-.. ', 'Q': '--.- ',
'E': ". ", 'R': '.-. ',
'F': "..-. ", 'S': '... ',
'G': '--. ', 'T': "- ",
'H': '.... ', "U": "..- ",
"I": ".. ", 'V': "...- ",
"J": ".--- ", "W":".-- ",
"K": "-.- ", "X": '-..- ',
"L": ".-.. ",'Y':"-.-- ", 
"M":" -- ", "Z": "--.. ",
" ": " "}

final = ""

for i in sentence.upper().strip():
    if i in morse:
        final += morse[i]
print(final)
