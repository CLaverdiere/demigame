# Interactive Sprite class.

import pyglet
import random

class ISprite(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(ISprite, self,).__init__(*args, **kwargs)
        self.event_handlers = []

        # This is a list of functions for the sprite to
        #   carry out each frame.
        self.duty_list = []

    def add_duty(self, func):
        self.duty_list.append(func)

    def check_bounds(self):
        pass

    def update(self, dt):
        for func in self.duty_list:
            func(self)

    def waddle(self):
        if not random.randint(1,7) % 7:
            self.x += random.randint(-3,3)
