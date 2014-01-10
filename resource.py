import pyglet

pyglet.resource.path = ['./res']
pyglet.resource.reindex()

demigod_img = pyglet.resource.image("demigod.png")
demigod_step1_img = pyglet.resource.image("demigod_step1.png")
demigod_step2_img = pyglet.resource.image("demigod_step2.png")
demigod_animstep = pyglet.image.Animation.from_image_sequence(
        [demigod_step1_img, demigod_step2_img], 0.2, True)
ponyo_img = pyglet.resource.image("ponyo.png")
