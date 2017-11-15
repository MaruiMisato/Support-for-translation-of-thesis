# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 17:52:33 2017

@author: kanri
"""
import pyperclip
import webbrowser
import time
text = pyperclip.paste()
print('text data:\n', text)

#Delete all newline characters
dst = text.replace('\n',' ')
dst = dst.replace('\r',' ')
dst = dst.replace("  ",' ')

#New line for each sentence
dst = dst.replace('.',".\n")
dst = dst.replace("\n ",'\n')
dst = dst.replace("ig.\n","ig.")#Fig. n
dst = dst.replace("i.\ne.\n","i.e.")#i.e.
dst = dst.replace("et al.\n","et al.")#et al.
#n.m
for n in "0123456789":
    for m in "0123456789":
        dst = dst.replace(n+".\n"+m,n+'.'+m)
        
pyperclip.copy(dst)
print('replaced text:\n', dst)

webbrowser.open("https://translate.google.co.jp/?hl=ja")
#time.sleep(1)
input()

#pip install pyperclip
#pip install pyautogui