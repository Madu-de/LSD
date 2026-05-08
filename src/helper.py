import platform
import sys
import os

def killWindows():
    if platform.system() == "Windows":
        print("Use a better OS (https://wiki.archlinux.org/title/Installation_guide)")
        exit()

def checkFile():
    if len(sys.argv) < 2:
        raise Exception("no filepath given")
    if ".lsd" not in sys.argv[1]: # its very funny. so we keep that here
        raise Exception("unkown file type")

def disableShellResponses():
    os.system("stty -echo")

def enableShellResponses():
    os.system("stty echo")

def clearTerminal():
    os.system("clear")

def getSrcDirectory():
    return os.path.dirname(os.path.realpath(__file__))