import pygame
import os
import sys

from pygame import image


def load_image(name, color_key=None):
    try:
        image = pygame.image.load(name)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


class Hero(pygame.sprite.Sprite):
    hp = 100
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.rect = pygame.Rect(0, 0, 62, 57)
        self.frames = [load_image('data\Walk\Walk (1).png', -1),
                    load_image('data\Walk\Walk (2).png', -1),
                    load_image('data\Walk\Walk (3).png', -1),
                    load_image('data\Walk\Walk (4).png', -1),
                    load_image('data\Walk\Walk (5).png', -1),
                    load_image('data\Walk\Walk (6).png', -1),
                    load_image('data\Walk\Walk (7).png', -1),
                    load_image('data\Walk\Walk (8).png', -1),
                    load_image('data\Walk\Walk (9).png', -1),
                    load_image('data\Walk\Walk (10).png', -1),
                    load_image('data\Walk\Walk (11).png', -1),
                    load_image('data\Walk\Walk (12).png', -1),
                    load_image('data\Walk\Walk (13).png', -1),
                    load_image('data\Walk\Walk (14).png', -1),
                    load_image('data\Walk\Walk (15).png', -1)]
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        screen.fill('black')

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
    
    


pygame.init()
screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)
FPS = 50
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
image = load_image("data/pygame-8-1.png")
player = Hero(0, 0)

while True:
    screen.fill('black')
    # get all events from the queue
    for event in pygame.event.get():
        # loop events queue
        if event.type == pygame.QUIT:
            pygame.quit()
            
            
            
    
    all_sprites.draw(screen)
    all_sprites.update()
    
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
