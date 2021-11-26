import pygame

if __name__ == '__main__':
    a = input().split()
    try:
        pygame.init()
        size = width, height = int(a[0]), int(a[1])
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Прямоугольник')

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (1, 1, width - 2, height - 2), width=0)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
