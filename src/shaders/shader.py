class shader: 
	display = None
	shader = None
	def __init__(self,display,shader):
		self.display = display 
		self.shader = shader
	def run(self,x,y,*rest):
		self.shader(self,x,y,*rest)	
