import shader

class text_shader(shader.shader):
	def __init__(self,display):
		def shader(self,x,y,width,text,layer,scale=1):
			self.display.set_layer(layer)
			p_x = 0
			p_y = 0
			start = (width/2)*scale - 0.25*scale
			for i in text:
				if i != " ":
					if i == ".":
						self.display.shaders["dot"].run(x + p_x*scale - start,y + p_y*scale,scale)
					else:
						self.display.shaders[i.lower()].run(x + p_x*scale - start,y + p_y*scale,scale)
				p_x += 0.5
				if p_x > width - 0.25*scale:
					p_x = 0
					p_y -= 0.3
		super().__init__(display,shader)
