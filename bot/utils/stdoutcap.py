import sys


class STDRedirect:
    def __init__(self):
        self.stdout = sys.stdout
        sys.stdout = self
        self.data = ""

    def write(self, data):
        self.data += data

    def flush(self, *args):
        pass

    def exit(self):
        sys.stdout = self.stdout

    def enter(self):
        sys.stdout = self
