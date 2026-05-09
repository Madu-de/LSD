from .animation import AnimationShader
from random import random
from colors import *

class LSDShader(AnimationShader):
    def __init__(self, display):
        def shader(self, x, y, progress, width, height, scale=1, full=False):
            width /= 2
            width *= scale
            height /= 2
            height *= scale
            range_x = self.display.range(
                self.display.translate_x(
                    x - width),
                self.display.translate_x(
                    x + width))
            range_y = self.display.range(
                self.display.translate_y(
                    y + height),
                self.display.translate_y(
                    y - height))
            keys = [*colors.keys()]
            for y in range_y:
                for x in range_x:
                    color1 = keys[int((len(keys) - 1) * random())]
                    color2 = keys[int((len(keys) - 1) * random())]
                    if full:
                        self.display.set_color(color1, color2)
                    else:
                        self.display.set_color(None, color2)
                    self.display._set(x, y, 0, self.display.get(x, y, 0)[1])
            if full:
                self.display.set_color("black", "white")
            else:
                self.display.set_color(None, "white")
        super().__init__(display, shader)
