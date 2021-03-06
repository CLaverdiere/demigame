import pyglet
import util

pyglet.resource.path = ['./res']
pyglet.resource.reindex()


# Player resources ---------------------------------------------------
demigod_img = pyglet.resource.image("demigod.png")
demigod_step1_img = pyglet.resource.image("demigod_step1.png")
demigod_step2_img = pyglet.resource.image("demigod_step2.png")
demigod_animstep = pyglet.image.Animation.from_image_sequence(
        [demigod_step1_img, demigod_step2_img], 0.2, True)

hero_img = pyglet.resource.image("player_stand.png")
hero_img_pistol = pyglet.resource.image("player_stand_pistol.png")
hero_walk1_img = pyglet.resource.image("player_walk1.png")
hero_walk2_img = pyglet.resource.image("player_walk2.png")
hero_walk1_img_flip = pyglet.resource.image("player_walk1.png", flip_x=True)
hero_walk2_img_flip = pyglet.resource.image("player_walk2.png", flip_x=True)
hero_animwalk = pyglet.image.Animation.from_image_sequence(
        [hero_walk1_img, hero_walk2_img, hero_walk2_img_flip, hero_walk1_img_flip], 0.2, True)

ponyo_img = pyglet.resource.image("ponyo.png")


# Environment resources
tree_bg_img = pyglet.resource.image("tree_bg.png")
desert_bg_img = pyglet.resource.image("desert_bg.png")


# Weapon resources ---------------------------------------------------
pistol_img = pyglet.resource.image("pistol.png")
util.center_body(pistol_img)

blt_pistol_img = pyglet.resource.image("blt_pistol.png")
util.center_body(blt_pistol_img)


# List of all image resources.
all_images = [ demigod_img,
               demigod_step1_img,
               demigod_step2_img,
               hero_img,
               hero_walk1_img,
               hero_walk1_img_flip,
               hero_walk2_img,
               hero_walk2_img_flip,
               hero_img_pistol,
               tree_bg_img,
               desert_bg_img,
               pistol_img,
               blt_pistol_img ]

for image in all_images:
    util.center_body(image)
