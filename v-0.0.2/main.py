import time

class main:
	def __init__(self):
		self.run = True
		self.frames = 60
		self.frame_list = []
	def loop(self):
		while self.run:
			start_time = time.time()
			while time.time() - start_time < 1/self.frames:
				pass 
			self.frame_list.append(time.time())
			while len(self.frame_list) > 0 and time.time() - self.frame_list[0] >= 1:
				self.frame_list.pop(0)
			self.main()
	def main(self):
		print(len(self.frame_list))
main = main().loop() 
