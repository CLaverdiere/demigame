import pyglet
import resource, player, i_sprite, weapon, bullet

win = pyglet.window.Window(fullscreen=True)
# win = pyglet.window.Window(height=800, width=800)

# Game objects batch for holding all interactive game objects.
b_gameobj = pyglet.graphics.Batch()

# Background batch, do be drawn under all other objects.
b_bg = pyglet.graphics.Batch()

# Environment batch, to hold all non interactive environmental objects.
b_env = pyglet.graphics.Batch()

# Write info strings to the bottom of the screen.
help_msg = "Controls: WASD for movement, Mouse for look. Shift to run."
help_lbl = pyglet.text.Label(text=help_msg, x=10, y=30, batch=b_gameobj)

demi_msg = "Demigame prototype. Not ready for critical acclaim."
demi_lbl = pyglet.text.Label(text=demi_msg, x=10, y=10, batch=b_gameobj)

# Create sprites / players.
hero = player.Player(lives=3, name="Hero", walk_speed=300, mass=300, 
                        player_img=resource.hero_img, walk_anim=resource.hero_animwalk,
                        x=win.width/2, y=win.height/2, batch=b_gameobj)

# Create a background
tree_bg = i_sprite.ISprite(img=resource.tree_bg_img, 
            x=hero.x, y=hero.y, batch=b_bg)
# desert_bg = i_sprite.ISprite(img=resource.desert_bg_img, 
#             x=hero.x, y=hero.y, batch=b_bg)

# Add objects to environment
pistol = weapon.Weapon(x=hero.x, y=hero.y, 
                       disp_x=-400, disp_y=300, batch=b_gameobj)

# Account for all of our interactive / non-interactive game objects.
bg_objs = [tree_bg]
g_objs = [hero, pistol]

# Handle handlers.
for handler in hero.event_handlers:
    win.push_handlers(handler)
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

    # Update all environment objects relative to player.
    for obj in g_objs[1:] + bg_objs:
        obj.update(dt, hero)

    # Update our player
    hero.update(dt)

@win.event
def on_draw():
    win.clear()
    b_bg.draw()
    b_env.draw()
    b_gameobj.draw()

if __name__ == "__main__":
    init()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
