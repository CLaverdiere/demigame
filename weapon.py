import pyglet
import resource, i_sprite, player

class Weapon(i_sprite.ISprite):
    def __init__(self, name="Pistol",
                       fire_speed=500,
                       weapon_img=resource.pistol_img,
                       bullet_img=resource.blt_pistol_img,
                       *args,
                       **kwargs):
        super(Weapon, self).__init__(img=weapon_img, *args, **kwargs)
        self.name = name
        self.fire_speed = fire_speed
        self.weapon_img = weapon_img
        self.bullet_img = bullet_img
        self.scale = 0.5
        self.event_handlers = []

    def handle_collision(self, other):
        if isinstance(other, player.Player):
            self.remove = True
        else:
            pass
