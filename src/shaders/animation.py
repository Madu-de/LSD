from .shader import Shader
import time


class AnimationShader(Shader):
    def __init__(self, display, animation_shader):
        def shader(self, x, y, time_limit, delay, name, *rest):
            dict = {}
            dict["start"] = time.time()
            dict["name"] = name

            def run():
                if time.time() - dict["start"] >= delay:
                    if time_limit is not None:
                        animation_shader(
                            self, x, y, (time.time() - dict["start"]) / time_limit, *rest)
                    else:
                        animation_shader(self, x, y, 1, *rest)
                    if time_limit is not None and time.time() - \
                            dict["start"] >= time_limit:
                        index = self.display.animations.index(run)
                        self.display.animations = self.display.animations[:index] + \
                            self.display.animations[index + 1:]
            self.display.animations += [run]
        super().__init__(display, shader)
