import pygame, sys
import players, tiles, background, const, enemys, test, particles

pygame.init()


ground = []
background_list = []
particle_list = []
enemy_list = []
tick = 0
game_over = False
const.SCREEN_SIZE = (1024, 640)
screen = pygame.display.set_mode(const.SCREEN_SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()
health_bar = background.health_bar()

#enemy_list.append(enemys.Ghost())

for x in range(int(const.SCREEN_SIZE[0]/(const.BASE_SIZE*4))+1):
    for y in range(int(const.SCREEN_SIZE[1]/(const.BASE_SIZE*4))+1):
        background_list.append(background.Background([x*const.BASE_SIZE*4, y*const.BASE_SIZE*4]))

for i in range(6):
    background_list.append(background.background_object((const.BASE_SIZE*4+i*const.BASE_SIZE*2, const.SCREEN_SIZE[1]-const.BASE_SIZE*3), "closed_prison"))
    background_list.append(background.background_object((const.BASE_SIZE*4+i*const.BASE_SIZE*2, const.BASE_SIZE*3), "closed_prison"))

for x in range(int(const.SCREEN_SIZE[0]/const.BASE_SIZE)):
    ground.append(tiles.Brick_block([x*const.BASE_SIZE, const.SCREEN_SIZE[1]-const.BASE_SIZE]))
    ground.append(tiles.Brick_block([x*const.BASE_SIZE, 0]))

for y in range(int(const.SCREEN_SIZE[1]/const.BASE_SIZE)):
    ground.append(tiles.Brick_block([0, y*const.BASE_SIZE]))
    ground.append(tiles.Brick_block([const.SCREEN_SIZE[0]-const.BASE_SIZE, y*const.BASE_SIZE]))

for i in range(int(const.SCREEN_SIZE[0]/const.BASE_SIZE)-4):
    ground.append(tiles.Brick_block((const.BASE_SIZE*3+i*const.BASE_SIZE, const.SCREEN_SIZE[1]-const.BASE_SIZE*5)))

ground.append(tiles.Brick_block([const.BASE_SIZE, const.SCREEN_SIZE[1]-const.BASE_SIZE*2]))
ground.append(tiles.Brick_block([const.BASE_SIZE, const.SCREEN_SIZE[1]-const.BASE_SIZE*3]))
ground.append(tiles.Brick_block([const.BASE_SIZE*2, const.SCREEN_SIZE[1]-const.BASE_SIZE*2]))

player = players.Player()
enemy_list.append(enemys.Ghost())


while True:
    screen.fill((0,0,0))
    for object in background_list:
        object.display(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        player.calc_event(event)
    
    for tile in ground:
        tile.display(screen)
        
    for enemy in enemy_list:
        enemy.move(player)

    for enemy in enemy_list:
        enemy.display(screen, tick)

    for i, particle in enumerate(particle_list):
        keep = particle.display(screen)
        if not keep:
            particle_list.pop(i)

    game_over, particle_list = player.move(ground, enemy_list, particle_list)

    player.display(screen, tick)
    
    if player.pos[1] > 1000:
        break

    #test.print_general_info(player)

    #print(particle_list)

    health_bar.display(screen, player.health)
    pygame.display.update()
    clock.tick(60)
    tick += 1
    if game_over:
        break
    