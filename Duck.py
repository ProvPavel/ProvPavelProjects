import pygame

n = int(input())
width1 = 40
height1 = 300
a = 136.5
b = 0
if __name__ == '__main__':
    pygame.init()
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    pygame.draw.ellipse(screen, (255, 255, 255), (0, 0, 300, 300), 1)
    pygame.display.flip()
    for i in range(1, n):
        pygame.draw.ellipse(screen, (255, 255, 255), (a, b, width1, height1), 1)
        pygame.draw.ellipse(screen, (255, 255, 255), (b, a, height1, width1), 1)
        pygame.display.flip()
        width1 += 28
        a -= 15
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
