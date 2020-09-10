import time

import pyautogui as gui

import random

import tkinter as tk


def Screenshot():
    name = random.randint(1, 9) * 420420
    name = 'F:/Python Udemy/Screenshot data/{}.png'.format(name)
    time.sleep(2)
    img = gui.screenshot(name)
    img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text='Screenshot',
    command=Screenshot)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text='Quit',
    command=quit)
close.pack(side=tk.LEFT)

root.mainloop()

Screenshot()
