import pyglet
import resource, player

win = pyglet.window.Window(fullscreen=True)
b_obj = pyglet.graphics.Batch()

help_msg = "Controls: WASD"
help_lbl = pyglet.text.Label(text=help_msg, x=10, y=30, batch=b_obj)

demi_msg = "demigame prototype. Not ready for official release."
demi_lbl = pyglet.text.Label(text=demi_msg, x=10, y=10, batch=b_obj)

demigod = player.Player(lives=99, name="Demi God", walk_speed=300, mass=300, 
                        player_img=resource.demigod_img, x=10, y=50, batch=b_obj)

g_objs = [demigod]
for obj in g_objs:
    for handler in obj.event_handlers:
        win.push_handlers(handler)

def init():
    pass

def update(dt):
    for obj in g_objs:
        obj.update(dt)

@win.event
def on_draw():
    win.clear()
    b_obj.draw()

if __name__ == "__main__":
    init()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
