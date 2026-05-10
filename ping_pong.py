from pygame import *

win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill((200, 255, 255))

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
           self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:  
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__(player_image, player_x, player_y, player_speed, size_x, size_y)
        self.direction = 'left'

    def update(self):
        if self.rect.x <= 435:
            self.direction = 'right'
        if self.rect.x > 560 - 50:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

ping = Player(("ракетка1.jpg"), 20, 430, 20, 100, 10)
pong = Player(("ракетка1.jpg"), 560, 100, 20, 100, 10)
ball = Enemy(("мяч.jpg"), 560, 250, 5, 20, 20)
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    ball.update()
    ping.update_l()
    pong.update_r()
    ping.reset()
    pong.reset()
    clock.tick(60)