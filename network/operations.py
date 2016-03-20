from fabric.operations import local
from fabric.api import *
from inviqa.project.environment import *
from inviqa.fabric.Colors import Colors
from inviqa.fabric.cli import confirm as inviqa_confirm
from inviqa.fabric.cli import prompt, puts


class Frontdoor2:
    def __init__(self, user):
        self.user = user

    def connect(self):
        local('ssh -D 8889 -C -N %s@frontdoor2.inviqa.com -p 22' % self.user)

class RemoteShredder:
    def __init__(self, environment):
        self.env = environment

    def shred(self):
        RemoteTaskNotifier(self.environment)
        remotefile_location = prompt('>>> Enter file location:')
        with cd(remotefile_location):
            run('ls')
            filename = prompt('>>> Enter file name to shred:')
            confirm_shred = inviqa_confirm("*** You are about to start shredding the file '%s'. Are you sure?" % (filename), False)
            if confirm_shred:
                sudo('shred -u -v %s' % (filename))
                fdisk = inviqa_confirm("*** Do you want to overwrite the free disk space?", False)
                if fdisk:
                    with cd('~'):
                        sudo('dd if=/dev/zero of=file.txt')
                        frm = inviqa_confirm("*** Do you want to delete file.txt?", False)
                        if frm:
                            sudo('rm file.txt')

class ProxyReverse:
    def __init__(self):
        pass

    def reverse(self):
        proxy = prompt('>>> Enter host (without http|https)')
        local('proxyreverse 8080,8443 %s' % (proxy))

class Downloader:
    def __init__(self, remote_path, local_path):
        self.remote_path = remote_path
        self.remote_cd_path = remote_path
        self.local_path = local_path

        remote_path_segments = self.remote_cd_path.split(os.sep)
        last = remote_path_segments.pop()

        if "." in last:
            self.remote_cd_path = os.sep.join(remote_path_segments)

    def download(self):
        puts('*** Downloading from %s' % (self.remote_path))
        puts('*** To %s' % (self.local_path))
        download = inviqa_confirm('>>> Continue?')
        with cd(self.remote_cd_path):
            if download:
                get(self.remote_path, self.local_path)


class Uploader:
    def __init__(self, local_path, remote_path):
        self.remote_cd_path = remote_path
        self.local_path = local_path
        self.remote_path = remote_path

        remote_path_segments = self.remote_cd_path.split(os.sep)
        last = remote_path_segments.pop()

        if "." in last:
            self.remote_cd_path = os.sep.join(remote_path_segments)

    def upload(self):
        puts('*** Uploading %s' % (self.local_path))
        puts('*** To %s' % (self.remote_path))
        upload = inviqa_confirm('>>> Continue?')
        with cd(self.remote_cd_path):
            if upload:
                put(self.local_path, self.remote_path)

