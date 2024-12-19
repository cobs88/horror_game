import pygame
import moderngl
import numpy as np
from pygame.locals import DOUBLEBUF, OPENGL
from PIL import Image
import pyrr
from renderer.renderer import Renderer
from scene.scene import Scene
from scene.object import Object
from renderer.camera import Camera

# Initialize Pygame and OpenGL context
pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
clock = pygame.time.Clock()

# Create a ModernGL context
ctx = moderngl.create_context()

# Set up the renderer
renderer = Renderer(ctx)

# Set up the scene
scene = Scene()

# Set up the camera
camera = Camera()
scene.add_camera(camera)

# Load the texture
texture_img = Image.open('assets/textures/dirt.png').convert('RGB')
texture = renderer.load_texture(texture_img)

# Define the object (a quad)
vertices = np.array([
    # Positions   # Texcoords
    [-0.5, -0.5, 0.0, 0.0, 0.0],
    [0.5, -0.5, 0.0, 1.0, 0.0],
    [-0.5, 0.5, 0.0, 0.0, 1.0],
    [0.5, -0.5, 0.0, 1.0, 0.0],
    [0.5, 0.5, 0.0, 1.0, 1.0],
    [-0.5, 0.5, 0.0, 0.0, 1.0],
], dtype='f4')

# Add object to the scene
obj = Object(vertices, texture)
scene.add_object(obj)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    renderer.clear_screen()

    # Render the scene
    scene.update()
    scene.render(renderer)

    # Swap the buffers
    pygame.display.flip()

    # Cap the framerate to 60 FPS
    clock.tick(60)

pygame.quit()
