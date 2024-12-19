import moderngl
import numpy as np
from renderer.shader import Shader

class Renderer:
    def __init__(self, ctx):
        self.ctx = ctx
        self.shader = Shader(ctx)  # Initialize the shader here
        self.objects = []
        self.camera = None

    def set_camera(self, camera):
        """Set the camera for the renderer."""
        self.camera = camera

    def clear_screen(self):
        """Clear the screen before rendering."""
        self.ctx.clear()

    def load_texture(self, img):
        """Load a texture from an image."""
        texture = self.ctx.texture(img.size, 3, img.tobytes())
        texture.use()
        return texture

    def render(self, obj, model, view, projection):
        """Render a single object using the shader and camera matrices."""
        self.shader.use()  # Activate the shader
        self.shader.render(obj, model, view, projection)  # Pass matrices and render the object
