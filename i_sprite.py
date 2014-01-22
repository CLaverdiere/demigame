# Interactive Sprite class.

import pyglet
import random

class ISprite(pyglet.sprite.Sprite):
    def __init__(self, 
                 disp_x=0, 
                 disp_y=0, 
                 disp_r=0, 
                 *args, **kwargs):
        super(ISprite, self,).__init__(*args, **kwargs)

        # Keep track of all events happening
        self.event_handlers = []

        # This is a list of functions for the sprite to
        #   carry out each frame.
        self.duty_list = []

        # Remove is when it's ready to actually be deleted from the batch.
        self.remove = False

        # Removing indicates the removal animation should activate.
        self.removing = False

        # Track sprite displacement so that environment objects can move in
        #   response to the player, while keeping the player centered.
        self.disp_x = disp_x or self.x
        self.disp_y = disp_y or self.y
        self.disp_r = disp_r or self.rotation  # Rotational displacement

    def add_duty(self, func):
        self.duty_list.append(func)

    def check_bounds(self):
        pass

    def update(self, dt, player):
        # if self.removing:
        #     self.opacity -= 5
        # if self.opacity < 0:
        #     self.remove = True

        # for func in self.duty_list:
        #     func(self)

        # Update sprite positions relative to player.
        self.image.anchor_x = self.disp_x + player.disp_x
        self.image.anchor_y = self.disp_y + player.disp_y
        self.rotation = self.disp_r + player.disp_r

    def collides(self, other):
        w_max = (self.width / 2) + (other.width / 2)
        h_max = (self.height / 2) + (other.height / 2)

        w_dist = abs(abs(self.disp_x) - abs(other.disp_x))
        h_dist = abs(abs(self.disp_y) - abs(other.disp_y))

        print self, other, 
        print w_dist, h_dist
        print w_max, h_max

        if w_dist < w_max and h_dist < h_max:
            return True
        else:
            return False

    def handle_collision(self, other):
        pass

    def waddle(self):
        if not random.randint(1,7) % 7:
            self.x += random.randint(-3,3)
