import pyrr
import moderngl

class Shader:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vertex_shader = '''
        #version 330
        in vec3 in_vert;  // Use 3D positions
        in vec2 in_texcoord;
        out vec2 v_texcoord;
        
        uniform mat4 model;
        uniform mat4 view;
        uniform mat4 projection;

        void main() {
            gl_Position = projection * view * model * vec4(in_vert, 1.0);
            v_texcoord = in_texcoord;
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

        self.program = self.ctx.program(vertex_shader=self.vertex_shader, fragment_shader=self.fragment_shader)

    def use(self):
        self.program['Texture'].value = 0

    def render(self, obj):
        vbo = self.ctx.buffer(obj.vertices.tobytes())
        vao = self.ctx.simple_vertex_array(self.program, vbo, 'in_vert', 'in_texcoord')
        
        model = pyrr.matrix44.create_identity()
        view = pyrr.matrix44.create_from_translation([0, 0, -3])
        proj = pyrr.matrix44.create_perspective_projection(45, 800/600, 0.1, 1000)
        
        self.program['projection'].write(proj.astype('f4').tobytes())
        self.program['view'].write(view.astype('f4').tobytes())
        self.program['model'].write(model.astype('f4').tobytes())
        
        vao.render(moderngl.TRIANGLES)
