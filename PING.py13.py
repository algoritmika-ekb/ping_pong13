from pygame import *

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
      keys = key.get_pressed()
      if keys[K_UP] and self.rect.x > 5:
          self.rect.x -= self.speed
      if keys[K_DOWN] and self.rect.x < win_width - 80:
          self.rect.x += self.speed
  def fire(self):
      bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
      bullets.add(bullet)

  def update(self):
      keys = key.get_pressed()
      if keys[K_w] and self.rect.x > 5:
          self.rect.x -= self.speed
      if keys[K_s] and self.rect.x < win_width - 80:
          self.rect.x += self.speed
  def fire(self):

back = (200, 255, 255)
window = display.set_mode((600, 500))
window.fill(back)    

game = True
finish = False
clock = clock.Clock()
Fps = 60


raсket1 = player('racket.png',  30, 200, 4, 50, 150)
raсket2 = player('racket.png',  520, 200, 4, 50, 150)
raсket3 = player('tenis_ball.png',  200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose 1 = font.render("PLAYER 1 LOSE!",  True, (180,0,0))
lose 2 = font.render("PLAYER 2 LOSE!",  True, (180,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if finish != True
            window.fill(back)
            racket1 = update_1()
            raсket2 = update_2()
            ball.rect.x += speed_x
            ball.rect.y += speed_y

            racket1.reset()
            racket2.reset()
            ball.reset()
        display.update()
        clock.tick(FPS)
