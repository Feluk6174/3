import const
import pygame

class Ghost():
    def __init__(self):
        self.pos = [0, 0]
        self.colide_pos = self.pos
        self.size = (const.BASE_SIZE, const.BASE_SIZE)
        self.colide_size = self.size
        self.speed = [0, 0]
        self.base_speed = 1
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

    def display(self, screen, tick):
        if self.looking.count(True) == 2:
            img = self.images["diagonal_"+str(self.img_idx)]["img"]
            if self.img_idx == 3:
                img = pygame.transform.rotate(img, 270)
                img = pygame.transform.flip(img, True, False)

            if self.looking[0] and self.looking[2]:
                img = pygame.transform.rotate(img, 180)
            elif self.looking[0] and self.looking[3]:
                img = pygame.transform.rotate(img, 90)
            elif self.looking[1] and self.looking[2]:
                img = pygame.transform.rotate(img, 270)
            
            img = pygame.transform.scale(img, self.size)
            screen.blit(img, self.colide_pos)

            if tick % 10 == 0:
                self.img_idx = self.img_idx + 1 if not self.img_idx == 3 else 0

        else:
            img = self.images["horizontal_"+str(self.img_idx)]["img"]
            if self.img_idx == 1 or self.img_idx == 3:
                img = pygame.transform.rotate(img, 270)
                img = pygame.transform.flip(img, True, False)

            if not self.speed[0] == 0 and self.speed[1] == 0:
                if self.speed[0] < 0:
                    pygame.transform.rotate(img, 180)

            else:
                if self.speed[1] < 0:
                    pygame.transform.rotate(img, 270)
                else:
                    pygame.transform.rotate(img, 90)
            
            img = pygame.transform.scale(img, self.size)
            screen.blit(img, self.colide_pos)

            if tick % 10 == 0:
                self.img_idx = self.img_idx + 1 if not self.img_idx == 3 else 0

    def move(self, player):
        self.move_axis(player, 0)
        self.move_axis(player, 1)
        print(self.speed)

    def move_axis(self, player, axis):
            
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
