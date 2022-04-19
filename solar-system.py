from ursina import *  # import ursina engine



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

    if mouse.hovered_entity == sol[0]:
        print("Hover!")
        info.visible = True
        print(mouse.x, mouse.y)
        info.x = mouse.x / 25.
        info.y = mouse.y / 25.
    else:
        info.visible = False
    print(mouse.x, mouse.y)


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
    sun     = Entity(model='sphere', position=(0, 0, 0), color=color.yellow,                 scale=2,    texture="tex/2k_sun", collider="sphere")
    corona  = Entity(model='sphere', position=(0, 0, 0), color=color.rgba(255, 255, 0, 128), scale=2.05, texture="tex/2k_sun")
    corona2 = Entity(model='sphere', position=(0, 0, 0), color=color.rgba(255, 255, 0, 32),  scale=2.15)

    return [sun, corona, corona2]


def planet_earth(parent):
    earth = Entity(parent=parent, model='sphere', position=(1, 0, 1), scale=0.2, texture="tex/earth")
    earth_atmosphere = Entity(parent=parent, model='sphere', position=(1, 0, 1), color=color.rgba(255, 255, 255, 32), scale=.22, texture="earth")
    return [earth, earth_atmosphere]


def moon(parent):
    return [Entity(parent=parent, model='sphere', color=color.white, position=(0.5, 0, 0.5), scale=0.09, texture="tex/2k_moon")]


def setup():
    camera.position = (0, 3.7, -7.5)  # x, y, z
    camera.rotation_x = 30
    window.borderless = False  # Show a border
    window.fullscreen = False  # Go full screen
    window.exit_button.visible = True  # Show the in-game red X that loses the window
    window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter
    window.size = (800, 600)
    window.center_on_screen()
    window.color = color.rgba(10, 10, 10, 0)


app     = Ursina()
sol     = star()
planets = planet_earth(sol[0])
moons   = moon(planets[0])

Text.size = 0.002
Text.default_resolution = 100
info = Text(text="Hover!")
info.visible = False


setup()

app.run()
