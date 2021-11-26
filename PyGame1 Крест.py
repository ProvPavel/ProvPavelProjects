import pygame

if __name__ == '__main__':
    a = input().split()
    try:
        pygame.init()
        size = width, height = int(a[0]), int(a[1])
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Крест')

        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), width=5)
        pygame.draw.line(screen, (255, 255, 255), (0, height), (width, 0), width=5)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
