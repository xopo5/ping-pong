from pygame import *
from button import Button
font.init()
stage = 'menu'
## https://idkru.pythonanywhere.com/code/vavoti

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

btn_start = Button(y = 200, width=150,height=40,text = 'Начать игру',font_size = 26)
btn_credits = Button(y = 250, width=150,height=40,text = 'Разработчики',font_size = 26)
btn_exit = Button(y = 300, width=150,height=40,text = 'Выход',font_size = 26)
btn_continue = Button(y=200,width=150,height=40,text='Продолжить',font_size = 26)
btn_to_menu = Button(y=250,width=150,height=40,text='Вернуться в меню',font_size=16)
btn_restart = Button(y=300,width=150,height=40,text='Рестарт',font_size=26)

dx =3 
dy=3
def restart():
    global player1,player2,ball
    player1 = Player('playersprite.png',10,HEIGHT/2+-80,40,120,5,K_w,K_s)
    player2 = Player('playersprite.png',500,HEIGHT/2-80,40,120,5,K_UP,K_DOWN)
    ball = Ball('ball.png',240,HEIGHT/4,50,50,5)
def game():
    mw.fill(BG_COLOR)
    player1.update()
    player2.update()
    player1.reset()
    player2.reset()
    ball.update()
    ball.player_collide(player1)
    ball.player_collide(player2)
    ball.reset()
def menu(events):
    global stage
    mw.fill(BG_COLOR)
    btn_start.update(events)
    btn_credits.update(events)
    btn_exit.update(events)
    btn_start.draw(mw)
    btn_credits.draw(mw)
    btn_exit.draw(mw)
    if btn_exit.is_clicked(events):
        stage = 'off'
    if btn_start.is_clicked(events):
        stage = 'game'
def pause(events):
    mw.fill(BG_COLOR)
    btn_continue.update(events)
    btn_to_menu.update(events)
    btn_to_menu.draw(mw)
    btn_continue.draw(mw)
    global stage
    if btn_continue.is_clicked(events):
        
        stage = 'game'
    if btn_to_menu.is_clicked(events):
        restart()
        stage = "menu"
def check_game_status():
    global stage
    if ball.rect.x < -ball.rect.width:
        stage = '2 win'
    if ball.rect.x > WIDTH:
        stage = '1 win'
def win_screen(events):
    global stage
    if stage == '2 win':
        print('Второй игрок победил')
    elif stage == '1 win':
        print('Первый игрок победил')
    btn_restart.update(events)
    btn_to_menu.update(events)
    btn_to_menu.draw(mw)
    btn_restart.draw(mw)
    if btn_restart.is_clicked(events):
        restart()
        stage = 'game'
    if btn_to_menu.is_clicked(events):
        stage = 'menu'
while stage!= 'off':
    events = event.get()
    for e in events:
        if e.type == QUIT:
            stage = 'off'
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                stage = 'pause'
    if stage == 'menu':
        menu(events)
    elif stage == 'game':
        game()
        check_game_status()
    elif stage == 'pause':
        pause(events)
    elif stage == '2 win' or stage == '1 win':
        win_screen(events)
    
    display.update()
    clock.tick(FPS)
