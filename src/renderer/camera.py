import pyrr

class Camera:
    def __init__(self, position, target, up=pyrr.Vector3([0.0, 1.0, 0.0]), fov=45.0, aspect_ratio=1.333, near=0.1, far=100.0):
        self.position = position
        self.target = target
        self.up = up
        self.fov = fov
        self.aspect_ratio = aspect_ratio
        self.near = near
        self.far = far
        self.view = pyrr.matrix44.create_look_at(self.position, self.target, self.up)
        self.projection = pyrr.matrix44.create_perspective_projection(self.fov, self.aspect_ratio, self.near, self.far)

    def update(self):
        """Update the camera's view matrix."""
        self.view = pyrr.matrix44.create_look_at(self.position, self.target, self.up)

    def set_position(self, position):
        """Set the camera's position."""
        self.position = position
        self.update()

    def set_target(self, target):
        """Set the camera's target."""
        self.target = target
        self.update()

    def set_up(self, up):
        """Set the camera's up vector."""
        self.up = up
        self.update()
