import random
import time
from tkinter import Tk, Button, DISABLED

win = Tk()
win.title('Matchmaker')
win.resizable(width=False, height=False)
first = True
previous_x = 0
previous_y = 0
buttons = dict()
buttons_symbols = dict()
symbols = [
    u'\2702', u'\2705', u'\2708', u'\2709', u'\270A', u'\270B',
    u'\270C', u'\270F', u'\2712', u'\2714', u'\2716', u'\2728',
    u'\2702', u'\2705', u'\2708', u'\2709', u'\270A', u'\270B',
    u'\270C', u'\270F', u'\2712', u'\2714', u'\2716', u'\2728',
]

random.shuffle(symbols)

def show_symbol(x, y):
    global first
    global previous_x, previous_y
    buttons[x, y]['text'] = buttons_symbols[x, y]
    buttons[x, y].update_idletasks()

    if first:
        previous_x = x
        previous_y = y
        first = False
    elif previous_x != x or previous_y != y:
        if buttons[previous_x, previous_y]['text'] != buttons[x, y]['text']:
            time.sleep(0.5)
            buttons[previous_x, previous_y]['text'] = ' '
            buttons[x, y]['text'] = ' '
        else:
            buttons[previous_x, previous_y]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
        first = True


for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=3, height=4)
        button.grid(column=x, row=y)
        buttons[x, y] = button
        buttons_symbols[x, y] = symbols.pop()

win.mainloop()