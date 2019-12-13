import os
import pickle
from datetime import date

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from options import Options
from colors import Colors


class File:
    """

    """

    def __init__(self, content):
        self.name = date.today().strftime("%Y-%m-%d") + ".report"
        self.dir = Options.DIR
        self.path = os.path.join(self.dir, self.name)
        self.content = content

    def save(self):
        """
        Saves informations collected from an IP in a file.
        """

        with open(self.path, 'wb+') as f:
            pickle.dump(self.content, f)
        print(Options.LIST_INFO + Colors.GREEN + "File saved!\n" + Colors.ENDC)

    def compare(self):
        """
        Compares the saved information (baseline) with the new information and save a report in gsheet.
        """

        # We take the most recent baseline finded in 'reports' directory.
        files_name = []
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                files_name.append(file)
        files_name.sort()

        # We check if there is a baseline
        if files_name:
            with open(os.path.join(self.dir, files_name.pop()), 'rb') as f:
                baseline_content = pickle.load(f)
                current_content = self.content

                is_difference = False
                for baseline_key, baseline_value in baseline_content.items():
                    current_value = current_content.get(baseline_key)

                    # Test the lengh difference between fetched infos
                    if len(baseline_content) != len(self.content):
                        is_difference = True
                        print(Options.LIST_INFO + Colors.INFO + "Difference detected!\n" + Colors.ENDC)

                    # Test the differences between open ports, services and protocols
                    elif type(baseline_value) == list:
                        for baseline_zip, current_zip in zip(baseline_value, current_value):
                            if baseline_zip != current_zip:
                                is_difference = True
                                print(Options.LIST_INFO + Colors.INFO + "Difference detected!\n" + Colors.ENDC)

                    # Test the other value
                    elif baseline_value != current_value:
                        is_difference = True
                        print(Options.LIST_INFO + Colors.INFO + "Difference detected!\n" + Colors.ENDC)

                if is_difference is False:
                    print(Options.LIST_INFO + Colors.GREEN + "No difference detected!\n" + Colors.ENDC)

            print(Options.LIST_INFO + Colors.INFO + "Saving reports in Google Sheet...\n" + Colors.ENDC)
            self.gsheet()
            print(Options.LIST_INFO + Colors.GREEN + "Report saved!\n" + Colors.ENDC)

        else:
            msg = "No baseline. Please run python3 cyberwatch.py -H [ip] -s"
            print(Colors.FAIL + Colors.BOLD + "\n" + Options.LIST_ERROR + "ERROR: " + Colors.ENDC + msg + "\n")

    def gsheet(self):
        """
        Write fetched informations on a Google Sheet
        """

        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'cyberwatch_gsheet.json', scope)

        gc = gspread.authorize(credentials)
        sh = gc.open('cyberwatch')
        try:
            wh = sh.add_worksheet(title=self.name, rows="100", cols="5")
        except Exception as e:
            wh = sh.worksheet(self.name)

        i = 1
        for key, value in self.content.items():
            wh.update_cell(i, 1, key)
            if type(value) == list:
                wh.update_cell(i, 2, str(value))
            else:
                wh.update_cell(i, 2, value)
            i += 1
