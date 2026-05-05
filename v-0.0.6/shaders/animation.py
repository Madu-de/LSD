import shader
import time

class animation(shader.shader):
	def __init__(self,display,animation_shader):
		def shader(self,x,y,time_limit,*rest):
			dict = {}
			dict["start"] = time.time()
			def run():
				animation_shader(self,x,y,(time.time() - dict["start"])/time_limit,*rest)
				if time.time() - dict["start"] >= time_limit: 
					index =  self.display.animations.index(run)
					self.display.animations = self.display.animations[:index] + self.display.animations[index + 1:]	
			self.display.animations += [run]
		super().__init__(display,shader)
