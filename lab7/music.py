import pygame 
from pygame import mixer

pygame.init()
mixer.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
FPS = 50
done = False
n = 0
musics = ['music/SAMIDOT.mp3']
plays = ['incoming.png', 'afterdark.png']
pause = 'pause.png'
play = 'play-button.png'
rewind_button = 'rewind.png'
forward_button = 'forward.png'

def start(n):
    
    mixer.music.load(musics[n])
      
    mixer.music.set_volume(0.2)

    mixer.music.play()

start(n)
screen.fill((255, 255, 255))
screen.blit(pygame.image.load(plays[n]), (100, 50))
screen.blit(pygame.image.load(play), (100, 120))
screen.blit(pygame.image.load(rewind_button), (30, 65))
screen.blit(pygame.image.load(forward_button), (41, 65))
paused = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if(paused == False):
                mixer.music.pause()
                paused = True
                
                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load(pause), (200, 65))
                screen.blit(pygame.image.load(plays[n]), (15, 10))
                screen.blit(pygame.image.load(rewind_button), (35, 65))
                screen.blit(pygame.image.load(forward_button), (41, 65))
            else:
                mixer.music.unpause()
                paused = False
                screen.fill((255, 255, 255))
                screen.blit(pygame.image.load(plays[n]), (15, 10))
                screen.blit(pygame.image.load(play), (38, 65))
                screen.blit(pygame.image.load(rewind_button), (35, 65))
                screen.blit(pygame.image.load(forward_button), (41, 65))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if n == 4: n = 0
            else: n += 1
            screen.fill((255, 255, 255))
            screen.blit(pygame.image.load(plays[n]), (15, 10))
            screen.blit(pygame.image.load(play), (38, 60))
            screen.blit(pygame.image.load(rewind_button), (35, 60))
            screen.blit(pygame.image.load(forward_button), (41, 60))
            start(n)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if n == 0: n = 4
            else: n -= 1
            screen.fill((255, 255, 255))
            screen.blit(pygame.image.load(plays[n]), (10, 10))
            screen.blit(pygame.image.load(play), (30, 60))
            screen.blit(pygame.image.load(rewind_button), (35, 65))
            screen.blit(pygame.image.load(forward_button), (40, 60))
            start(n)
  
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()