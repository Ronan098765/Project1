from pygame import *
from random import randint
from time import time as timer

mixer.init()
mixer.music.load('Music_fon.mp3')
mixer.music.play()
mixer.music.stop()
pick_money = mixer.Sound('Pick_money.ogg')
music_win = mixer.Sound('Music_win.ogg')
music_lose = mixer.Sound('Music_lose.ogg')
pick_mush = mixer.Sound('Pick_mush.ogg')
pick_mush_evil = mixer.Sound('Pick_mush_evil.ogg')
font.init()
font2 = font.SysFont('Arial', 36)
win = font2.render('You win', True, (30, 89, 69))
lose = font2.render('You lose', True, (144, 0,32 ))

img_mush_evil = 'Mush_evil.xcf'
img_mush = 'Mushroom.xcf'
img_back = 'Fon.jpg'
img_bul_R = 'Bullet_R.xcf'
img_player = 'player1.xcf'
img_player1 = 'player1.xcf'
img_player2 = 'player2.xcf'
img_player3 = 'player3.xcf'
img_player4 = 'player4.xcf'
img_player5 = 'player5.xcf'
img_player6 = 'player6.xcf'
img_bul_L = 'Bullet_L.xcf'
img_money = 'Money.xcf'
img_bomb = 'bomb.xcf'
explouse = 'explouse.png'
img_bomb0 = 'bomb.xcf'

money_num = 0
heart_player = 100

player_xx = 350
player_yy = 250

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
    def update(self):
        global player_xx, player_yy
        
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            player_yy -= self.speed
        if keys[K_s] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
            player_yy += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            player_xx -= self.speed
        if keys[K_d] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
            player_xx += self.speed
        
    
class Bullet(GameSprite):
    def update(self):
        self.rect.x -= self.speed
        global bullets_num
        if self.rect.x < 0:
            self.kill()
            bullet = Bullet(img_bul_L, 700, randint(50, win_height - 50), 20, 20, randint(5,15))
            bullets.add(bullet)

class Bullet_r(GameSprite):
    def update(self):
        self.rect.x += self.speed
        global bullets_num
        if self.rect.x > 700:
            self.kill()
            bullet_r = Bullet_r(img_bul_R, 0, randint(50, win_height - 50), 20, 20, randint(5,15))
            bullets_r.add(bullet_r)  
            
class Bomb(GameSprite):
    def update(self):
        pass
            
            
            

class Money(GameSprite):
    def update(self):
        pass

class Mushroom(GameSprite):
    def update(self):
        pass



win_width = 700
win_height = 500
display.set_caption('Game')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

player = Player(img_player, 350, 250, 80, 60, 10)

bullets = sprite.Group()
bullets_r = sprite.Group()
moneys = sprite.Group()
exps = sprite.Group()

time1 = 0
for i in range(1, 6):
    bullet = Bullet(img_bul_L, 700, randint(50, win_height - 50), 20, 20, randint(5,15))
    bullets.add(bullet)
for i in range(1, 6):
    bullet_r = Bullet_r(img_bul_R, 0, randint(50, win_height - 50), 20, 20, randint(5,15))
    bullets_r.add(bullet_r) 
    
for i in range(0, 7):
    money = Money(img_money, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)
    moneys.add(money)

mushroom = Mushroom(img_mush, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)
mush_evil = Mushroom(img_mush_evil, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)
finish = False
game = True

bomb = Bomb(img_bomb, 200, 1000, 30, 30 , 0)

time2 = 0
time3 = 0
ex_x = 1000
ex_y = 1000

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(player, mushroom):
        pick_mush.play()
        heart_player += 1
        mushroom.kill()
        mushroom = Mushroom(img_mush, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)

    if sprite.collide_rect(player, mush_evil):
        pick_mush_evil.play()
        heart_player -= 1
        mush_evil.kill()
        mush_evil = Mushroom(img_mush_evil, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)

    if not finish:
        window.blit(background,(0, 0))
        score = font2.render('Score:' + str(money_num), 1, (255, 255, 255))
        window.blit(score, (10, 10))
        hearts = font2.render('Hp:' + str(heart_player), 1, (168, 228, 160))
        window.blit(hearts, (600, 10))

        if sprite.spritecollide(player, moneys, True):
            money_num += 1 
            pick_money.play()
            money = Money(img_money, randint(50, win_width - 50), randint(50, win_height - 50), 25, 25, 0)
            moneys.add(money)
            
        if sprite.spritecollide(player, bullets, True):
            heart_player -= 1
            bullet = Bullet(img_bul_L, 700, randint(50, win_height - 50), 20, 20, randint(5,15))
            bullets.add(bullet)
            pick_mush_evil.play()
            
        if sprite.spritecollide(player, bullets_r, True):
            heart_player -= 1
            bullet_r = Bullet_r(img_bul_R, 0, randint(50, win_height - 50), 20, 20, randint(5,15))
            bullets_r.add(bullet_r) 
            pick_mush_evil.play()
            
        if heart_player <= 0:
            finish = True
            window.blit(lose, (290, 220))
            music_lose.play()

        if money_num >= 50:
            finish = True
            window.blit(win, (290, 220))
            music_win.play()
        
        time1 += 1
        if time1 <= 2:
            img_player = img_player1
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)
        elif time1 <= 4:
            img_player = img_player2
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)
        elif time1 <= 6:
            img_player = img_player3
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)
        elif time1 <= 8:
            img_player = img_player4
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)
        elif time1 <= 10:
            img_player = img_player5
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)
        elif time1 <= 12:
            img_player = img_player6
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)
        elif time1 <= 14:
            img_player = img_player5
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)  
        elif time1 <= 16:
            img_player = img_player4
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)  
        elif time1 <= 18:
            img_player = img_player3
            player.kill()
            player = Player(img_player, player_xx, player_yy, 90, 60, 10)
        else:
            time1 = 0
        
        time2 += 1
        
        bomb_x = randint(50, win_width - 50)
        bomb_y = randint(50, win_height - 50)
        
        if time2 >= 30:
            bomb.kill()
            bomb = Bomb(img_bomb, bomb_x, bomb_y, 30, 30, 0)
            time2 = 0
            ex_x = bomb_x - 140
            ex_y = bomb_y - 140
        
        if time2 < 30 and time2 >= 20:
            time3 += 1
        if time3 >= 10:
            bomb.kill()
            bomb = Bomb(explouse, ex_x, ex_y, 300, 300, 0)
            bomb.add(exps)
            time3 = 0
            

        if sprite.spritecollide(player, exps, True):
            pick_mush_evil.play()
            heart_player -= 5
            bomb.kill()
        
        
        bomb.update()
        bomb.reset()
        player.update()
        player.reset()
        bullets.update()
        bullets_r.update()
        bullets_r.draw(window)
        bullets.draw(window)
        moneys.draw(window)
        mushroom.reset()
        mush_evil.reset()
        display.update()
    time.delay(60)
