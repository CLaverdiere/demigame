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
        if x != self.x:
            self.mouse_angle = math.degrees( math.atan2 ( (y - self.y) , (x - self.x) ))
            self.rotation = -(self.mouse_angle + 90)

    def update(self, dt):
        # Movement controls, WASD.
        if self.keyh[key.A]:
            self.x -= self.walk_speed * math.sin(math.radians(self.mouse_angle)) * dt
            self.y += self.walk_speed * math.cos(math.radians(self.mouse_angle)) * dt
        elif self.keyh[key.D]:
            self.x += self.walk_speed * math.sin(math.radians(self.mouse_angle)) * dt
            self.y -= self.walk_speed * math.cos(math.radians(self.mouse_angle)) * dt
        if self.keyh[key.W]:
            self.x += self.walk_speed * math.cos(math.radians(self.mouse_angle)) * dt
            self.y += self.walk_speed * math.sin(math.radians(self.mouse_angle)) * dt
        elif self.keyh[key.S]:
            self.x -= self.walk_speed * math.cos(math.radians(self.mouse_angle)) * dt / 2
            self.y -= self.walk_speed * math.sin(math.radians(self.mouse_angle)) * dt / 2

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

