import pyrr

class Camera:
    def __init__(self):
        self.position = pyrr.Vector3([0.0, 0.0, -3.0])
        self.view_matrix = pyrr.matrix44.create_look_at(self.position, pyrr.Vector3([0.0, 0.0, 0.0]), pyrr.Vector3([0.0, 1.0, 0.0]))

    def update(self):
        # Camera movement logic can go here
        pass
