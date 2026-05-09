import os
from time import *
import sys
import traceback
from helper import getSrcDirectory


class Logger:
    logfilePath = None

    def __init__(self, logfile):
        logDirPath = os.path.join(getSrcDirectory(), "..", "logs")
        self.logfilePath = os.path.join(logDirPath, logfile)
        if (not os.path.exists(logDirPath)):
            os.mkdir(logDirPath)

    def log(self, data):
        with open(self.logfilePath, "a") as file:
            file.write(data + "\n")

    def err(self):
        ex_type, ex_value, ex_traceback = sys.exc_info()
        trace_back = traceback.extract_tb(ex_traceback)

        self.log("--------------------- Exception ---------------------")
        self.log("Exception type: " + ex_type.__name__)
        self.log("Exception message: " + str(ex_value))
        self.log("Stacktrace:")
        for trace in trace_back:
            self.log(
                "File : %s , Line : %d, Func.Name : %s, Message : %s" %
                (trace[0], trace[1], trace[2], trace[3]))
        self.log("-----------------------------------------------------")
