import random
from turtle import width

import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, all_sprites=None):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)


horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):

    def __init__(self, x1, y1, x2, y2, all_sprites=None, vertical_borders=None, horizontal_borders=None):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)

for i in range(10):
    Ball(20, 100, 100)


def update(self):
    self.rect = self.rect.move(self.vx, self.vy)
    if pygame.sprite.spritecollideany(self, horizontal_borders):
        self.vy = -self.vy
    if pygame.sprite.spritecollideany(self, vertical_borders):
        self.vx = -self.vx
