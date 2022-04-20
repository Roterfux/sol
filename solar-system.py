from ursina import *  # import ursina engine

pause = False


def update():
    if not pause:
        for entity in sol:
            entity.rotation_y += time.dt * 10
        for entity in planet:
            entity.rotation_y += time.dt * 50
        for entity in moons:
            entity.rotation_y -= time.dt * 100

    key_action()
    mouse_action()


def key_action():
    if held_keys['e']:
        camera.position += (0, time.dt, 0)
    if held_keys['q']:
        camera.position -= (0, time.dt, 0)
    if held_keys['w']:
        camera.position -= (0, 0, -time.dt)
    if held_keys['s']:
        camera.position -= (0, 0, time.dt)
    if held_keys['a']:
        camera.position -= (time.dt, 0, 0)
    if held_keys['d']:
        camera.position -= (-time.dt, 0, 0)

    if held_keys['x']:
        exit(0)
    # print("{:.3f} {:.3f} {:.3f}".format(camera.position.x, camera.position.y, camera.position.z))


def mouse_action():
    if mouse.hovered_entity == sol[0]:
        info.visible = True
        info.x = mouse.x / 25.
        info.y = mouse.y / 25.
    else:
        info.visible = False
    # print(": {:.3f} {:.3f}".format(mouse.x, mouse.y))


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

    if key == "space":
        global pause
        pause = not pause


def star():
    sol = Entity(model='sphere',
                 position=(0, 0, 0),
                 color=color.yellow,
                 scale=2,
                 texture="tex/2k_sun",
                 collider="sphere")
    corona = Entity(model='sphere',
                    position=(0, 0, 0),
                    color=color.rgba(255, 255, 0, 128),
                    scale=2.05,
                    texture="tex/2k_sun")
    corona2 = Entity(model='sphere',
                     position=(0, 0, 0),
                     color=color.rgba(255, 255, 0, 32),
                     scale=2.15)

    return [sol, corona, corona2]


def planet(parent, position, texture):
    sphere = Entity(parent=parent,
                    model='sphere',
                    position=position,
                    scale=0.2,
                    texture=texture)
    sphere_atmosphere = Entity(parent=parent,
                               model='sphere',
                               position=position,
                               color=color.rgba(0, 0, 128, 96),
                               scale=.22,
                               collider='box',
                               on_click=show_name)
    return [sphere, sphere_atmosphere]


def moon(parent):
    for _ in range(10):
        satellite = Entity(parent=parent,
                           model='sphere',
                           color=color.white,
                           position=(1 + random.random() * 1.3, 0, 0),
                           scale=0.1 * random.random(),
                           texture="tex/2k_moon",
                           rotation_y=random.random() * 180
                           )
    return [satellite]


def show_name():
    Text.size = 0.002
    Text.default_resolution = 100
    text_name = Text(text="Earth")
    text_name.x = mouse.x / 25.
    text_name.y = mouse.y / 25.
    text_name.visible = True
    print("Click!")


def setup():
    camera.position = (0, 3.7, -7.5)  # x, y, z
    camera.rotation_x = 30
    window.borderless = False  # Show a border
    window.fullscreen = False  # Go full screen
    window.exit_button.visible = True  # Show the in-game red X that loses the window
    window.fps_counter.enabled = True  # Show the FPS (Frames per second) counter
    window.size = (1200, 800)
    window.center_on_screen()
    window.color = color.rgba(10, 10, 10, 0)


app = Ursina()

sol = star()
planet = planet(sol[0], position=(1, 0, 1), texture="tex/earth")
moons = moon(planet[0])

Text.size = 0.002
Text.default_resolution = 100
info = Text(text="Hover!")
info.visible = False

setup()

app.run()
