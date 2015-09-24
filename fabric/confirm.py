from fabric.contrib.console import confirm as fab_confirm
from . import Colors

c = Colors.Colors();

def confirm(question, default=True):
        return fab_confirm(c.get(question), default)
