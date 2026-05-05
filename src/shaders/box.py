import shader

class box_shader(shader.shader):
	def __init__(self,display):
		def shader(self,x,y,width,height,layer,scale=1):
			self.display.shaders["change_color"].run(x,y,width,height,layer,scale)
			self.display.set_layer(layer)
			width /= 2
			width *= scale
			height /= 2
			height *= scale
			self.display.set_line(x - width, y - height, x + width,y - height,0,"-")
			self.display.set_line(x - width, y + height, x - width,y - height,0,"|")
			self.display.set_line(x + width, y + height, x + width,y - height,0,"|")
			self.display.set_line(x - width, y + height, x + width,y + height,0,"-")
			self.display.set_layer(0)
		super().__init__(display,shader)
