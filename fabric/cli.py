from fabric.contrib.console import confirm as fab_confirm
from fabric.api import prompt as fab_prompt
from fabric import utils
from . import Colors

c = Colors.Colors();

def confirm(question, default=True):
    return fab_confirm(c.get(question), default)

def prompt(text, key=None, default='', validate=None):
    return fab_prompt(c.get(text), key, default, validate)

def puts(text, show_prefix=None, end="\n", flush=False):
    return utils.puts(c.get(text), show_prefix, end, flush)
