import pygame
from enum import Enum

pygame.init()

w = 500
h = 480
win = pygame.display.set_mode((w, h))
pygame.display.set_caption("First Game")

right_image_names = ['R1.png','R2.png','R3.png','R4.png','R5.png','R6.png','R7.png','R8.png','R9.png']
left_image_names = ['L1.png','L2.png','L3.png','L4.png','L5.png','L6.png','L7.png','L8.png','L9.png']
walkRight = []
walkLeft = []
for image_name in right_image_names: 
    walkRight.append(pygame.image.load('Pygame-Images/Game/'+ image_name))
for image_name in left_image_names: 
    walkLeft.append(pygame.image.load('Pygame-Images/Game/'+ image_name))

standing_char = pygame.image.load('Pygame-Images/Game/'+'standing.png')

class Pose(Enum):
    standing = 0
    facing_right = 1
    facing_left = 2

class Borders:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

class Character():
    def __init__(self, color, pos, width, height, borders):
        self.pos = pos
        self.width = width
        self.height = height
        self.horizontal_velocity = 5
        self.color = color
        self.borders = borders
        self.vertical_velocity = 0
        self.acceleration = 10
        self.period = 0.1

        self.pose = Pose.standing
        self.walkCount = 0

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
        
    def draw(self):
        global walkRight, walkLeft, standing_char
        self.walkCount = self.walkCount % 27

        if self.pose == Pose.facing_left:
            win.blit(walkLeft[self.walkCount//3], (self.pos.x, self.pos.y))
            self.walkCount += 1
        elif self.pose == Pose.facing_right:
            win.blit(walkRight[self.walkCount//3], (self.pos.x, self.pos.y))
            self.walkCount += 1
        else:
            win.blit(standing_char, (self.pos.x, self.pos.y))
        
        pygame.display.update()


class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Dir(Enum):
    Left=0
    Right=1
    Up=2
    Down=3
    
character_borders = Borders(0, w, 0, h-20)
character = Character((255, 0, 0), Position(0, 500-60), 40, 60, character_borders)

class Game():
    def __init__(self, square):
        self.s = square
        self.run = True

        self.bg_img = pygame.image.load('Pygame-Images/Game/' + 'bg.jpg')


    def listen_for_key_press(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.s.move_horizontally(Dir.Left)
        elif keys[pygame.K_RIGHT]:
            self.s.move_horizontally(Dir.Right)
        else:
            self.s.pose = Pose.standing
        if keys[pygame.K_SPACE]:
            self.s.jump()

        self.s.move_vertically()

    def listen_for_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def draw_background(self):
        win.blit(self.bg_img, (0,0))

    def redraw_window(self):
        self.draw_background()
        self.s.draw()
        pygame.display.update()
        

run = True
game = Game(character)
background_color = (0,0,0)
clock = pygame.time.Clock()
while game.run:
    clock.tick(27)


    game.listen_for_quit()
    game.listen_for_key_press()
    game.redraw_window()

