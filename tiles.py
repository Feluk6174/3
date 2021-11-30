import pygame, random
import const

class Brick_block():
    def __init__(self, pos:list):
        self.pos = pos
        self.size = (const.BASE_SIZE, const.BASE_SIZE)
        #self.screen_pos = []
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.x_flip = True if random.randint(0, 1) == 0 else False
        self.y_flip = True if random.randint(0, 1) == 0 else False

    def display(self, screen):
        img = pygame.image.load("./images/obstacles/brick.png").convert()
        img = pygame.transform.scale(img, self.size)
        img = pygame.transform.flip(img, self.x_flip, False)
        screen.blit(img, (self.pos[0], self.pos[1]))

class Exit():
    def __init__(self, dispaly:bool=False):
        pass