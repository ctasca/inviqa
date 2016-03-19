from fabric.operations import local
from fabric.api import *
from inviqa.project.Environment import *
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
        RemoteTaskNotifier()
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
