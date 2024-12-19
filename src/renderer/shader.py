import pyrr
import moderngl

class Shader:
    def __init__(self, ctx):
        self.ctx = ctx
        
        self.vertex_shader = '''
        #version 330
        in vec3 in_vert;  // Position of the vertex
        in vec2 in_texcoord;  // Texture coordinates
        out vec2 v_texcoord;

        uniform mat4 model; 
        uniform mat4 view;  // View matrix from the camera
        uniform mat4 projection;  // Projection matrix (perspective)

        void main() {
            gl_Position = projection * view * model * vec4(in_vert, 1.0);  // Apply all transformations
            v_texcoord = in_texcoord;  // Pass texture coordinates to fragment shader
        }
        '''
        
        self.fragment_shader = '''
        #version 330
        uniform sampler2D Texture;
        in vec2 v_texcoord;
        out vec4 f_color;

        void main() {
            f_color = texture(Texture, v_texcoord);
        }
        '''

        # Create the shader program
        self.program = self.ctx.program(vertex_shader=self.vertex_shader, fragment_shader=self.fragment_shader)

    def use(self):
        # Use texture unit 0
        self.program['Texture'].value = 0

    def set_matrices(self, model, view, projection):
        """Pass the model, view, and projection matrices to the shader."""
        self.program['model'].write(model.astype('f4').tobytes())
        self.program['view'].write(view.astype('f4').tobytes())
        self.program['projection'].write(projection.astype('f4').tobytes())

    def render(self, obj, model, view, projection):
        """Render the object with the passed matrices."""
        # Create the VBO and VAO for the object
        vbo = self.ctx.buffer(obj.vertices.tobytes())
        vao = self.ctx.simple_vertex_array(self.program, vbo, 'in_vert', 'in_texcoord')

        # Set the matrices in the shader
        self.set_matrices(model, view, projection)

        # Render the object
        vao.render(moderngl.TRIANGLES)
