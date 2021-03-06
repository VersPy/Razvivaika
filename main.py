import sqlite3
import pygame
import os


def text(text, x, y):
    font = pygame.font.Font(None, 50)
    logo = font.render(text, True, pygame.Color('gold'))
    screen.blit(logo, (x, y))


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


class Exit_btn(pygame.sprite.Sprite):
    image = load_image("exit.png")

    def __init__(self, x, y):
        super().__init__(buttons)
        self.image = Exit_btn.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Blue(pygame.sprite.Sprite):
    image = load_image("blue.png")

    def __init__(self, x, y):
        super().__init__(page_three)
        self.image = Blue.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Yellow(pygame.sprite.Sprite):
    image = load_image("yellow.png")

    def __init__(self, x, y):
        super().__init__(page_three)
        self.image = Yellow.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Red(pygame.sprite.Sprite):
    image = load_image("red.png")

    def __init__(self, x, y):
        super().__init__(page_three)
        self.image = Red.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class One(pygame.sprite.Sprite):
    image = load_image("one.png")

    def __init__(self, x, y):
        super().__init__(page_four)
        self.image = One.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Two(pygame.sprite.Sprite):
    image = load_image("two.png")

    def __init__(self, x, y):
        super().__init__(page_four)
        self.image = Two.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Three(pygame.sprite.Sprite):
    image = load_image("three.png")

    def __init__(self, x, y):
        super().__init__(page_four)
        self.image = Three.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Square(pygame.sprite.Sprite):
    image = load_image("square.png")

    def __init__(self, x, y):
        super().__init__(page_two)
        self.image = Square.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Circle(pygame.sprite.Sprite):
    image = load_image("circle.png")

    def __init__(self, x, y):
        super().__init__(page_two)
        self.image = Circle.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Trinagle(pygame.sprite.Sprite):
    image = load_image("trinagle.png")

    def __init__(self, x, y):
        super().__init__(page_two)
        self.image = Trinagle.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y

class Figur(pygame.sprite.Sprite):
    image = load_image("figurspng.png")

    def __init__(self, x, y):
        super().__init__(page_one)
        self.image = Figur.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


class Color(pygame.sprite.Sprite):
    image = load_image("colors.png")

    def __init__(self, x, y):
        super().__init__(page_one)
        self.image = Color.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


class Num(pygame.sprite.Sprite):
    image = load_image("numbers.png")

    def __init__(self, x, y):
        super().__init__(page_one)
        self.image = Num.image
        self.rect = self.image.get_rect()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, frame, idle=True):
        super().__init__(page_one)
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

def terminate():
    import sys
    pygame.quit()
    sys.exit()

def start_screen():
    intro_text = ['','',"                                              Razvivaika",
                  "         Это развивающая детская игра для самых маленьких",
                  "                                           И да это 50cent"]

    fon = pygame.transform.scale(load_image('fon.png'), (800, 400))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 35)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('gold'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)

pygame.init()

x = 40
y = 315

pygame.mixer.music.load('data\in da club.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

pygame.display.set_caption("Razvivaika")
pygame.display.set_icon(pygame.image.load('data\icon.png'))

cur_frame = 0
Idle = True
stoping_x = 41

screen_size = (800, 400)
screen = pygame.display.set_mode(screen_size)
screen.fill((16, 74, 16))

speed = 150
FPS = 24
clock = pygame.time.Clock()
walker = pygame.time.Clock()
start_screen()

page_one = pygame.sprite.Group()
page_two = pygame.sprite.Group()
page_three = pygame.sprite.Group()
page_four = pygame.sprite.Group()
page_five = pygame.sprite.Group()

buttons = pygame.sprite.Group()

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

doska_v_1 = Doska_V(0, 35)
doska_v_2 = Doska_V(765, 35)
doska_g_1 = Doska_G(0, 0)
doska_g_2 = Doska_G(0, 365)

page = 1
test = 1

figurs = Figur(70, 50)
colors = Color(300, 50)
numbers = Num(530, 50)

circle = Circle(75, 75)
trinagle = Trinagle(290, 75)
square = Square(540, 75)

blue = Blue(50, 75)
red = Red(300, 75)
yellow = Yellow(550, 75)

one = One(100, 75)
two = Two(350, 75)
three = Three(500, 75)

exit = Exit_btn(50, 40)

result = 0

runing = True
flag = True
while runing:
    screen.fill((16, 74, 16))
    # get all events from the queue
    for event in pygame.event.get():
        # loop events queue
        if event.type == pygame.QUIT:
            runing = False
        if page == 1: 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.get_idle() or x in (140, 390, 600):
                    player.walk_idle()
                    if 100 < event.pos[0] < 234 and 200 < event.pos[1] < 235:
                        stoping_x = 140
                        flag = True
                    elif 350 < event.pos[0] < 451 and 270 < event.pos[1] < 304:
                        stoping_x = 390
                        flag = True
                    elif 560 < event.pos[0] < 691 and 200 < event.pos[1] < 235:
                        stoping_x = 600
                        flag = True
                    elif 650 < event.pos[0] < 724 and 315 < event.pos[1] < 349:
                        stoping_x = 690
                        flag = True
        if page in (2, 3, 4, 5):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 < event.pos[0] < 114 and 40 < event.pos[1] < 72:
                    
                    test = 1
                    if page == 5:
                        con = sqlite3.connect('data\datebase.sqlite')
                        cur = con.cursor()
                        cur.execute(f"""INSERT INTO results(result) VALUES({result})""").fetchall()
                        con.commit()
                    page = 1
                    result = 0
        if page == 5:
            if test == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 290 < event.pos[0] < 490 and 75 < event.pos[1] < 300:
                        result += 1
                        test = 2
                    if 75 < event.pos[0] < 267 and 75 < event.pos[1] < 267:
                        test = 2
                    if 540 < event.pos[0] < 743 and 75 < event.pos[1] < 278:
                        test = 2
                    continue
            if test == 2:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 < event.pos[0] < 250 and 75 < event.pos[1] < 275:
                        result += 1
                        test = 3
                    elif 300 < event.pos[0] < 500 and 75 < event.pos[1] < 275:
                        test = 3
                    elif 550 < event.pos[0] < 750 and 75 < event.pos[1] < 275:
                        test = 3
                    continue
            if test == 3:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 500 < event.pos[0] < 666 and 75 < event.pos[1] < 256:
                        result += 1
                        test = 4
                    elif 350 < event.pos[0] < 460 and 75 < event.pos[1] < 270:
                        test = 4
                    elif 100 < event.pos[0] < 255 and 75 < event.pos[1] < 311:
                        test = 4
                    continue

    if page == 1:
        player = Hero(x, y, cur_frame, Idle)
        text('Фигуры', 100, 200)
        text('Цвета', 350, 270)
        text('Цифры', 560, 200)
        text('Тест', 650, 315)
        page_one.update()
        page_one.draw(screen)

        if x < stoping_x and not player.get_idle():
            x += speed / FPS
        elif x >= stoping_x and flag:
            player.walk_idle()
            flag = False
            if stoping_x == 140:
                page = 2
            if stoping_x == 390:
                page = 3
            if stoping_x == 600:
                page = 4
            if stoping_x == 690:
                page = 5
            x = 45
        page_one.remove(player)
    if page == 2:
        buttons.draw(screen)
        page_two.draw(screen)
        text('Это круг', 100, 300)
        text('Это треугольник', 250, 300)
        text('Это квадрат', 540, 300)
    if page == 3:
        buttons.draw(screen)
        page_three.draw(screen)
        text('Это синий', 75, 300)
        text('Это красный', 300, 300)
        text('Это жёлтый', 550, 300)
    if page == 4:
        buttons.draw(screen)
        page_four.draw(screen)
        text('Это один', 75, 300)
        text('Это два', 325, 300)
        text('Это три', 550, 300)
    if page == 5:
        buttons.draw(screen)
        if test == 1:
            print(test)
            page_two.draw(screen)
            text('Выбери треугольник', 200, 300)
        if test == 2:
            print(test)
            page_three.draw(screen)
            text('Выбери синий цвет', 200, 300)
        if test == 3:
            page_four.draw(screen)
            text('Выбери число три', 200, 300)
        if test == 4:
            text(f'Вы ответили на:{result} вопроса правильно', 100, 150)
            

    horizontal_borders.draw(screen)
    vertical_borders.draw(screen)

    clock.tick(FPS)

    pygame.display.flip()
pygame.quit()
