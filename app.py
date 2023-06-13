import sys
sys.path.append("./jiggler/jiggle.py")
from jiggler import jiggle
from threading import Thread
import keyboard
import random
from time import sleep
import sys
from tkinter import ttk
import os
import sv_ttk
import tkinter
import ctypes as ct
import platform

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
        
def dark_title_bar(window):
    if "window" not in platform.platform().lower(): return
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
    ct.windll.shcore.SetProcessDpiAwareness(True)

def uiGen ():
    time_options_list = ["Hours", "Minutes", "Seconds", "Days???"]

    window = tkinter.Tk()
    window.title("No Idle Bro")
    window.wm_iconbitmap(resource_path("icon.ico"))
    window.resizable(False, False)
    dark_title_bar(window=window)

    w = 550
    h = 220
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


    value_inside = tkinter.StringVar(window)
    value_inside.set("Unit")

    mainFrame = ttk.Frame(master=window, padding=10)

    frame = ttk.Frame(master=mainFrame, padding=20)
    frameInput = ttk.Frame(master=mainFrame, borderwidth=5)
    instruction = ttk.Label(text = "Input Duration", master=frame, font=('Arial', 20))
    entry = ttk.Entry(width=60, master=frameInput)
    unit_menu = ttk.OptionMenu(frameInput, value_inside, "Unit  ", *time_options_list)
   
    instruction_stop = ttk.Label(text = "You can stop the thread by pressing the spacebar!", master = mainFrame, foreground='red', font=('Arial', 12))

    button = ttk.Button(
    text="Start",
    width=15,
    command=lambda: clicked(value_inside.get(), int(entry.get()), window),
    master=mainFrame,
    )

    instruction.pack()
    entry.pack(side="left", padx=5)
    unit_menu.pack(side="right")
    frame.pack()
    frameInput.pack()
    button.pack(pady=5)
    instruction_stop.pack()
    mainFrame.pack()

    sv_ttk.set_theme("dark")


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