from renderer.camera import Camera
from scene.object import Object
import pyrr

class Scene:
    def __init__(self):
        self.objects = []
        self.cameras = []

    def add_object(self, obj):
        """Add an object to the scene."""
        self.objects.append(obj)

    def add_camera(self, camera):
        """Add a camera to the scene."""
        self.cameras.append(camera)

    def update(self):
        """Update the scene (for future use, e.g., animations)."""
        pass

    def render(self, renderer):
        """Render all objects in the scene."""
        for obj in self.objects:
            # Assuming the camera is already set in the renderer
            if renderer.camera:
                model = pyrr.matrix44.create_identity()  # Or apply object-specific transformations
                view = renderer.camera.view
                projection = renderer.camera.projection
                renderer.render(obj, model, view, projection)
