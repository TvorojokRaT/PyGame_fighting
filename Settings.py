from pygame import *
from pathlib import Path

#Классы
class Button():
    def __init__(self, x, y, img, width, height):
        self.x = x
        self.y = y
        self.img = Path("images", img)
        self.img = transform.scale(image.load(self.img), (width, height))
        self.width = width
        self.height = height

    def draw(self, text, text_color, action = None):
        mouserect = mouse.get_pos()
        click = mouse.get_pressed()

        if self.x < mouserect[0] < self.x + self.width:
            if self.y < mouserect[1] < self.y + self.height:
                if click[0] == 1 and action != None:
                    action()
                    time.delay(100)
                    


        win.blit(self.img, (self.x, self.y))

        text = font1.render(text, True, text_color)
        win.blit(text, (self.x + self.width//2 - 25, self.y + 6))

#Основные настройки
FPS = 60 #Кадры в секунду 

#Размеры окна
WIN_WIDTH = 700 #Ширина X
WIN_HEIGHT = 550 #Высота Y
win = display.set_mode((WIN_WIDTH, WIN_HEIGHT))

#Условия игры
RUN = True #Условие игры
START = False #Начата игра или нет?

#Картинки
BACKGROUND = Path("images", "testbackground.png")

PLAYER_IMG = Path("images", "TestPlayerChar.png")
ENEMY_IMG = Path("images", "TestEnemy.png")
PLAYER_IMG_WIDTH = 200
PLAYER_IMG_HEIGHT = 350
PLAYER_IMG_SQUATTING = Path("images", "TestPlayerCharSquatting.png")
#Атака игрока или врага
PLAYER_IMG_ATACKING1 = Path("images", "TestPlayerCharAtacking1.png")
ENEMY_IMG_ATACKING1 = Path("images", "TestEnemyAtacking1.png")

DIALOGEWIN = Path("images", "Dialoge.png")
DIALOGEWIN = transform.scale(image.load(DIALOGEWIN), (WIN_WIDTH, WIN_HEIGHT))

#Шрифт
font.init()
font1 = font.Font("Antropos  Freefont.ttf", 30)
#Тексты
DialogeQ1 = font1.render("Ты готов(-a) начать битву?", True, (255, 255, 255))
DialogeA1 = Button(450, 270, "AnsBtn.png", 209, 51)
DialogeA2 = Button(450, 323, "AnsBtn.png", 209, 51)


