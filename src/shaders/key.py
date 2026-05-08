import shader

class KeyShader(shader.Shader):
	def __init__(self,display,base_shader):
		def shader(self,x,y,scale=1):
			base_shader(self,x,y,scale)
		super().__init__(display,shader)
