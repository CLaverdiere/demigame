import pyglet
import resource, i_sprite, util, weapon
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

        self.disp_x = 0
        self.disp_y = 0
        self.disp_r = 0

        self.lives = lives
        self.name = name
        self.walk_speed = walk_speed
        self.mass = mass
        self.player_img = player_img
        self.walk_anim = walk_anim
        self.holding_gun = False

        # Key handling
        self.keyh = key.KeyStateHandler()
        self.event_handlers = [self, self.keyh]

        # Movement
        self.walking = False
        self.mouse_angle = 0.0

    def on_mouse_motion(self, x, y, dx, dy):
        # Make our player face the mouse.
        #   Also make sure our x component isn't 0 to avoid division errors.
        self.disp_r += dx * .5

    def update(self, dt):
        # Movement controls, WASD.
        if self.keyh[key.A]:
            self.disp_x -= self.walk_speed * math.sin(math.radians(self.disp_r)) * dt
            self.disp_y += self.walk_speed * math.cos(math.radians(self.disp_r)) * dt
        elif self.keyh[key.D]:
            self.disp_x += self.walk_speed * math.sin(math.radians(self.disp_r)) * dt
            self.disp_y -= self.walk_speed * math.cos(math.radians(self.disp_r)) * dt
        if self.keyh[key.W]:
            self.disp_x += self.walk_speed * math.cos(math.radians(self.disp_r)) * dt
            self.disp_y += self.walk_speed * math.sin(math.radians(self.disp_r)) * dt
        elif self.keyh[key.S]:
            self.disp_x -= self.walk_speed * math.cos(math.radians(self.disp_r)) * dt / 2
            self.disp_y -= self.walk_speed * math.sin(math.radians(self.disp_r)) * dt / 2

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
            if self.holding_gun:
                self.image = resource.hero_img_pistol
            else:
                self.image = self.player_img

    def handle_collision(self, other):
        if isinstance(other, weapon.Weapon):
            self.holding_gun = True
            print "Picked up weapon!"
        else:
            pass

