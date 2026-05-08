import shader

class ClearShader(shader.Shader):
	def __init__(self,display):
		def shader(self,layer):
			self.display.clear_layer(layer)
		super().__init__(display,shader)
