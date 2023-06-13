import sys
sys.path.append("./jiggler/jiggle.py")
from jiggler import jiggle
from threading import Thread
import keyboard
import random
from time import sleep
import sys
import tkinter as tk
import os

time_unit = None
time_value = None
time = None

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def timerCalc(duration, unit = "s"):
    if (unit == "s"): return duration
    elif (unit == "h"): return duration * 3600
    elif (unit == "m"): return duration * 360
    elif (unit == "D"): return duration * 86400
    else: return None

running = False

def main():
    if __name__ == "__main__":
        uithread = Thread(target=uiGen)
        uithread.start()

def clicked (value_inside, entry, window):
    print (value_inside)
    print (entry)
    if (value_inside == None or entry == None):
        return
    global time_value
    global time_unit
    global time

    time_value = entry
    if (value_inside == "Hours"):
        time_unit = "h"
    if (value_inside == "Minutes"):
        time_unit = "m"
    if (value_inside == "Seconds"):
        time_unit = "s"
    if (value_inside == "Days"):
        time_unit == "D"

    time = timerCalc(time_value, time_unit) 

    thread = Thread(target=jigleMouse)
    thread1 = Thread(target=keyPress)
    thread.start()
    thread1.start()
    running = True
    window.destroy()
    keyboard.wait("spacebar")
    os._exit(1)
        

def uiGen ():
    time_options_list = ["Hours", "Minutes", "Seconds", "Days???"]

    window = tk.Tk()
    window.title("No Idle Bro")
    window.wm_iconbitmap(resource_path("icon.ico"))

    w = 500
    h = 200
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


    value_inside = tk.StringVar(window)
    value_inside.set("Unit")

    mainFrame = tk.Frame(master=window, padx=10, pady=10)

    frame = tk.Frame(master=mainFrame)
    frameInput = tk.Frame(master=mainFrame, borderwidth=5)
    instruction = tk.Label(text = "Input Duration", height=5, width=12, master=frame)
    entry = tk.Entry(fg="grey", bg="white", width=50, master=frameInput, borderwidth=3)
    unit_menu = tk.OptionMenu(frameInput, value_inside, *time_options_list)
    instruction_stop = tk.Label(text = "You can stop the thread by pressing the spacebar!", master = mainFrame, fg="red")

    button = tk.Button(
    text="Start",
    width=10,
    height=1,
    bg="white",
    fg="black",
    command=lambda: clicked(value_inside.get(), int(entry.get()), window),
    master=mainFrame
    )

    instruction.pack()
    entry.pack(side="left")
    unit_menu.pack(side="right")
    frame.pack()
    frameInput.pack()
    button.pack()
    instruction_stop.pack()
    mainFrame.pack()

    window.mainloop()
   
    

def keyPress():
    global time
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    for second in range(time):
        keyboard.press_and_release(keys[random.randint(0,10)])
        keyboard.press("backspace")
        sleep(1)
    os._exit(1)

def jigleMouse():
    global time
    if (time != None):
        jiggle.jiggle(time)


main()