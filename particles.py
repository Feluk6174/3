import pygame, random

class dust():
    def __init__(self, pos:tuple, size:int):
        self.pos = pos
        self.size = size
        self.age = 10

    def display(self, screen):
        print(f"pos: {self.pos}, size: {self.size}, age: {self.age}")
        pygame.draw.rect(screen, (128, 128, 128), (self.pos[0], self.pos[1]-random.randint(0,self.size), self.size-self.age, self.size-self.age))
        self.age -= 1
        if self.age <= 0:
            return False
        return True
        

