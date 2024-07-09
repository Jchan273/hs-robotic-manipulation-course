# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pygame Template")
clock = pygame.time.Clock()
running = True

# initialize colors
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (51,51, 255)
LIGHT_GREY = pygame.Color("lightgrey")
PINK = (204, 33, 181)
BROWN = (128, 70, 27)
av_fonts = pygame.font.get_fonts()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    # RENDER YOUR GAME HERE
    
    pygame.draw.rect(screen,BLACK,(300,100,250,425))
    pygame.draw.rect(screen,BLACK,(300,100,250,425))
    pygame.draw.rect(screen,PINK, (310,110,230,405))
    pygame.draw.rect(screen,BLACK,(325,300,85,85))
    pygame.draw.rect(screen,BLACK,(325,415,85,85))
    pygame.draw.rect(screen,BLACK,(430,300,85,85))
    pygame.draw.rect(screen,BLACK,(430,415,85,85))
    pygame.draw.rect(screen,BROWN, (310,110,230,150))
    pygame.draw.rect(screen,BLACK,(325,145,85,85))
    pygame.draw.rect(screen,BLACK,(430,145,85,85))
    pygame.draw.rect(screen,BROWN, (335,155,65,65))
    pygame.draw.rect(screen,BROWN, (440,155,65,65))
    pygame.draw.rect(screen,LIGHT_GREY,(310,240,230,40))
    pygame.draw.rect(screen,PINK,(335,310,65,65))
    pygame.draw.rect(screen,PINK,(335,425,65,65))
    pygame.draw.rect(screen,PINK,(440,310,65,65))
    pygame.draw.rect(screen,PINK,(440,425,65,65))
    pygame.draw.line(screen,WHITE,(320,260),(530,260),25)


    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()