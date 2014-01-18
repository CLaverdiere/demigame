import pyglet
import resource, i_sprite

class Bullet(i_sprite.ISprite):
    def __init__(self, name="Pistol bullet",
                       bullet_img=resource.blt_pistol_img,
                       *args,
                       **kwargs):
        super(Bullet, self).__init__(img=bullet_img, *args, **kwargs)
        self.name = name
        self.bullet_img = bullet_img
