from fabric.api import *
from inviqa.fabric.puts import puts

class Environment:
    def __init__(self, www_dir):
        self.www_dir = www_dir
        self.hosts = {}
        self.host_dictionary = {}

    def boostrap(self):
        env.use_ssh_config = True
        env.colorize_errors = True

    def add_host(self, key, host):
        self.hosts[key] = host

    def map_host(self, key, value):
        self.host_dictionary[key] = value

    def get_host(self, key):
        return self.hosts[key]

    def set_host(self, key):
        env.hosts = [self.get_host(key)]

    def current_host(self):
        current_host = env.hosts[0]
        dict_key = [key for key, value in self.hosts.items() if value == current_host][0]
        return self.host_dictionary[dict_key]

    def www_home_dir(self):
        current_host = self.current_host()
        return self.www_dir % current_host

    def remote_task_notifier(self):
        puts('*** Running task on %s' % env.hosts[0])


class RemoteTaskNotifier:
    def __init__(self):
        self.notify()

    def notify(self):
        puts('*** Running task on %s' % env.hosts[0])
