from .shader import Shader


class ChangeColorShader(Shader):
    def __init__(self, display):
        def shader(self, x, y, width, height, layer, scale=1):
            self.display.set_layer(layer)
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
            for y in range_y:
                for x in range_x:
                    self.display._set(
                        x, y, 0, self.display.get(
                            x, y, layer)[1])
            self.display.set_layer(0)
        super().__init__(display, shader)
