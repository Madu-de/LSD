from time import *
from select import *
from helper import *
from logger import *
import sys
import os
import display

class Main:
	file: str = None
	currentSlide: str = None
	def __init__(self):
		self.frames = 60
		self.frame_list = []
		self.file = open(sys.argv[1]).read().replace("\n","").split("<>")
		display.init()
		disableShellResponses()
		if len(self.file) > 0:
			self.next()
	def loop(self):
		while True:
			try:
				start_time = time()
				while time() - start_time < 1/self.frames:
					pass 
				self.frame_list.append(time())
				while len(self.frame_list) > 0 and time() - self.frame_list[0] >= 1:
					self.frame_list.pop(0)
				self.checkForNext()
				display.renderSlide(self.currentSlide)
			except:
				Logger("exception.log").err()
				enableShellResponses()
				exit()
	def checkForNext(self):
		vin = select([sys.stdin],[],[],0)[0]
		if len(vin) > 0:
			temp = vin[0].readline()
			if len(self.file) > 0:
				self.next()
	def next(self):
		self.currentSlide = self.file.pop(0)

if __name__ == "__main__":
	killWindows()
	checkFile()
	Main().loop()
