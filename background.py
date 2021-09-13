import pygame
import const

class Background():
    def __init__(self, pos):
        self.pos = pos
        self.size = (const.BASE_SIZE*4, const.BASE_SIZE*4)
        #self.screen_pos = []


    def display(self, screen):
        img = pygame.image.load("./images/background/brick_bkg.png").convert()
        img = pygame.transform.scale(img, self.size)
        screen.blit(img, (self.pos[0], self.pos[1]))

class background_object():
    def __init__(self, pos, object):
        if object == "closed_door":
            self.pos = pos
            self.size = (const.BASE_SIZE, const.BASE_SIZE*2)
            self.path = "./images/background/closed_door.png"
        if object == "closed_prison":
            self.pos = pos
            self.size = (const.BASE_SIZE, const.BASE_SIZE*2)
            self.path = "./images/background/closed_prison.png"
        if object == "opened_prison":
            self.pos = pos
            self.size = (const.BASE_SIZE, const.BASE_SIZE*2)
            self.path = "./images/background/opened_prison.png"
        
    def display(self, screen):
        img = pygame.image.load(self.path).convert()
        img = pygame.transform.scale(img, self.size)
        screen.blit(img, (self.pos[0], self.pos[1]))

class health_bar():
    def __init__(self):
        self.pos = (8, 8)
        self.size = (256, 32)

    def display(self, screen, health):
        red_size = 8*health
        pygame.draw.rect(screen, (43, 128, 64), (self.pos[0]+4, self.pos[1]+4, health*8-8, self.size[1]-8))
        pygame.draw.rect(screen, (128, 32, 32), (self.pos[0]+4+health*8-8, self.pos[1]+4, 256-health*8, self.size[1]-8))

        img = pygame.image.load("./images/other/life_bar.png")
        img = pygame.transform.scale(img, self.size)
        screen.blit(img, self.pos)