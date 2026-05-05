import sys
import json 
import os

sys.path.append(os.path.abspath(os.getcwd() + "/shaders"))
import a

display = [] 
class main:
	def __init__(self):
		pass
	def init(self):
		global display
		lines = os.get_terminal_size().lines
		columns = os.get_terminal_size().columns
		
		display = []
		
		display += [[]]
		
		for i in range(columns):
			display[0] += "."
		
		for i in range(lines):
			display += [*display[0]]
	def write(self):
		result = ""
		
		for i in range(len(display)):
			result += "".join(display[i])
		
		print(result[:-1])
main = main()
main.init()
main.write()
print(dir(a.a_shader(main)))
