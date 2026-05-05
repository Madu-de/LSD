import shader

class clear_shader(shader.shader):
	def __init__(self,display):
		def shader(self,layer,none):
			self.display.clear_layer(layer)
		super().__init__(display,shader)
