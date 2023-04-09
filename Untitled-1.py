from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50, speed=5, key_up=K_w, key_down=K_s):
        super().__init__(sprite_image, x, y, width, height)
        self.speed = speed
        self.key_down = key_down
        self.key_up = key_up
    def update(self):
        keys = key.get_pressed()
        if keys[self.key_up]:
            self.rect.y -= self.speed
        if keys[self.key_down]:
            self.rect.y += self.speed
BG_COLOR = (220,100,220)
WIDTH,HEIGHT = 600, 480
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Пинг-Понг')
mw.fill(BG_COLOR)
clock = time.Clock()

run = True
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
    
    display.update()
    clock.tick(FPS)
