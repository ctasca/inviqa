import os, sys, subprocess
from subprocess import *
from fabric.api import *
from inviqa.fabric.cli import confirm as inviqa_confirm
from inviqa.fabric.cli import prompt, puts
from inviqa.network.operations import Downloader

class MediaDownloader:
    def __init__(self, sync_dir, environment):
        self.sync_dir = sync_dir
        self.env = environment
    def download(self, pubdir = 'public'):
        sync_dir = os.sep + 'media' + os.sep + self.sync_dir
        local_sync_dir = sync_dir
        sync_dir_segments = sync_dir.split(os.sep)
        last = sync_dir_segments.pop()

        if "." not in last:
            local_sync_dir = os.sep.join(sync_dir_segments)

        remote_dir = self.env.www_public_dir() + sync_dir
        local_dir = self.env.local_project_dir() + os.sep + pubdir + local_sync_dir

        downloader = Downloader(remote_dir, local_dir)
        downloader.download()
