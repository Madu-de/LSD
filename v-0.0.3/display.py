import sys
import json 
import os

sys.path.append(os.path.abspath(os.getcwd() + "/shaders"))
import shaders

class display:
	lines = None
	columns = None
	display = None
	shaders = None
	def __init__(self):
		def is_not__(string):
			return not(string[0] == "_" and string[1] == "_")
		self.is_not__ = is_not__
	def init(self):
		self.lines = os.get_terminal_size().lines
		self.columns = os.get_terminal_size().columns
		
		self.display = []
		self.create_layer()
		
	def create_layer(self):
		display = [[]]		
		for i in range(self.columns):
			display[0] += " "
		
		for i in range(self.lines):
			display += [[*display[0]]]
		self.display += [display]
		
	def init_shader(self):
		self.shaders = {}
		self.shaders["a"] = shaders.a.a_shader(self)
		self.shaders["b"] = shaders.b.b_shader(self)
		self.shaders["c"] = shaders.c.c_shader(self)
		self.shaders["d"] = shaders.d.d_shader(self)
	def write(self):
		result = ""
		display = self.display[0]
		
		for i in range(len(display)):
			result += "".join(display[i])
		
		print(result)
	def set_line(self,x1,y1,x2,y2,layer,char):
		x1 = self.translate_x(x1)
		y1 = self.translate_y(y1)
		x2 = self.translate_x(x2)
		y2 = self.translate_y(y2)
		range_x = self.range(x1,x2)
		range_y = self.range(y1,y2)
		if len(range_x) >= len(range_y):
			factor = len(range_y)/len(range_x)
			for i in range(len(range_x)):
				self._set(range_x[i], range_y[int(i*factor)],layer,char)
		if len(range_x) < len(range_y):
			factor = len(range_x)/len(range_y)
			for i in range(len(range_y)):
				self._set(range_x[int(i*factor)],range_y[i],layer,char)
	def set(self,x1,y1,x2,y2,layer,char):
		x1 = self.translate_x(x1)
		y1 = self.translate_y(y1)
		x2 = self.translate_x(x2)
		y2 = self.translate_y(y2)
		for y in range(y1,y2+1):
			for x in range(x1,x2+1):
				self._set(x,y,layer,char)	
	def _set(self,x,y,layer,char):
		self.display[layer][y][x] = char
	def translate_x(self,x):
		x = self.ratio_correction_x(x)
		result = int((x+1)*((self.columns-1)/2))
		if result < 0:
			result = 0
		if result > self.columns-1:
			result = self.columns-1
		return result
	def translate_y(self,y):
		y = self.ratio_correction_y(y)
		result = int((-y+1)*((self.lines)/2))
		if result < 0:
			result = 0
		if result > self.lines:
			result = self.lines
		return result
	def ratio_correction_x(self,x):
		if self.columns > self.lines:
			x *= self.lines/self.columns
		return x
	def ratio_correction_y(self,y):
		if self.lines> self.columns:
			y *= self.columns/self.lines
		return y
	def range(self,start,end):
		result = []	
		increment = 1
		if start > end:
			increment = -1
		while start != end:
			result += [start]
			start += increment
		result += [start]
		return result
display = display()
display.init()
display.init_shader()
display.shaders["a"].run(-0.5,0,1)
display.shaders["b"].run(0,0,1)
display.shaders["c"].run(0.5,0,1)
display.shaders["d"].run(1,0,1)
display.write()
