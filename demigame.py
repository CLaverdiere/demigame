import pyglet
import resource, player, i_sprite, weapon, bullet

win = pyglet.window.Window(fullscreen=True)
# win = pyglet.window.Window(height=800, width=800)

# Our batch for holding all objects to be drawn.
b_obj = pyglet.graphics.Batch()

# Our background batch, do be drawn under all other objects.
bg_obj = pyglet.graphics.Batch()

# Write info strings to the bottom of the screen.
help_msg = "Controls: WASD for movement, Mouse for look."
help_lbl = pyglet.text.Label(text=help_msg, x=10, y=30, batch=b_obj)

demi_msg = "Demigame prototype. Not ready for critical acclaim."
demi_lbl = pyglet.text.Label(text=demi_msg, x=10, y=10, batch=b_obj)

# Create sprites / players.
hero = player.Player(lives=3, name="Hero", walk_speed=300, mass=300, 
                        player_img=resource.hero_img, walk_anim=resource.hero_animwalk,
                        x=500, y=500, batch=b_obj)

# Create a background
tree_bg = pyglet.sprite.Sprite(img=resource.tree_bg_img,
          x=win.width/2 - resource.tree_bg_img.width/2, 
          y=win.height/2 - resource.tree_bg_img.height/2, batch=bg_obj)

# Add objects to environment
pistol = weapon.Weapon(x=200, y=100, batch=b_obj)

# Account for all of our interactive game objects.
g_objs = [hero, pistol]

# Handle handlers.
for obj in g_objs:
    for handler in obj.event_handlers:
        win.push_handlers(handler)

def init():
    pass

def update(dt):
    # Handle removed objects
    for obj in g_objs:
        if obj.remove:
            g_objs.remove(obj)
            obj.delete()

    # Handle collisions
    for i in range(len(g_objs)):
        for j in range(i+1, len(g_objs)):
            o1 = g_objs[i]
            o2 = g_objs[j]

            if o1.collides(o2):
                o1.handle_collision(o2)
                o2.handle_collision(o1)

    for obj in g_objs:
        obj.update(dt)

@win.event
def on_draw():
    win.clear()
    bg_obj.draw()
    b_obj.draw()

if __name__ == "__main__":
    init()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
