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
		self.shaders["e"] = shaders.e.e_shader(self)
		self.shaders["f"] = shaders.f.f_shader(self)
		self.shaders["g"] = shaders.g.g_shader(self)
		self.shaders["h"] = shaders.h.h_shader(self)
		self.shaders["i"] = shaders.i.i_shader(self)
		self.shaders["j"] = shaders.j.j_shader(self)
		self.shaders["k"] = shaders.k.k_shader(self)
		self.shaders["l"] = shaders.l.l_shader(self)
		self.shaders["m"] = shaders.m.m_shader(self)
		self.shaders["n"] = shaders.n.n_shader(self)
		self.shaders["o"] = shaders.o.o_shader(self)
		self.shaders["p"] = shaders.p.p_shader(self)
		self.shaders["q"] = shaders.q.q_shader(self)
		self.shaders["r"] = shaders.r.r_shader(self)
		self.shaders["s"] = shaders.s.s_shader(self)
		self.shaders["t"] = shaders.t.t_shader(self)
		self.shaders["u"] = shaders.u.u_shader(self)
		self.shaders["v"] = shaders.v.v_shader(self)
		self.shaders["w"] = shaders.w.w_shader(self)
		self.shaders["x"] = shaders.x.x_shader(self)
		self.shaders["y"] = shaders.y.y_shader(self)
		self.shaders["z"] = shaders.z.z_shader(self)
		self.shaders["1"] = shaders.i1.i1_shader(self)
		self.shaders["2"] = shaders.i2.i2_shader(self)
		self.shaders["3"] = shaders.i3.i3_shader(self)
		self.shaders["4"] = shaders.i4.i4_shader(self)
		self.shaders["5"] = shaders.i5.i5_shader(self)
		self.shaders["6"] = shaders.i6.i6_shader(self)
		self.shaders["7"] = shaders.i7.i7_shader(self)
		self.shaders["8"] = shaders.i8.i8_shader(self)
		self.shaders["9"] = shaders.i9.i9_shader(self)
		self.shaders["0"] = shaders.i0.i0_shader(self)
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
scale = 1 
display.shaders["a"].run(-3.5,0,scale)
display.shaders["b"].run(-3,0,scale)
display.shaders["c"].run(-2.5,0,scale)
display.shaders["d"].run(-2,0,scale)
display.shaders["e"].run(-1.5,0,scale)
display.shaders["f"].run(-1,0,scale)
display.shaders["g"].run(-0.5,0,scale)
display.shaders["h"].run(0,0,scale)
display.shaders["i"].run(0.5,0,scale)
display.shaders["j"].run(1,0,scale)
display.shaders["k"].run(1.5,0,scale)
display.shaders["l"].run(2,0,scale)
display.shaders["m"].run(2.5,0,scale)
display.shaders["n"].run(3,0,scale)
display.shaders["o"].run(3.5,0,scale)
display.shaders["p"].run(-3.5,-0.25,scale)
display.shaders["q"].run(-3,-0.25,scale)
display.shaders["r"].run(-2.5,-0.25,scale)
display.shaders["s"].run(-2,-0.25,scale)
display.shaders["t"].run(-1.5,-0.25,scale)
display.shaders["u"].run(-1,-0.25,scale)
display.shaders["v"].run(-0.5,-0.25,scale)
display.shaders["w"].run(0,-0.25,scale)
display.shaders["x"].run(0.5,-0.25,scale)
display.shaders["y"].run(1,-0.25,scale)
display.shaders["z"].run(1.5,-0.25,scale)
display.shaders["1"].run(2,-0.25,scale)
display.shaders["2"].run(2.5,-0.25,scale)
display.shaders["3"].run(3,-0.25,scale)
display.shaders["4"].run(3.5,-0.25,scale)
display.shaders["5"].run(-3.5,-0.5,scale)
display.shaders["6"].run(-3,-0.5,scale)
display.shaders["7"].run(-2.5,-0.5,scale)
display.shaders["8"].run(-2,-0.5,scale)
display.shaders["9"].run(-1.5,-0.5,scale)
display.shaders["0"].run(-1,-0.5,scale)
display.write()
