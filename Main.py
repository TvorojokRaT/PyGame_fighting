from Settings import * #Импорт параметров игры, картинок и прочего.

clock = time.Clock()
background = transform.scale(image.load(BACKGROUND), (WIN_WIDTH, WIN_HEIGHT))
#Параметры
display.set_caption("Файтинг")
IS_JUMP = False #Прыгает ли игрок или нет
JUMP_COUNT = 10 #Коэф-нт прыжка
SQUATTING = False #Присел ли персонаж или нет
ATACKING = False #Атакует ли игрок или нет

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed): #Конструктор игрового спрайта
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y)) #Картинка игрока
        self.speed = player_speed #Скорость передвижения в области

        self.rect = self.image.get_rect() #Место расположения игрового спрайта в области
        self.rect.x = player_x #Расположение по X
        self.rect.y = player_y #Расположение по Y

    def reset(self): #Разместить картинку в область
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self): #Обновить положение игрока в облости и т.п.
        global IS_JUMP, JUMP_COUNT, ATACKING, SQUATTING
        keys = key.get_pressed() #Обнаружить какие кнопки были нажаты в одной итерации

        if keys[K_a] and self.rect.x > 5 and not ATACKING: #Движение игрока вправо
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < WIN_WIDTH - 115 and not ATACKING: #Движение игрока влево
            self.rect.x += self.speed

        if not IS_JUMP and not ATACKING:
            if keys[K_s]: #Приседание игрока
                self.image = transform.scale(image.load(PLAYER_IMG_SQUATTING), (PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT))
                self.speed = 3 #Снижение скорости передвижения игрока
                SQUATTING = True 
            else: #Если пользователь больше не нажимает кнопку s, то...
                #Вернуть картинку и скорость игрока в норму
                self.image = transform.scale(image.load(PLAYER_IMG), (PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT))
                self.speed = 10
                SQUATTING = False

            if keys[K_w] and not SQUATTING:
                IS_JUMP = True #Совершить прыжок при нажатии пробела и не в приседе

        if IS_JUMP:
            if JUMP_COUNT >= -10: #Коэф-нт прыжка больше -10, то
                if JUMP_COUNT < 0: #Если игрок не достиг высшей точки прыжка, то
                    self.rect.y += (JUMP_COUNT ** 2) / 4 

                else: #А если достиг, то
                    self.rect.y -= (JUMP_COUNT ** 2) / 4

                JUMP_COUNT -= 1 
            else:
                IS_JUMP = False 
                JUMP_COUNT = 10 #Вернуть коэф-т прыжка в норму

    def atack(self): 
        global ATACKING, now
        if not ATACKING and not IS_JUMP and not SQUATTING:
            now = time.get_ticks()
            ATACKING = True
            self.image = transform.scale(image.load(PLAYER_IMG_ATACKING1), (PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT))
            self.speed = 0

    def updateATACKING(self):
        global ATACKING
        current_time = time.get_ticks()
        if current_time - now >= 300:
            ATACKING = False

class Enemy(GameSprite):
    def update(self):
        pass

def Quitt():
    global RUN
    RUN = False

def Startt():
    global START
    START = True

#Создание объектов

player = Player(PLAYER_IMG, 100, 100, PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT, 10)
enemy = Enemy(ENEMY_IMG, 400, 100, PLAYER_IMG_WIDTH, PLAYER_IMG_HEIGHT, 10)

while RUN == True:
    clock.tick(60)
    for i in event.get():
        if i.type == QUIT:
            RUN = False

        if i.type == MOUSEBUTTONDOWN:
            if START:
                if i.button == 1:
                    player.atack()

    if ATACKING:
        player.updateATACKING()

    win.blit(background, (0, 0))
    enemy.reset()
    player.reset()
    if START:
        player.update()
        enemy.update()
    else:
        win.blit(DIALOGEWIN, (0, 0))
        win.blit(DialogeQ1, (70, 400))
        DialogeA1.draw("Да", (255, 255, 255), lambda: Startt())
        DialogeA2.draw("Нет", (255, 255, 255), lambda: Quitt())

    display.update()
    time.delay(50)