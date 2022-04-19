from ursina import *  # import ursina engine
app = Ursina()  # Initialize your Ursina app


def update():
    for entity in sol:
        entity.rotation_y += time.dt * 10
    for entity in planets:
        entity.rotation_y += time.dt * 10
    for entity in moons:
        entity.rotation_y += time.dt * 10

    if held_keys['a']:
        camera.position += (0, time.dt, 0)
    if held_keys['q']:
        camera.position -= (0, time.dt, 0)
    if held_keys['w']:
        camera.position -= (0, 0, -time.dt)
    if held_keys['s']:
        camera.position -= (0, 0, time.dt)
    if held_keys['x']:
        exit(0)
    print(camera.position)

    Text.size = 0.001
    info = Text(text="Hover!")
    if mouse.hovered_entity == sol[0]:
        print("Hover!")
        #info.background = True
        info.visible = True
    else:
        info.visible = False


def input(key):
    if key == '1':
        camera.position = (0, 0, -20)
        camera.rotation_x = 0

    if key == '2':
        camera.position = (0, 20, 0)
        camera.rotation_x = 90

    if key == '3':
        camera.position = (0, 10, -20)
        camera.rotation_x = 30


def star():
    sun     = Entity(model='sphere', position=(0, 0, 0), color=color.yellow,                 scale=2,    texture="2k_sun", collider="sphere")
    corona  = Entity(model='sphere', position=(0, 0, 0), color=color.rgba(255, 255, 0, 128), scale=2.05, texture="2k_sun")
    corona2 = Entity(model='sphere', position=(0, 0, 0), color=color.rgba(255, 255, 0, 32),  scale=2.15)

    return [sun, corona, corona2]


def planet_earth(parent):
    earth = Entity(parent=parent, model='sphere', position=(1, 0, 1), scale=0.2, texture="earth")
    earth_atmosphere = Entity(parent=parent, model='sphere', position=(1, 0, 1), color=color.rgba(255, 255, 255, 32), scale=.22, texture="earth")
    return [earth, earth_atmosphere]


def moon(parent):
    return [Entity(parent=parent, model='sphere', color=color.white, position=(0.5, 0, 0.5), scale=0.09, texture="2k_moon")]


sol     = star()
planets = planet_earth(sol[0])
moons   = moon(planets[0])


def setup():
    camera.position = (0, 5, -10)  # x, y, z
    camera.rotation_x = 30
    window.borderless = False  # Show a border
    window.fullscreen = False  # Go full screen
    window.exit_button.visible = True  # Show the in-game red X that loses the window
    window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter
    window.size = (800, 600)
    window.center_on_screen()
    window.color = color.rgba(10, 10, 10, 0)


setup()
app.run()
