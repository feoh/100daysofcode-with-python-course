# Adds a bracketed datetime stamp to whatever's in your clipboard.

import pyperclip
import datetime

unstamped = pyperclip.paste()
stamped = f"[{datetime.datetime.now()}] {unstamped}"
pyperclip.copy(stamped)
