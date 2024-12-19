import moderngl
from PIL import Image
import numpy as np
from renderer.shader import Shader

class Renderer:
    def __init__(self, ctx):
        self.ctx = ctx
        self.shader = Shader(self.ctx)
        self.shader.use()

    def load_texture(self, image):
        texture = self.ctx.texture(image.size, 3, image.tobytes())
        texture.use()
        return texture

    def clear_screen(self):
        self.ctx.clear(0.1, 0.1, 0.1)  # Background color: dark grey

    def render(self, obj):
        self.shader.render(obj)