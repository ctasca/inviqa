from fabric import utils
from . import Colors

c = Colors.Colors()

def puts(text, show_prefix=None, end="\n", flush=False):
    return utils.puts(c.get(text), show_prefix, end, flush)

