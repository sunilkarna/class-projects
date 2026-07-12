import pygame
import sys
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Basics: Shapes and Text")
BG_COLOR = (30, 30, 40)
RECT_COLOR = (242, 100, 25) 
TEXT_COLOR = (255, 255, 255)
font = pygame.font.SysFont(None, 48)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BG_COLOR)
    rect_x = 300
    rect_y = 200
    rect_width = 200
    rect_height = 150
    pygame.draw.rect(screen, RECT_COLOR, (rect_x, rect_y, rect_width, rect_height))
    text_surface = font.render("Hello, World!", True, TEXT_COLOR)
    screen.blit(text_surface, (280, 400))
    pygame.display.flip()
pygame.quit()
sys.exit()