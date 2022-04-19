from ursina import *  # import ursina engine

app = Ursina()  # Initialize your Ursina app

sun = Entity(model='sphere',
             position=(0, 0, 0),
             color=color.yellow,
             scale=2,
             texture="tex/2k_sun",
             collider="sphere"
             )
asphere = Entity(model="sphere",
                 position=(0, 0, 0),
                 color=color.rgba(255, 255, 0, 128),
                 scale=2.05,
                 texture="tex/2k_sun")


def generate_star():
    pass


def update():
    sun.rotation_y += time.dt * 10
    if mouse.hovered_entity == sun:
        print("!")

    #if mouse.position.y >= sun.y:
    #    pitch = -1
    #else:
    #    pitch = 1

    keyboard_navigation()


def keyboard_navigation():
    if held_keys['a']:
        sun.position += (-time.dt, 0, 0)
    if held_keys['d']:
        sun.position += (time.dt, 0, 0)
    if held_keys['w']:
        sun.position += (0, 0, -time.dt)
    if held_keys['s']:
        sun.position += (0, 0, time.dt)


def setup():
    camera.position = (0, 5, -9)  # x, y, z
    camera.rotation_x = 30
    window.borderless = False  # Show a border
    window.exit_button.visible = True  # Show the in-game red X that loses the window
    window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter
    window.size = (1024, 768)
    window.center_on_screen()
    window.color = color.rgba(10, 10, 10, 0)


setup()
app.run()
