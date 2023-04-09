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
        if keys[self.key_up] and HEIGHT - self.rect.y<460:
            self.rect.y -= self.speed
        if keys[self.key_down] and HEIGHT - self.rect.y>140:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, sprite_image, x=0, y=0, width=50, height=50, speed=5):
        super().__init__(sprite_image, x, y, width, height)
        self.dx = speed
        self.dy = speed
    def update(self):
        if self.rect.y < 50 or self.rect.y > 430:
            self.dy *= -1
        self.rect.x += self.dx
        self.rect.y += self.dy

    def player_collide(self, player):
        if sprite.collide_rect(self, player):
            self.dx *= -1



BG_COLOR = (190, 190, 190)
WIDTH,HEIGHT = 600, 480
FPS = 60

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Пинг-Понг')
mw.fill(BG_COLOR)
clock = time.Clock()

player1 = Player('playersprite.png',10,HEIGHT/2+-80,40,120,5,K_w,K_s)
player2 = Player('playersprite.png',500,HEIGHT/2-80,40,120,5,K_UP,K_DOWN)
ball = Ball('ball.png',240,HEIGHT/4,50,50,5)
run = True

dx =3 
dy=3
while run:
    mw.fill(BG_COLOR)
    player1.update()
    player2.update()
    player1.reset()
    player2.reset()
    ball.update()
    ball.player_collide(player1)
    ball.player_collide(player2)
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
   
    
    display.update()
    clock.tick(FPS)
