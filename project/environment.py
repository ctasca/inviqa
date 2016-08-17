import os
from fabric.api import *
from inviqa.fabric.cli import puts
from inviqa.fabric.Colors import Colors

c = Colors()

class Servers:
    def __init__(self, local_dir, www_dir, www_public):
        self.local_dir = local_dir
        self.www_dir = www_dir
        self.www_public = www_public
        self.hosts = {}
        self.host_dictionary = {}
        self.default_vcl_dir = "/etc/varnish"

    def boostrap(self):
        env.use_ssh_config = True
        env.colorize_errors = True

    def add_host(self, key, host):
        self.hosts[key] = host

    def map_host(self, key, value):
        self.host_dictionary[key] = value

    def get_host(self, key):
        return self.hosts[key]

    def local_project_dir(self):
        return self.local_dir

    def set_host(self, key):
        env.hosts = [self.get_host(key)]

    def current_host(self):
        current_host = env.hosts[0]
        dict_key = [key for key, value in self.hosts.items() if value == current_host][0]
        return self.host_dictionary[dict_key]

    def www_home_dir(self):
        current_host = self.current_host()
        return self.www_dir % current_host

    def www_public_dir(self):
        current_host = self.current_host()
        return self.www_public % current_host

    def varnish_default_vcl_dir(self):
        return self.default_vcl_dir

    def remote_task_notifier(self):
        puts('*** Running task on %s' % env.hosts[0])


class RemoteTaskNotifier:
    def __init__(self, environment):
        self.notify(environment)

    def notify(self, environment):
        puts('!! Running task on %s.\nCurrent Working directory: %s' % (env.hosts[0], environment.www_home_dir()))

class DirectoryChooser:
    def __init__(self, cwd, environment):
        self.cwd = cwd
        self.env = environment
        self.dirlist = []
        self.selected = False

    def choose(self):
        pass
