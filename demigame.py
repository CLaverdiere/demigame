import pyglet
import resource, player, i_sprite

win = pyglet.window.Window(fullscreen=True)

# Our batch for holding all objects to be drawn.
b_obj = pyglet.graphics.Batch()

# Write info strings to the bottom of the screen.
help_msg = "Controls: WASD"
help_lbl = pyglet.text.Label(text=help_msg, x=10, y=30, batch=b_obj)

demi_msg = "demigame prototype. Not ready for official release."
demi_lbl = pyglet.text.Label(text=demi_msg, x=10, y=10, batch=b_obj)

# Create sprites / players.
hero = player.Player(lives=3, name="Hero", walk_speed=300, mass=300, 
                        player_img=resource.hero_img, walk_anim=resource.hero_animwalk,
                        x=500, y=500, batch=b_obj)

# Account for all of our interactive game objects.
g_objs = [hero]

# Handle handlers.
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
