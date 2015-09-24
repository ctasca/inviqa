from fabric.colors import *
import re

class Colors:
        def __init__(self):
            pass
        def get(self, text):
            if re.match(r'^\>\>\>', text):
                return cyan(text)
            if re.match(r'^\*\*\*', text):
                return yellow(text)
            if re.match(r'^\[\d{1,}\]', text):
                return yellow(text)
            if re.match(r'^\!\!\!', text):
                return red(text)
            if re.match(r'^\.:\~', text):
                return green(text)
