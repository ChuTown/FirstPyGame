import pygame
from spritesheet import *
from constants import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Assuming initialX, initialY, lengthOfRect are defined in constants

BLACK = (0, 0, 0)

# Loading Owl running left or right
sprite_sheet_image_run_RIGHT = pygame.image.load("./assets/Owlet_Monster/OwletMonsterRun.png")
sprite_sheet_RIGHT = SpriteSheet(sprite_sheet_image_run_RIGHT)

sprite_sheet_image_run_LEFT = pygame.image.load("./assets/Owlet_Monster/OwletMonsterRunMirrored.png")
sprite_sheet_LEFT = SpriteSheet(sprite_sheet_image_run_LEFT)

# Loading Owl idle
sprite_sheet_image_IDLE_RIGHT = pygame.image.load("./assets\Owlet_Monster\Owlet_Monster.png")
sprite_sheet_IDLE_RIGHT = SpriteSheet(sprite_sheet_image_IDLE_RIGHT)
owlIdleRIGHT = sprite_sheet_IDLE_RIGHT.get_image(0,32,32,3,BLACK)

sprite_sheet_image_IDLE_LEFT = pygame.image.load("./assets\Owlet_Monster\OwletMonsterRunMirrored.png")
sprite_sheet_IDLE_LEFT =SpriteSheet(sprite_sheet_image_IDLE_LEFT)
owlIdleLEFT = sprite_sheet_IDLE_LEFT.get_image(0,32,32,3,BLACK)


owlXLoc = 0
owlYLoc = 0

# Create animation list
animation_list_RIGHT = []
animation_steps_RIGHT = 6

animation_list_LEFT = []
animation_steps_LEFT = 6

for x in range(animation_steps_RIGHT):
    animation_list_RIGHT.append(sprite_sheet_RIGHT.get_image(x, 32, 32, 3, BLACK))

for i in range(5, -1, -1):
    animation_list_LEFT.append(sprite_sheet_LEFT.get_image(i, 32, 32, 3, BLACK))
    

last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0

move_speed = 0.2
last_direction = "right"

run = True
while run:
    screen.fill((50, 50, 50))

    current_time = pygame.time.get_ticks()

    # Update animation
    if (current_time - last_update >= animation_cooldown):
        frame += 1
        last_update = current_time
        if frame >= len(animation_list_RIGHT):
            frame = 0

    idleOrNot = True
    
    # Move character
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        owlXLoc -= move_speed
        current_animation_list = animation_list_LEFT
        last_direction = "left"
        idleOrNot = False
    elif key[pygame.K_d]:
        owlXLoc += move_speed
        current_animation_list = animation_list_RIGHT 
        last_direction = "right"
        idleOrNot = False
    else:
        # Use the last direction when no horizontal movement
        if last_direction == "left":
            current_animation_list = animation_list_LEFT
        elif last_direction == "right":
            current_animation_list = animation_list_RIGHT

    if key[pygame.K_w]:
        owlYLoc -= move_speed
    if key[pygame.K_s]:
        owlYLoc += move_speed

    # Show frame image
    if idleOrNot == False:
        screen.blit(current_animation_list[frame], (owlXLoc, owlYLoc))
    else:
        if last_direction == "left": 
            screen.blit(owlIdleLEFT,(owlXLoc,owlYLoc))
        elif last_direction == "right":
            screen.blit
            screen.blit(owlIdleRIGHT,(owlXLoc,owlYLoc))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
