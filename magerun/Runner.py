from fabric.api import local
from inviqa.fabric.puts import puts
import re,os

class Runner:
    def __init__(self, path):
        self.path = path + os.sep
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
        local(self.path + "n98-magerun.phar sys:set:run")
    def list(self):
        local(self.path + "n98-magerun.phar list")
    def command(self, command):
        local(self.path + ("n98-magerun.phar %s" % command))
