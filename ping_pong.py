from pygame import *
init()
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("стол.jpg"), (win_width, win_height))

font.init()
font_score = font.Font(None, 36)

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

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y, 0)
        self.speed_x = speed_x + 1
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0 or self.rect.y >= win_height - 20:
            self.speed_y = -self.speed_y
            
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ping = Player("ракетка1.png", 20, 200, 20, 100, 10)
pong = Player("ракетка2.png", 560, 200, 20, 100, 10)
ball = Ball("мяч.png", 300, 250, 20, 20, 3, 3)

score_left = 0
score_right = 0
win_score = 5
end = False
win = False


clock = time.Clock()

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and end:
            if e.key == K_r:
                score_left = 0
                score_right = 0
                end = False
                win = False
                winner_text = ""
                ball.rect.x = win_width // 2
                ball.rect.y = win_height // 2
                ball.speed_x = 3
                ball.speed_y = 3
                ping.rect.y = 200
                pong.rect.y = 200

                ball.rect.x = win_width // 2
                ball.rect.y = win_height // 2
                ball.speed_x = 3
                ball.speed_y = 3
                ping.rect.y = 200
                pong.rect.y = 200

    if not end:

        window.blit(background, (0, 0))

        ping.update_l()
        pong.update_r()
        ball.update()

        if sprite.collide_rect(ping, ball):
            ball.speed_x = -ball.speed_x + 0.5

        if sprite.collide_rect(pong, ball):
            ball.speed_x = -ball.speed_x - 0.5

        if ball.rect.x < 0:
            score_right += 1
            ball.rect.x = win_width // 2
            ball.rect.y = win_height // 2
            ball.speed_x = 3
            ball.speed_y = 3
            
        if ball.rect.x > win_width:
            score_left += 1
            ball.rect.x = win_width // 2
            ball.rect.y = win_height // 2
            ball.speed_x = -3
            ball.speed_y = 3
        
        if score_left >= win_score:
            end = True
            win = True
            winner_text = "Левый игрок победил!"
        elif score_right >= win_score:
            end = True
            win = True
            winner_text = "Правый игрок победил!"

    else:
        if win:
            win_text = font_score.render(winner_text, True, (0, 255, 0))
            window.blit(win_text, (win_width // 2 - win_text.get_width() // 2, win_height // 2 - 50))
            restart_text = font_score.render("Нажмите R для новой игры", True, (255, 0, 0))
            window.blit(restart_text, (win_width // 2 - restart_text.get_width() // 2, win_height // 2 + 30))

    ping.reset()
    pong.reset()
    ball.reset()

    display.update()
    clock.tick(60)
