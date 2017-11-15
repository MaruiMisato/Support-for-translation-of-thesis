# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:52:33 2017

@author: kanri
"""
import pyperclip
import webbrowser
txt = pyperclip.paste()
print('text data:\n', txt)

#Delete all newline characters
txt= txt.replace('\n',' ')
txt = txt.replace('\r','')

#New line for each sentence
txt = txt.replace('.',".\n")
txt = txt.replace("\n ",'\n')
txt = txt.replace("ig.\n","ig.")#Fig. n
txt = txt.replace("i.\ne.\n","i.e.")#i.e.
txt = txt.replace("et al.\n","et al.")#et al.
#n.m
for n in "0123456789":
    for m in "0123456789":
        txt = txt.replace(n+".\n"+m,n+'.'+m)
        
pyperclip.copy(txt)
print('replaced text:\n',txt)

webbrowser.open("https://translate.google.co.jp/?hl=ja")
input()

#pip install pyperclip
#pip install pyautogui