# This is a comment! My name is Xandra!
from pygame import *
from random import *

init()

print("""
      The game is about to start!
      Dodge the pipes to win
      Good luck!
      """)

screen = display.set_mode((800, 600))

background_image = image.load("bg.png")
bird_image = image.load("bird.png")
pipe_top_image = image.load("top.png")
pipe_bottom_image = image.load("bottom.png")

bird_x = 10
bird_y = 250

pipe_x = 200
pipe_y = 250
pipe_flipped = False
pipe2_x = 450
pipe2_y = 100
pipe2_flipped = False
# adjusted the distance to next hanging pipe
pipe3_x = 760
pipe3_y = 400
pipe3_flipped = True

while True:

    new_event = event.poll()
    if new_event.type == KEYDOWN and new_event.key == K_UP:
        bird_y = bird_y - 50
    if new_event.type == KEYDOWN and new_event.key == K_DOWN:
        bird_y = bird_y + 50

    pipe_x = pipe_x - 2
    pipe2_x = pipe2_x - 2
    pipe3_x = pipe3_x - 2

    background = screen.blit(background_image, (0, 0))
    bird = screen.blit(bird_image, (bird_x, bird_y))

    if pipe_flipped:
        pipe = screen.blit(pipe_top_image, (pipe_x, -pipe_y))
    else:
        pipe = screen.blit(pipe_bottom_image, (pipe_x, pipe_y))

    if pipe2_flipped:
        pipe2 = screen.blit(pipe_top_image, (pipe2_x, -pipe2_y))
    else:
        pipe2 = screen.blit(pipe_bottom_image, (pipe2_x, pipe2_y))

    if pipe3_flipped:
        pipe3 = screen.blit(pipe_top_image, (pipe3_x, -pipe3_y))
    else:
        pipe3 = screen.blit(pipe_bottom_image, (pipe3_x, pipe3_y))
    

    display.update()


    if bird.colliderect(pipe):
        print("Game Over!")
        quit()
        break

    if bird.colliderect(pipe2):
        print("Game Over!")
        quit()
        break
    
    if bird.colliderect(pipe3):
        print("Game Over!")
        quit()
        break

    if pipe_x < -87:
        pipe_x = 800
        pipe_y = randint(100, 500)
        pipe_flipped = choice([True, False])

    if pipe2_x < -87:
        pipe2_x = 800
        pipe2_y = randint(100, 500)
        pipe2_flipped = choice([True, False])

    if pipe3_x < -87:
        pipe3_x = 800
        pipe3_y = randint(100, 500)
        pipe3_flipped = choice([True, False])
