import pyglet
import resource
from pyglet.window import key

class Player(pyglet.sprite.Sprite):
    def __init__(self, lives=3,
                       name="Default Player",
                       walk_speed=250,
                       mass=75,
                       player_img=resource.ponyo_img,
                       *args,
                       **kwargs):
        super(Player, self).__init__(img=player_img, *args, **kwargs)
        self.lives = lives
        self.name = name
        self.walk_speed = walk_speed
        self.mass = mass
        self.player_img = player_img

        # Key handling
        self.keyh = key.KeyStateHandler()
        self.event_handlers = [self, self.keyh]

        # Movement
        self.walking = False

    def update(self, dt):

        # Movement controls, WASD.
        if self.keyh[key.A]:
            self.x -= self.walk_speed * dt
            if not self.walking:
                self.image = resource.demigod_animstep
                self.walking = True
        elif self.keyh[key.D]:
            self.x += self.walk_speed * dt
            if not self.walking:
                self.image = resource.demigod_animstep
                self.walking = True
        else:
            self.image = resource.demigod_img
            self.walking = False
            
