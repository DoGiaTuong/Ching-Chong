from pygame import *

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image, player_x,player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset():
        window.blit(self.image, (self.rect.x,self.rect.y))
     
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > win_height -80:
            self.rect.y += self.speed


back = (200,178,34)
win_height = 500
win_width = 600
window = display.set_mode((win_width,win_height))
window.fill(back)

#game object
image_1 = ""
image_2 = ""
ball_image = ""



paddle_1 = Player(image_1, 30,200,4,50,150)
paddle_2 = Player(image_2, 520,200,4,50,150)
ball = GameSprite(ball_image, 200,200,4,50,50)






#game loop

game = True
finish = False
clock = time.Clock()
FPS = 60


while game:
    for e in event.type():
        if e.type == QUIT:
            game = False

    


