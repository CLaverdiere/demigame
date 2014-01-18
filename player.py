import pyglet
import resource, i_sprite
import math
from pyglet.window import key

class Player(i_sprite.ISprite):
    def __init__(self, lives=3,
                       name="Default Player",
                       walk_speed=250,
                       mass=75,
                       player_img=resource.ponyo_img,
                       walk_anim=None,
                       *args,
                       **kwargs):
        super(Player, self).__init__(img=player_img, *args, **kwargs)
        self.lives = lives
        self.name = name
        self.walk_speed = walk_speed
        self.mass = mass
        self.player_img = player_img
        self.walk_anim = walk_anim

        # Key handling
        self.keyh = key.KeyStateHandler()
        self.event_handlers = [self, self.keyh]

        # Movement
        self.walking = False

    def on_mouse_motion(self, x, y, dx, dy):
        # Make our player face the mouse.
        self.rotation = 90 + -math.degrees( math.atan( (y - self.y) / (x - self.x) ) )

    def update(self, dt):
        # Movement controls, WASD.
        if self.keyh[key.A]:
            self.x -= self.walk_speed * dt
        elif self.keyh[key.D]:
            self.x += self.walk_speed * dt
        if self.keyh[key.W]:
            self.y += self.walk_speed * dt
        elif self.keyh[key.S]:
            self.y -= self.walk_speed * dt

        # Only set the animation once a key is pressed.
        if not self.walking:
            self.image = self.walk_anim

        # Determine if walking.
        if sum(self.keyh[k] for k in [key.W, key.A, key.S, key.D]):
            self.walking = True
        else:
            self.walking = False

        # Adjust sprite for not walking.
        if not self.walking:
            self.image = self.player_img
