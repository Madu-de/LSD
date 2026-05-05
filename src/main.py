import time
import sys
import os
import select

class main:
	file = None
	pid = None
	path = None
	def __init__(self):
		self.run = True
		self.frames = 60
		self.frame_list = []
		if ".lsd" not in sys.argv[1]: # its very funny. so we keep that here
			raise Exception("unkown file type")
		self.file = open(sys.argv[1]).read().replace("\n","").split("<>")
		self.path = os.getcwd()
		os.system("python " + self.path + "/display.py &")
		pid = open(self.path + "/pid","r")
		self.pid = pid.read()
		os.system("stty -echo")
		if len(self.file) > 0:
			self.next()
	def loop(self):
		while self.run:
			try:
				start_time = time.time()
				while time.time() - start_time < 1/self.frames:
					pass 
				self.frame_list.append(time.time())
				while len(self.frame_list) > 0 and time.time() - self.frame_list[0] >= 1:
					self.frame_list.pop(0)
				self.main()
			except:
				os.system("kill " + self.pid)
				os.system("stty echo")
				exit()
	def main(self):
		vin = select.select([sys.stdin],[],[],0)[0]
		if len(vin) > 0:
			temp = vin[0].readline()
			if len(self.file) > 0:
				self.next()
	def next(self):
		os.system("echo '" + self.file.pop(0) + "' > " + self.path + "/in")
main = main().loop() 
