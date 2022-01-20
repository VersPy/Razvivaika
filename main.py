import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    return image


def load_image_p(name, color_key=None):
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


class Figur(pygame.sprite.Sprite):
    image = load_image("figurspng.png")

    def __init__(self, x, y):
        super().__init__(horizontal_borders)
        self.image = Figur.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


class Color(pygame.sprite.Sprite):
    image = load_image("colors.png")

    def __init__(self, x, y):
        super().__init__(horizontal_borders)
        self.image = Color.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


class Num(pygame.sprite.Sprite):
    image = load_image("numbers.png")

    def __init__(self, x, y):
        super().__init__(horizontal_borders)
        self.image = Num.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, frame, idle=True):
        super().__init__(all_sprites)
        self.x = x
        self.y = y
        self.Idle = idle
        self.rect = pygame.Rect(0, 0, 62, 57)
        self.idle = [load_image_p('data\Idle\Idle (1).png', -1),
                     load_image_p('data\Idle\Idle (2).png', -1),
                     load_image_p('data\Idle\Idle (3).png', -1),
                     load_image_p('data\Idle\Idle (4).png', -1),
                     load_image_p('data\Idle\Idle (5).png', -1),
                     load_image_p('data\Idle\Idle (6).png', -1),
                     load_image_p('data\Idle\Idle (7).png', -1),
                     load_image_p('data\Idle\Idle (8).png', -1),
                     load_image_p('data\Idle\Idle (9).png', -1),
                     load_image_p('data\Idle\Idle (10).png', -1),
                     load_image_p('data\Idle\Idle (11).png', -1),
                     load_image_p('data\Idle\Idle (12).png', -1),
                     load_image_p('data\Idle\Idle (13).png', -1),
                     load_image_p('data\Idle\Idle (14).png', -1),
                     load_image_p('data\Idle\Idle (15).png', -1)]
        self.walk = [load_image_p('data\Walk\Walk (1).png', -1),
                     load_image_p('data\Walk\Walk (2).png', -1),
                     load_image_p('data\Walk\Walk (3).png', -1),
                     load_image_p('data\Walk\Walk (4).png', -1),
                     load_image_p('data\Walk\Walk (5).png', -1),
                     load_image_p('data\Walk\Walk (6).png', -1),
                     load_image_p('data\Walk\Walk (7).png', -1),
                     load_image_p('data\Walk\Walk (8).png', -1),
                     load_image_p('data\Walk\Walk (9).png', -1),
                     load_image_p('data\Walk\Walk (10).png', -1),
                     load_image_p('data\Walk\Walk (11).png', -1),
                     load_image_p('data\Walk\Walk (12).png', -1),
                     load_image_p('data\Walk\Walk (13).png', -1),
                     load_image_p('data\Walk\Walk (14).png', -1),
                     load_image_p('data\Walk\Walk (15).png', -1)]
        self.cur_frame = frame
        if self.Idle:
            self.image = self.idle[self.cur_frame]
        else:
            self.image = self.walk[self.cur_frame]
        self.rect = self.rect.move(self.x, self.y)
        screen.fill((16, 74, 16))

    def update(self):
        global cur_frame
        self.cur_frame = (self.cur_frame + 1) % len(self.walk)
        if self.Idle:
            self.image = self.idle[self.cur_frame]
        else:
            self.image = self.walk[self.cur_frame]
        cur_frame = self.cur_frame

    def walk_idle(self):
        global Idle
        self.Idle = not self.Idle
        Idle = self.Idle
    
    def get_idle(self):
        return self.Idle

class Doska_V(pygame.sprite.Sprite):
    image = load_image("doska_v.png")

    def __init__(self, x, y):
        super().__init__(vertical_borders)
        self.image = Doska_V.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


class Doska_G(pygame.sprite.Sprite):
    image = load_image("doska_g.png")

    def __init__(self, x, y):
        super().__init__(horizontal_borders)
        self.image = Doska_G.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

pygame.init()

x = 40
y = 315

cur_frame = 0
Idle = True
stoping_x = 41

screen_size = (800, 400)
screen = pygame.display.set_mode(screen_size)
screen.fill((16, 74, 16))

speed = 500
FPS = 30
clock = pygame.time.Clock()
walker = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

doska_v_1 = Doska_V(0, 35)
doska_v_2 = Doska_V(765, 35)
doska_g_1 = Doska_G(0, 0)
doska_g_2 = Doska_G(0, 365)

figurs = Figur(70, 50)
colors = Color(300, 50)
numbers = Num(530, 50)


runing = True
while runing:
    screen.fill((16, 74, 16))
    player = Hero(x, y, cur_frame, Idle)
    
    # get all events from the queue
    for event in pygame.event.get():
        # loop events queue
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.walk_idle()
            stoping_x = event.pos[0]

    all_sprites.update()
    all_sprites.draw(screen)
    horizontal_borders.draw(screen)
    vertical_borders.draw(screen)
    
    if not player.get_idle():
        x += speed / FPS
    elif x == stoping_x:
        player.walk_idle()
    if x > 765:
        x = 45

    clock.tick(FPS)
    all_sprites.remove(player)
    pygame.display.flip()
pygame.quit()