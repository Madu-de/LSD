class Shader:
    display = None
    shader = None

    def __init__(self, display, shader):
        self.display = display
        self.shader = shader

    def run(self, *parameters):
        self.shader(self, *parameters)
