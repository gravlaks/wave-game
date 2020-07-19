import pygame
class Enemy:
    walkRight = [pygame.image.load('Pygame-Images/Game/R%sE.png' % frame) for frame in range(1, 12)]
    walkLeft = [pygame.image.load('Pygame-Images/Game/L%sE.png' % frame) for frame in range(1, 12)]

    def __init__(self, pos, width, height, end):
        self.pos = pos 
        self.width = width 
        self.height = height
        self.end = end
        self.path = [self.pos.x, self.end]
        self.walkCount = 0
        self.vel = 3

    def is_moving_right(self):
        return self.vel>0

    def draw(self, win):
        if self.is_moving_right():
            win.blit(self.walkRight[self.walkCount//3], (self.pos.x, self.pos.y))
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.pos.x, self.pos.y))

    def change_direction(self):
        self.vel *= -1
        self.walkCount = 0

    def move(self):
        if self.vel > 0:
            if self.pos.x + self.vel > self.path[1]:
                self.change_direction() 
        else:
            if self.pos.x + self.vel < self.path[0]:
                self.change_direction()
        self.pos.x = self.pos.x+self.vel
        self.walkCount += 1
        self.walkCount = self.walkCount %33
            

