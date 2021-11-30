import const
import pygame, players

class Ghost():
    def __init__(self):
        self.pos = [0, 0]
        self.colide_pos = self.pos
        self.size = (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))
        self.colide_size = self.size
        self.speed = [0, 0]
        self.base_speed = 2
        self.looking = [False, False, False, False] #up, down, left, right
        self.path = "./images/ghost/"
        self.images = {"diagonal_0": {"img": pygame.image.load(self.path+"diagonal_0.png"), "rel_pos": (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2)), "rel_size":(int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))},
        "diagonal_1": {"img": pygame.image.load(self.path+"diagonal_1.png"), "rel_pos": (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2)), "rel_size":(int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))},
        "diagonal_2": {"img": pygame.image.load(self.path+"diagonal_0.png"), "rel_pos": (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2)), "rel_size":(int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))},
        "diagonal_3": {"img": pygame.image.load(self.path+"diagonal_1.png"), "rel_pos": (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2)), "rel_size":(int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))},
        "horizontal_0": {"img": pygame.image.load(self.path+"horizontal_0.png"), "rel_pos": (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2)), "rel_size":(int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))},
        "horizontal_1": {"img": pygame.image.load(self.path+"horizontal_1.png"), "rel_pos": (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2)), "rel_size":(int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))},
        "horizontal_2": {"img": pygame.image.load(self.path+"horizontal_0.png"), "rel_pos": (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2)), "rel_size":(int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))},
        "horizontal_3": {"img": pygame.image.load(self.path+"horizontal_1.png"), "rel_pos": (int(const.BASE_SIZE/2), int(const.BASE_SIZE/2)), "rel_size":(int(const.BASE_SIZE/2), int(const.BASE_SIZE/2))}}
        
        self.img_idx = 0

    def display(self, screen, tick:int):
        img = pygame.image.load(self.path+"ghost.png")
        img = pygame.transform.scale(img, self.size)
        screen.blit(img, (self.pos[0], self.pos[1]))
        #pygame.draw.rect(screen, (0, 255, 255), (self.pos[0], self.pos[1], self.size[1], self.size[1]))
        return screen

    def move(self, player:players.Player):
        self.move_axis(player, 0)
        self.move_axis(player, 1)
        #print(self.pos)

    def move_axis(self, player:players.Player, axis:int):
            
        if player.colide_pos[axis] > self.colide_pos[axis]:
            other_axis = 0 if axis == 1 else 1
            self.speed[axis] = self.base_speed
            if self.colide_pos[axis]+self.colide_size[axis] > player.colide_pos[axis] and self.colide_pos[axis] < player.colide_pos[axis]+player.colide_size[axis]:
                if axis == 0:
                    self.looking[0] = False
                    self.looking[1] = False
                    self.looking[2] = False
                    self.looking[3] = True
                else:
                    self.looking[0] = False
                    self.looking[1] = True
                    self.looking[2] = False
                    self.looking[3] = False

            else:
                if axis == 0:
                    self.looking[3] = True
                    self.looking[1] = False
                else:
                    self.looking[2] = True
                    self.looking[0] = False
        else:
            self.speed[axis] = -self.base_speed
            if self.colide_pos[axis]+self.colide_size[axis] > player.colide_pos[axis] and self.colide_pos[axis] < player.colide_pos[axis]+player.colide_size[axis]:
                if axis == 0:
                    self.looking[0] = False
                    self.looking[1] = False
                    self.looking[2] = True
                    self.looking[3] = False
                else:
                    self.looking[0] = True
                    self.looking[1] = False
                    self.looking[2] = False
                    self.looking[3] = False
            
            else:
                if axis == 0:
                    self.looking[3] = False
                    self.looking[1] = True
                else:
                    self.looking[2] = False
                    self.looking[0] = True

        self.pos[axis] += self.speed[axis]
