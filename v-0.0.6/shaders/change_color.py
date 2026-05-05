import shader

class change_color_shader(shader.shader):
	def __init__(self,display):
		def shader(self,x,y,width,height,scale=1):
			width /= 2
			width *= scale
			height /= 2
			height *= scale
			range_x = self.display.range(self.display.translate_x(x - width), self.display.translate_x(x + width))
			range_y = self.display.range(self.display.translate_y(y + height), self.display.translate_y(y - height))
			for y in range_y:
				for x in range_x:
					self.display._set(x,y,0,self.display.get(x,y,0)[1])
		super().__init__(display,shader)
