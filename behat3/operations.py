from fabric.api import local
from inviqa.fabric.cli import prompt, puts
from inviqa.fabric.Colors import Colors
import re,os
from os.path import splitext

c = Colors()

class CliTool:
    def __init__(self):
        self.profile = False
        self.path = False
        self.fpath = False
        self.selected = False
        self.absolute_fpath = False
        self.exclude_walk_dirs = ['bootstrap']
        self.features_list = []
    def add_walk_exclude_dir(self, dirname):
        self.exclude_walk_dirs.append(dirname)
    def set_profile(self, profile):
        """
        Sets behat profile in scope when running features (as defined in behat.yml)
        """
        self.profile = profile

    def set_path(self, path):
        """
        Sets absolute path to 'features' folder
        """
        self.path = path
    def set_driver(self, driver):
        """
        Sets driver instance. Driver must have start and stop methods in its protocol
        """
        self.driver = driver
    def run_prompt(self, fpath):
        """
        Provide list of available features directories and features
        """
        self.absolute_fpath = os.path.abspath(fpath)
        exclude = set(self.exclude_walk_dirs)


        for root, subdirs, files, in os.walk(self.absolute_fpath):
            subdirs[:] = [d for d in subdirs if d not in exclude]

            for name in files:
                ext = splitext(name)[1]
                if (ext != '.feature'):
                    continue
                fp = os.path.join(root, name)
                replace = self.absolute_fpath + os.sep
                fp = fp.replace(replace, '')
                self.features_list.append(fp)
            for name in subdirs:
                self.features_list.append(name)


        for feature in self.features_list:
            i = self.features_list.index(feature) + 1
            print str(c.get("[" + str(i) + "]")) + " " + feature

        self.selected = prompt('>>> Choose feature/features to run or press enter for entire suite')

        # when no features dir or feature is provided, run all in features path
        if (self.selected.isdigit() == False):
            self.path = fpath
    def run(self):
        """
         Runs behat selected features in specified path.
         """
        if self.path == False:
            puts("!!! Cannot list 'features' from specified path.")
            return 1

        profile  = prompt('>>> Enter Behat profile or press enter to run default profile')
        options  = prompt('>>> Enter any additional options for behat command or press enter')

        if re.match(r'^\d{1,}-\d{1,}', self.selected):
            range_split = self.selected.split('-')
            selected_list = range(int(range_split[0]), int(range_split[1]))
        else:
            selected_list = self.selected.split(' ')

        for selected in selected_list:
            selected = str(selected);

            if selected.isdigit():
                findex = int(selected.strip()) -1

            if selected.isdigit() == False:
                run_feature = ''
            else:
                run_feature = self.features_list[findex]

            line = prompt('>>> Enter line number, or press enter')

            if line:
                    run_feature = run_feature + ':' + line

            if run_feature != '':
                puts("*** Running feature: " + run_feature)
            else:
                puts("*** Running all features in suite")

            behat_command = "bin/behat features/%s %s" % (run_feature, options)

            if (profile):
                behat_command = "bin/behat -p %s features/%s %s" % (profile, run_feature, options)

            local(behat_command)


class Runner:
    def __init__(self):
        pass
