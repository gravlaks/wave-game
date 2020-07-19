import pygame
from enum import Enum
from Position import Position
from Pose import Pose
from Enemy import Enemy





class Borders:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

class Images:
    def __init__(self):
        self.walkRight = []
        self.walkLeft = []

    
        self.right_image_names = ['R1.png','R2.png','R3.png','R4.png','R5.png','R6.png','R7.png','R8.png','R9.png']
        self.left_image_names = ['L1.png','L2.png','L3.png','L4.png','L5.png','L6.png','L7.png','L8.png','L9.png']
        for image_name in self.right_image_names: 
            self.walkRight.append(pygame.image.load('Pygame-Images/Game/'+ image_name))
        for image_name in self.left_image_names: 
            self.walkLeft.append(pygame.image.load('Pygame-Images/Game/'+ image_name))

        self.standing_char = pygame.image.load('Pygame-Images/Game/'+'standing.png')

class Character():
    def __init__(self, color, pos, width, height, borders, images):
        self.standing = True    
        self.pos = pos
        self.width = width
        self.height = height
        self.horizontal_velocity = 5
        self.color = color
        self.borders = borders
        self.vertical_velocity = 0
        self.acceleration = 10
        self.period = 0.1

        self.walkCount = 0
        self.images = images
        self.pose = Pose.facing_right

    def move_left(self):
        self.pos.x -= min(self.horizontal_velocity,self.pos.x-self.borders.left)
    def move_right(self):
        self.pos.x += min(self.horizontal_velocity, self.borders.right-self.pos.x-self.width)

    def move_horizontally(self, direction):
        if direction == Dir.Left:
            self.pose = Pose.facing_left
            self.move_left()
        if direction == Dir.Right:
            self.pose = Pose.facing_right
            self.move_right()


    def move_vertically(self):
        self.vertical_velocity += self.acceleration*self.period
        self.pos.y += min(self.vertical_velocity, self.borders.bottom-self.pos.y-self.height)

    def jump(self):
        if self.pos.y >= self.borders.bottom - self.height:
            self.vertical_velocity = -10
        
    def draw(self, win):
        global walkRight, walkLeft, standing_char
        self.walkCount = self.walkCount % 27

        if not self.standing:
            if self.pose == Pose.facing_left:
                win.blit(self.images.walkLeft[self.walkCount//3], (self.pos.x, self.pos.y))
                self.walkCount += 1
            else:
                win.blit(self.images.walkRight[self.walkCount//3], (self.pos.x, self.pos.y))
                self.walkCount += 1
        else:
            if self.pose == Pose.facing_left:
                win.blit(self.images.walkLeft[0], (self.pos.x, self.pos.y))
            else:
                win.blit(self.images.walkRight[0], (self.pos.x, self.pos.y))
        
        pygame.display.update()

class Projectile():
    def __init__(self, pos, radius, color, facing):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8*facing.value

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.pos.x, self.pos.y), self.radius)

    def move(self):
        self.pos.x += self.vel

    def is_on_screen(self):
        return self.pos.x<500 and self.pos.x>0
class Dir(Enum):
    Left=0
    Right=1
    Up=2
    Down=3
    

class Game():
    def __init__(self, win):
        character_borders = Borders(0, w, 0, h-20)
        images = Images()
        self.character = Character((255, 0, 0), Position(0, w-60), 40, 60, character_borders, images)
        self.run = True
        self.win = win

        self.bg_img = pygame.image.load('Pygame-Images/Game/' + 'bg.jpg')

        self.bullets = []
        self.enemy = Enemy(Position(255, w-100), 40, 60, 420)


    def listen_for_key_press(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.character.move_horizontally(Dir.Left)
            self.character.standing = False
        elif keys[pygame.K_RIGHT]:
            self.character.move_horizontally(Dir.Right)
            self.character.standing = False
        else:
            self.character.standing=True
        if keys[pygame.K_UP]:
            self.character.jump()

        if keys[pygame.K_SPACE]:
            bullet_position = Position(int(self.character.pos.x+self.character.width//2), int(self.character.pos.y+self.character.height//2))
            self.bullets.append(Projectile(bullet_position, 2, (0, 0, 0), self.character.pose))

    
        self.character.move_vertically()
        for bullet in self.bullets:
            bullet.move()

        self.enemy.move()

    def listen_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def draw_background(self):
        win.blit(self.bg_img, (0,0))

    def redraw_window(self):
        self.draw_background()
        self.character.draw(self.win)

        for bullet in self.bullets:
            if bullet.is_on_screen():
                bullet.draw(self.win)

        self.enemy.draw(self.win)

        pygame.display.update()
        


pygame.init()

w = 500
h = 480

win = pygame.display.set_mode((w, h))
pygame.display.set_caption("First Game")

game = Game(win)

clock = pygame.time.Clock()
while game.run:
    clock.tick(27)


    game.listen_for_quit()
    game.listen_for_key_press()
    game.redraw_window()

