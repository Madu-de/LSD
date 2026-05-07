import time
import sys
import os
import select
import platform

class main:
	file = None
	pid = None
	path = None
	def __init__(self):
		self.killWindows()
		self.run = True
		self.frames = 60
		self.frame_list = []
		if ".lsd" not in sys.argv[1]: # its very funny. so we keep that here
			raise Exception("unkown file type")
		self.file = open(sys.argv[1]).read().replace("\n","").split("<>")
		self.path = os.getcwd()
		if not os.path.exists(self.path + "/temp"):
			os.mkdir(self.path + "/temp")
		os.system("python " + self.path + "/display.py &")
		pidPath = self.path + "/temp/pid"
		if not os.path.exists(pidPath):
			open(pidPath, "x")
		pid = open(pidPath,"r")
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
		inPath = self.path + "/temp/in"
		if not os.path.exists(inPath):
			open(inPath, "x")
		os.system("echo '" + self.file.pop(0) + "' > " + inPath)
	def killWindows(self):
		if platform.system() == "Windows":
			print("Use a better OS (https://wiki.archlinux.org/title/Installation_guide)")
			exit()
main = main().loop() 
