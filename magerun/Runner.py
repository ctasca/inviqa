from fabric.api import local, run, sudo
from inviqa.fabric.cli import puts
import re,os

class Runner:
    def __init__(self, path, rpath):
        self.path = path + os.sep
        self.rpath = rpath + os.sep
    def template_hints(self):
        local(self.path +  "n98-magerun.phar dev:template-hints")
    def clean_cache(self):
        local(self.path +  "n98-magerun.phar cache:clean")
        local(self.path +  "n98-magerun.phar cache:flush")
    def reindex_all(self):
        local(self.path + "n98-magerun.phar index:reindex:all")
    def admin_create(self):
        lcoal(self.path + "n98-magerun.phar admin:user:create")
    def setup_run(self):
        local(self.path + "n98-magerun.phar sys:setup:run")
    def list(self):
        local(self.path + "n98-magerun.phar list")
    def module_create(self, namespace, module, codepool):
        local((self.path + "n98-magerun.phar dev:module:create  %s %s %s") % (namespace, module, codepool))
    def command(self, command, use_run = False, use_sudo = False):
        if (use_run == True):
            run(self.rpath + ("n98-magerun.phar %s" % command))
        elif (use_sudo == True):
             sudo(self.rpath + ("n98-magerun.phar %s" % command))
        else:
            local(self.path + ("n98-magerun.phar %s" % command))
