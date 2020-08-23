import pygame
import math
from pixelArtCLASS import Pixel

# Pixel Art canvas, to switch colors the top row of the keyboard from q-y

pygame.init()
# variables
rect1 = pygame.Rect(0, 0, 60, 20)
font = pygame.font.SysFont(None, 24)
wn_height = 600
wn_width = 600
pixels = []
color_switch = ["Red", "Blue", "Grey", "Purple", "Black", "Green", "Erase"]
color_selection = 0
painting = False
# window
wn = pygame.display.set_mode((wn_width, wn_height))
# colors
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
GREY = [200, 200, 200]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]
PURPLE = [150, 0, 200]
color = RED


# functions
def makePixels(arr):
    for i in range(0, 30):
        pixel = Pixel((i * 20) - 19, (i * 20) - 19)
        arr.append(pixel)
        i += 1
    return arr


def drawGrid():
    for i in range(0, 40):
        pygame.draw.line(wn, BLACK, (i * 20, 0), (i * 20, 600), 1)
        i += 1
    for j in range(0, 40):
        pygame.draw.line(wn, BLACK, (0, j * 20), (600, j * 20), 1)


def paint(x, y, rect_color):
    rect = pygame.Rect(x, y, 19, 19)
    pygame.draw.rect(wn, rect_color, rect)


wn.fill(WHITE)
makePixels(pixels)
drawGrid()

running = True
while running:
    # getting the position of the mouse and putting the pixel on the grid
    m_pos = pygame.mouse.get_pos()
    m_posX = math.ceil(m_pos[0] / 20)
    m_posY = math.ceil(m_pos[1] / 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # changing colors
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                color = RED
                color_selection = 0
            if event.key == pygame.K_w:
                color = BLUE
                color_selection = 1
            if event.key == pygame.K_e:
                color = GREY
                color_selection = 2
            if event.key == pygame.K_r:
                color = PURPLE
                color_selection = 3
            if event.key == pygame.K_t:
                color = BLACK
                color_selection = 4
            if event.key == pygame.K_y:
                color = GREEN
                color_selection = 5
            if event.key == pygame.K_a:
                color = WHITE
                color_selection = 6
            if event.key == pygame.K_z:
                wn.fill(WHITE)
                drawGrid()
        # if the user is painting
        if event.type == pygame.MOUSEBUTTONDOWN:
            painting = True
        if event.type == pygame.MOUSEBUTTONUP:
            painting = False
    # paints the squares using a function
    if painting:
        paint(pixels[m_posX].getX(), pixels[m_posY].getY(), color)

    pygame.draw.rect(wn, WHITE, rect1)
    img = font.render(color_switch[color_selection], True, BLACK)
    wn.blit(img, (0, 0))

    pygame.display.update()
