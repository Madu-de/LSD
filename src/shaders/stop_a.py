import shader

class stop_a_shader(shader.shader):
	def __init__(self,display):
		def shader(self,name,none):
			self.display.remove_animation(name)
		super().__init__(display,shader)
