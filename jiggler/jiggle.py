import mouse
import math
from screeninfo import get_monitors


def get_monitor_res():
    monitors = []
    for m in get_monitors():
        monitors.append(m)
    monitor_width = monitors[0].width
    monitor_height = monitors[0].height
    monitor_res = {"width": monitor_width, "height": monitor_height}
    return monitor_res

def jiggle(duration_seconds):
    r = 270
    monitor_res = get_monitor_res()
    monitor_center_x = monitor_res["width"]/2
    monitor_center_y = monitor_res["height"]/2
    mouse.move(monitor_center_x, monitor_center_y, absolute=True, duration=0)
    print(duration_seconds)
    for reps in range(int(duration_seconds)):
        for i in range(360):
            if (i%6 == 0):
                mouse.move(monitor_center_x+r*math.cos(math.radians(i)), monitor_center_y + r * math.sin(math.radians(i)), absolute=True, duration = 1/360)



