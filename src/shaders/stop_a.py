from .shader import Shader


class StopAShader(Shader):
    def __init__(self, display):
        def shader(self, name):
            self.display.remove_animation(name)
        super().__init__(display, shader)
