import os
from datetime import date

from options import Options
from colors import Colors


class File:
    def __init__(self, content):
        self.name = date.today().strftime("%d-%m-%Y") + "_report.log"
        self.dir = Options.DIR
        self.path = os.path.join(self.dir, self.name)
        self.content = content

    def save(self):
        with open(self.path, 'a+') as f:
            for line in self.content:
                f.write(line)
        print(Options.LIST_INFO + Colors.GREEN + "File saved!\n" + Colors.ENDC)
