# -*- coding: utf-8 -*-
import pyperclip
import webbrowser
import re

txt = pyperclip.paste()
print('txt data:\n', txt)

txt= txt.replace('\n',' ')#Delete all newline characters
txt = txt.replace('\r','')

txt = txt.replace('. ',".\n")#New line for each sentence

txt = txt.replace("Fig.\n","Fig.")#Fig. n
txt = txt.replace("i.\ne.\n","i.e.")#i.e.
txt = txt.replace("et al.\n","et al.")#et al.

re.sub("(\d)\.\n(\d)","$1.$2",txt)#n.m

pyperclip.copy(txt)
print('replaced txt:\n',txt)

webbrowser.open("https://translate.google.co.jp/?hl=ja")
input()

#pip install pyperclip
#pip install pyautogui