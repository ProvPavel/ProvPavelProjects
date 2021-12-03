import pygame


class Error(Exception):
    pass


if __name__ == '__main__':
    try:
        input_value = input().split()
        w, hue = int(input_value[0]), int(input_value[1])
        if w > 100 or w < 0 or w % 4 != 0 or hue > 360 or hue < 0:
            raise Error
        color_1 = pygame.Color(0, 0, 0)
        color_2 = pygame.Color(0, 0, 0)
        color_3 = pygame.Color(0, 0, 0)
        color_1.hsva = (hue, 100, 100)
        color_2.hsva = (hue, 100, 75)
        color_3.hsva = (hue, 100, 50)

        pygame.init()
        size = 300, 300
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Куб')

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, color_2, (150 - int(0.75 * w), 150 - int(0.25 * w), w, w))
        pygame.draw.polygon(screen, color_1, ((150 - int(0.75 * w), 150 - int(0.25 * w)),
                                              (150 - int(0.25 * w), 150 - int(0.75 * w)),
                                              (150 + int(0.75 * w), 150 - int(0.75 * w)),
                                              (150 + int(0.25 * w), 150 - int(0.25 * w))))
        pygame.draw.polygon(screen, color_3, ((150 + int(0.25 * w), 150 - int(0.25 * w)),
                                              (150 + int(0.75 * w), 150 - int(0.75 * w)),
                                              (150 + int(0.75 * w), 150 + int(0.25 * w)),
                                              (150 + int(0.25 * w), 150 + int(0.75 * w))))
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()
    except Exception:
        print('Неправильный формат ввода')
