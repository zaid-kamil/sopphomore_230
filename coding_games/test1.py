import pgzrun

colors = [0, 0, 0]

def draw():
    screen.fill(tuple(colors))

def update():
    colors[0] = (colors[0] + 1) % 256

def on_key_down(key, mod, unicode):
    colors[1] = (colors[1] + 1) % 256

pgzrun.go()