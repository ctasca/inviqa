from fabric.api import prompt as fab_prompt
from . import Colors

c = Colors.Colors()

def prompt(text, key=None, default='', validate=None):
    return fab_prompt(c.get(text), key, default, validate)
