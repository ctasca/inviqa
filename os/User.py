import os, pwd

class User:
    def __init__(self):
        pass
    def name(self):
        return pwd.getpwuid( os.getuid() )[ 0 ]
