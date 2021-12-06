import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0]]

    def render(self, screen):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x]:
                    pygame.draw.rect(screen, (100, 100, 100), (x * 100, y * 100, 100, 100))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Something')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)

    running = True
    fps = 60
    clock = pygame.time.Clock()
    smth = Board(width, height)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        smth.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
