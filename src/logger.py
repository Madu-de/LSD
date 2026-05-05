import os

class logger:
    logfile = None
    def __init__(self, logfile):
        self.logfile = os.getcwd() + "/logs/" + logfile
    def log(self, data):
        with open(self.logfile, "a") as file:
            file.write(data + "\n")