# This is a comment! My name is Xandra!
from pygame import *
init()

print("""
      The game is about to start!
      You can move the bird up and down using the arrow keys
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
pipe2_x = 450
pipe2_y = 100
pipe3_x = 700
pipe3_y = 400

while True:

    new_event = event.poll()
    if new_event.type == KEYDOWN and new_event.key == K_UP:
        print("Going up")
        bird_y = bird_y - 50
    if new_event.type == KEYDOWN and new_event.key == K_DOWN:
        print("Going down")
        bird_y = bird_y + 50
    if new_event.type == KEYDOWN and new_event.key == K_LEFT:
        print("Going left")
        bird_x = bird_x - 50
    if new_event.type == KEYDOWN and new_event.key == K_RIGHT:
        print("Going up")
        bird_x = bird_x + 50

    background = screen.blit(background_image, (0, 0))
    bird = screen.blit(bird_image, (bird_x, bird_y))
    pipe = screen.blit(pipe_bottom_image, (pipe_x, pipe_y))
    pipe2 = screen.blit(pipe_bottom_image, (pipe2_x, pipe2_y))
    pipe3 = screen.blit(pipe_top_image, (pipe3_x, -pipe3_y))

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

    if bird_x >= 800:
        print("Winner!")
        quit()
        break


