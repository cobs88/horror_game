import numpy as np

class Object:
    def __init__(self, vertices, texture):
        self.vertices = np.array(vertices, dtype='f4')
        self.texture = texture

    def update(self):
        # For now, no updates (can add animations or transformations here)
        pass