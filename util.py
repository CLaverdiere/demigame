import math

def distance(x1, x2, y1, y2):
    return math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2 )

def center_body(body):
    body.anchor_x = body.width / 2
    body.anchor_y = body.height / 2
