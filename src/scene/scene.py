class Scene:
    def __init__(self):
        self.objects = []
        self.cameras = []
        self.active_camera = None

    def add_object(self, obj):
        self.objects.append(obj)
    
    def remove_object(self, obj):
        self.objects.remove(obj)

    def add_camera(self, camera):
        self.cameras.append(camera)
        if not self.active_camera:
            self.active_camera = camera

    def update(self):
        # Update objects and cameras
        for obj in self.objects:
            obj.update()

    def render(self, renderer):
        # Render each object in the scene
        for obj in self.objects:
            renderer.render(obj)
