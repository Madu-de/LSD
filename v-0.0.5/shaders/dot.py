import key 

class dot_shader(key.key_shader): 
	def __init__(self,display):
		def shader(self,x,y,scale):
			display.set(x - 0.05*scale, y, x + 0.05*scale, y - 0.1*scale,0,"+")
		super().__init__(display,shader)
