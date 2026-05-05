import shader

class color_shader(shader.shader):
	def __init__(self,display):
		def shader(self,background_color=None,color=None):
			self.display.set_color(background_color,color)
		super().__init__(display,shader)
