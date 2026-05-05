import animation

class next_shader(animation.animation):
	def __init__(self,display):
		def shader(self,x,y,progress):
			self.display.set_layer(0)
			width = self.display.columns
			height = self.display.lines
			width /= 2
			height /= 2
			range_x = self.display.range(self.display.translate_x(x - width), self.display.translate_x(x + width))
			range_y = self.display.range(self.display.translate_y(y + height), self.display.translate_y(y - height))
			for y in range_y:
				for x in range_x:
					if self.display.translate_x(-1.3*(self.display.columns/self.display.lines)*progress) <= x <= self.display.translate_x(1.3*(self.display.columns/self.display.lines)*progress):
						if self.display.translate_y(1.2*progress) <= y <= self.display.translate_y(-1.2*progress):
							self.display._set(x,y,0,self.display.get(x,y,1), False)
		super().__init__(display,shader)
