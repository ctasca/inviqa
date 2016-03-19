from fabric.api import local
from inviqa.fabric.cli import puts
import re,os

class Runner:
    def __init__(self,path):
        self.path = path
        self.pwd = 'cd ' + self.path + ';'
    def status(self):
        local(self.pwd +  'vagrant status;')
    def up(self):
        local(self.pwd + 'vagrant up;')
    def ssh(self):
        local(self.pwd + 'vagrant ssh;')
    def suspend(self):
        local(self.pwd + 'vagrant suspend;')
    def resume(self):
        local(self.pwd + 'vagrant resume;')
    def destroy(self):
        local(self.pwd + 'vagrant destroy;')
