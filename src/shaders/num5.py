from .key import KeyShader


class Num5Shader(KeyShader):
    def __init__(self, display):
        def shader(self, x, y, scale):
            display.set_line(
                x - 0.1 * scale,
                y + 0.1 * scale,
                x - 0.1 * scale,
                y,
                0,
                "|")
            display.set_line(
                x + 0.1 * scale,
                y + 0.1 * scale,
                x - 0.1 * scale,
                y + 0.1 * scale,
                0,
                "-")
            display.set_line(
                x - 0.1 * scale,
                y,
                x + 0.1 * scale,
                y - 0.05 * scale,
                0,
                "\\")
            display.set_line(
                x + 0.1 * scale,
                y - 0.05 * scale,
                x - 0.1 * scale,
                y - 0.1 * scale,
                0,
                "/")
        super().__init__(display, shader)
