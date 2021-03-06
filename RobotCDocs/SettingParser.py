import PythonFileLibrary.SettingParser

"""
    SettingParser.py

    Parses setup.txt for library name, the directory of the files you want to scan, and
    the output directory of BuiltInVariables.txt.
"""
class SettingParser(PythonFileLibrary.SettingParser.SettingParser):
    def __init__(self):
        super().__init__()
        self.libraryName = ""
        self.libraryDirectory = ""
        self.outputDirectory = ""

        try:
            self.Parse()
        except AssertionError as error:
            print(error)

    # Parse setup.txt. Will throw an AssertionError if the
    # file cannot be read.
    def Parse(self):
        assert self.canParse, "SettingParser.py: Could not parse setup.txt."

        currentSetting = 0
        for line in self.GetSettings():
            currentSetting += 1

            if currentSetting == 1:
                self.libraryName = self.GetNextLine().strip()

            if currentSetting == 2:
                self.libraryDirectory = self.GetNextLine().strip()

            if currentSetting == 3:
                self.outputDirectory = self.GetNextLine().strip()

        self.ResetReader()
