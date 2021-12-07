import pygame, random
import const, test, particles

class Player():
    def __init__(self):
        self.pos = [480, const.SCREEN_SIZE[1]-const.BASE_SIZE*2-1]
        self.colide_pos = self.pos
        self.size = (const.BASE_SIZE, const.BASE_SIZE)
        self.colide_size = self.size
        self.level_pos = [0, 0]
        self.speed = [0, 0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.def_speed = int(const.BASE_SIZE*0.09375)
        self.on_ground = False
        self.fall_time = 0
        self.jump_speed = int(const.BASE_SIZE*0.25)
        self.path = "./images/player/"
        self.idle_img_idx = 0
        self.moving_img_idx = 0
        self.covering_img_idx = 0
        self.covering = False
        self.looking_left = False
        self.health = 32
        self.action = "idle"
        self.images = {"idle_0":{"img": pygame.image.load("./images/player/idle_0.png"), "size": (const.BASE_SIZE-int(const.BASE_SIZE/32*12), const.BASE_SIZE), "edit_pos": (int(const.BASE_SIZE/32*6), 0)}, 
        "idle_1":{"img": pygame.image.load("./images/player/idle_1.png"), "size": (const.BASE_SIZE-int(const.BASE_SIZE/32*12), const.BASE_SIZE), "edit_pos": (int(const.BASE_SIZE/32*6), 0)}, 
        "idle_2":{"img": pygame.image.load("./images/player/idle_2.png"), "size": (const.BASE_SIZE-int(const.BASE_SIZE/32*12), const.BASE_SIZE), "edit_pos": (int(const.BASE_SIZE/32*6), 0)}, 
        "idle_3":{"img": pygame.image.load("./images/player/idle_3.png"), "size": (const.BASE_SIZE-int(const.BASE_SIZE/32*12), const.BASE_SIZE), "edit_pos": (int(const.BASE_SIZE/32*6), 0)}, 
        "moving_0":{"img": pygame.image.load("./images/player/moving_0.png"), "size": (const.BASE_SIZE-int(const.BASE_SIZE/32*16), const.BASE_SIZE-int(const.BASE_SIZE/32*1)), "edit_pos": (int(const.BASE_SIZE/32*8), int(const.BASE_SIZE/32*1))}, 
        "moving_1":{"img": pygame.image.load("./images/player/moving_1.png"), "size": (const.BASE_SIZE-int(const.BASE_SIZE/32*16), const.BASE_SIZE-int(const.BASE_SIZE/32*1)), "edit_pos": (int(const.BASE_SIZE/32*8), int(const.BASE_SIZE/32*1))}}
        self.max_fall_speed = 28
        self.walking_particle_size = 5


    def display(self, screen, tick):
        if self.speed[0] == 0:
            if self.covering:
                img = pygame.image.load(self.path+"covering_"+str(self.covering_img_idx)+".png")
                img = pygame.transform.scale(img, self.size)
                img = pygame.transform.flip(img, self.looking_left, False)
                screen.blit(img, (self.pos[0], self.pos[1]))

                self.action = "covering"

                if tick % 10 == 0:
                    self.covering_img_idx = self.covering_img_idx + 1 if not self.covering_img_idx == 1 else 0
                
            else:
                img = self.images["idle_"+str(self.idle_img_idx)]["img"]
                img = pygame.transform.scale(img, self.size)
                img = pygame.transform.flip(img, self.looking_left, False)
                self.update_collision_box(self.images["idle_"+str(self.idle_img_idx)]["size"], self.images["idle_"+str(self.idle_img_idx)]["edit_pos"])
                #pygame.draw.rect(screen, (255, 0, 0), (self.pos[0], self.pos[1], self.size[0], self.size[1]))
                #pygame.draw.rect(screen, (0, 255, 0), (self.colide_pos[0], self.colide_pos[1], self.colide_size[0], self.colide_size[1]))
                screen.blit(img, (self.pos[0], self.pos[1]))
            
                self.action = "idle"


                if tick % 15 == 0:
                    self.idle_img_idx = self.idle_img_idx + 1 if not self.idle_img_idx == 3 else 0


        else:
            img = self.images["moving_"+str(self.moving_img_idx)]["img"]
            img = pygame.transform.scale(img, self.size)
            if self.speed[0] < 0:
                img = pygame.transform.flip(img, True, False)
            self.update_collision_box(self.images["moving_"+str(self.moving_img_idx)]["size"], self.images["moving_"+str(self.moving_img_idx)]["edit_pos"])
            #pygame.draw.rect(screen, (255, 0, 0), (self.pos[0], self.pos[1], self.size[0], self.size[1]))
            #pygame.draw.rect(screen, (0, 255, 0), (self.colide_pos[0], self.colide_pos[1], self.colide_size[0], self.colide_size[1]))
            screen.blit(img, (self.pos[0], self.pos[1]))

            self.action = "moving"


            if tick % 4 == 0:
                self.moving_img_idx = self.moving_img_idx + 1 if not self.moving_img_idx == 1 else 0
            

    def calc_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.speed[0] -= self.def_speed
                self.looking_left = True
                
            if event.key == pygame.K_d:
                self.speed[0] += self.def_speed
                self.looking_left = False
            if event.key == pygame.K_w:
                if self.on_ground:
                    self.speed[1] -= self.jump_speed
                    self.on_ground = False
            if event.key == pygame.K_c:
                self.covering = True
        
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.speed[0] += self.def_speed
            if event.key == pygame.K_d:
                self.speed[0] -= self.def_speed
            if event.key == pygame.K_c:
                self.covering = False

    def move(self, obstacles, enemy_list, particle_list:list):
        particle_list = self.check_on_ground(obstacles,particle_list)
        self.fall()
        self.pos[0] += self.speed[0]
        self.update_collision_box(self.colide_size, self.images[self.action+"_"+str(self.moving_img_idx)]["edit_pos"])
        colided, obstacle = self.collision(obstacles)

        self.action_colided(colided, 0, obstacle)

        self.pos[1] += self.speed[1]
        self.update_collision_box(self.colide_size, self.images[self.action+"_"+str(self.moving_img_idx)]["edit_pos"])
        colided, obstacle = self.collision(obstacles)
        self.action_colided(colided, 1, obstacle)
        if colided:
            self.on_ground = True
            self.fall_time = 0
            self.speed[1] = 0
        if not self.speed[0] == 0 and self.on_ground:
            if self.looking_left:
                particle_list.append(particles.dust((self.pos[0], self.pos[1]+self.size[1]), self.walking_particle_size))
            else:
                particle_list.append(particles.dust((self.pos[0]+self.size[0], self.pos[1]+self.size[1]), self.walking_particle_size))
        return self.enemy_colisions(enemy_list), particle_list


    def action_colided(self, colided, axis, obstacle):
        if not colided:
            return None
        else:
            
            if self.colide_pos[axis]+self.colide_size[axis] >= obstacle.pos[axis] and self.colide_pos[axis]+self.colide_size[axis] <= obstacle.pos[axis]+int(obstacle.size[axis]/2):
                self.colide_pos[axis] = obstacle.pos[axis]-self.colide_size[axis]-1

            elif self.colide_pos[axis] > int((obstacle.pos[axis]+obstacle.size[axis])/2) and self.colide_pos[axis] < obstacle.pos[axis]+obstacle.size[axis]:
                self.colide_pos[axis] = obstacle.pos[axis]+obstacle.size[axis]+1

            self.update_display_pos()

    def fall(self):
        if not self.on_ground:
            self.speed[1] += self.fall_time*const.GRAVITY
            self.fall_time += 1
        if self.speed[1] > self.max_fall_speed:
            self.speed[1] = self.max_fall_speed

    def collision(self, obstacles):
        for obstacle in obstacles:
            if self.colide_pos[0]+self.colide_size[0] >= obstacle.pos[0] and self.colide_pos[0] <= obstacle.pos[0]+obstacle.size[0] and self.colide_pos[1]+self.colide_size[1] >= obstacle.pos[1] and self.colide_pos[1] <= obstacle.pos[1]+obstacle.size[1]:
                return True, obstacle
        return False, obstacle

    def check_on_ground(self, obstacles, particle_list:list):
        self.colide_pos[1] += 3
        colided, obstacle = self.collision(obstacles)
        if colided:
            if not self.on_ground:
                particle_list.append(particles.dust((self.pos[0]-5, self.pos[1]+self.size[1]), self.walking_particle_size+1))
                particle_list.append(particles.dust((self.pos[0]-10, self.pos[1]+self.size[1]), self.walking_particle_size+2))
                particle_list.append(particles.dust((self.pos[0]-15, self.pos[1]+self.size[1]), self.walking_particle_size+3))
                particle_list.append(particles.dust((self.pos[0]-20, self.pos[1]+self.size[1]), self.walking_particle_size+4))
                particle_list.append(particles.dust((self.pos[0]-25, self.pos[1]+self.size[1]), self.walking_particle_size+5))
            self.on_ground = True
        else:
            self.on_ground = False
        self.colide_pos[1] -= 3
        return particle_list

    def update_collision_box(self, size, rel_pos):
        self.colide_size = size
        self.colide_pos = [self.pos[0]+rel_pos[0], self.pos[1]+rel_pos[1]]

        
    def update_display_pos(self):
        
        if self.action == "idle":

            self.pos = [self.colide_pos[0]-self.images[self.action+"_"+str(self.idle_img_idx)]["edit_pos"][0], self.colide_pos[1]-self.images[self.action+"_"+str(self.idle_img_idx)]["edit_pos"][1]]



            
        elif self.action == "moving":
            self.pos = [self.colide_pos[0]-self.images[self.action+"_"+str(self.moving_img_idx)]["edit_pos"][0], self.colide_pos[1]-self.images[self.action+"_"+str(self.moving_img_idx)]["edit_pos"][1]]

        
    def enemy_colisions(self, enemy_list):
        for enemy in enemy_list:
            if self.colide_pos[0]+self.colide_size[0] >= enemy.colide_pos[0] and self.colide_pos[0] <= enemy.colide_pos[0]+enemy.colide_size[0] and self.colide_pos[1]+self.colide_size[1] >= enemy.colide_pos[1] and self.colide_pos[1] <= enemy.colide_pos[1]+enemy.colide_size[1]:
                return True
        return False