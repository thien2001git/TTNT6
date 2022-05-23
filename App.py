import json
import random as rd
from turtle import width
import pygame as pg
from pygame.locals import *
# from map.map import *
from models.Setting import Setting
from windows.Window1 import start

import numpy as np
CELL_HIGHT = 101
CELL_WIDTH = 101
x_img = pg.image.load("img/x1.png")
x_img = pg.transform.scale(x_img, (99, 99))
o_img = pg.image.load("img/o1.png")
o_img = pg.transform.scale(o_img, (99, 99))

x_win = pg.image.load("img/x_win1.png")
o_win = pg.image.load("img/o_win1.png")
hoa = pg.image.load("img/hoa.png")

dkk = 0
white = (255, 255, 255)
line_color = (0, 0, 0)

def game_initiating_window(screen, width, height, cols, rows):
    # displaying over the screen
    # screen.blit(initiating_window, (0, 0))

    # updating the display
    # pg.display.update()
    # time.sleep(3)
    screen.fill(white)

    # drawing vertical lines
    for i in range(cols - 1):
        pg.draw.line(screen, line_color, (CELL_WIDTH * (i + 1), 0), (CELL_WIDTH * (i + 1), height), 1)
    

    # drawing horizontal lines
    for i in range(rows - 1):
        pg.draw.line(screen, line_color, (0, CELL_HIGHT * (i + 1)), (width, CELL_HIGHT * (i + 1)), 1)
    
    pg.display.update()

def myfunction(x):
    cn = 0
    for i in x:
        if i == 0:
            cn += 1
        else:
            cn = 0
        if cn == dkk:
            return "o"
    
    cn = 0
    for i in x:
        
        if i == 1:
            cn += 1
        else:
            cn = 0
        if cn == dkk:
            return "x"
    
def miniMax(map1:np.array, luot):
    pass

def checkWin(map1: np.array, dk, luot, row, col):

    cn = 0
   
    r, c = map1.shape
    # print(r)
    # print(c)
    # np.apply_along_axis(myfunction, axis=1, arr=map1)
    for i in range(c):
        if map1[row, i] == luot:
            cn += 1
            if cn == dk:
                # print("ok")
                return True
        else:
            cn = 0
    
    cn = 0
    for i in range(r):
        # print(map1[i, col])
        if map1[i, col] == luot:
            cn += 1
            if cn == dk:
                # print("ok")
                return True
        else:
            cn = 0
    col_tmp = 0
    row_tmp = 0
    if row <= col:
        col_tmp = col - row
        row_tmp = 0
        # print("{} {}".format(0, col - row))
    elif col < row:
        row_tmp = row - col
        col_tmp = 0
        # print("{} {}".format(row - col, 0))
    cn = 0
    # print("{} {}".format(row_tmp, col_tmp))
    while True:
        if map1[row_tmp, col_tmp] == luot:
            cn += 1
            if cn == dk:
                # print("ok")
                return True
        else:
            cn = 0
        row_tmp += 1
        col_tmp += 1
        if row_tmp >= r or col_tmp >= c:
            break
    
    col_tmp = col
    row_tmp = row
    # print("{} {}".format(row_tmp, col_tmp))
    while True:
        col_tmp += 1
        row_tmp -= 1
        if row_tmp < 0:
            col_tmp -= 1
            row_tmp = 0
            break
        if col_tmp > c - 1:
            col_tmp = c - 1
            row_tmp += 1
            break
    # print("{} {}".format(row_tmp, col_tmp))
 
    
    cn = 0
    while True:
        if map1[row_tmp, col_tmp] == luot:
            cn += 1
            if cn == dk:
                print("ok")
                return True
        else:
            cn = 0
        row_tmp += 1
        col_tmp -= 1
        if row_tmp > r - 1 or col_tmp < 0:
            break
    return False


class App:
    # khởi tạo
    def __init__(self, hang: int, cot: int, dk: int):
        self._running = True  # chạy
        self._screen = None
        self.size = self.weight, self.height = cot * CELL_WIDTH, hang * CELL_HIGHT  # kích thước màn hình
        self.dk = dk
        self.hang = hang
        self.cot = cot
        self.luot = 1
        self.win = False
        self.who = None
        m = []
        
        for i in range(hang):
            m.append([None] * cot)
        self.map = np.array(m)
        print(self.map)

    # khởi tạo game
    def on_init(self):
        pg.init()
        self._screen = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self._running = True
        # tên cửa sổ
        pg.display.set_caption("Cờ caro với AI")
        # thời gian
        self.CLOCK = pg.time.Clock()

    # sự kiện
    def on_event(self, event):
        if event.type == pg.QUIT:  # sự kiện thoát
            self._running = False
        # sự kiện click chuột
        if event.type == MOUSEBUTTONDOWN:
            if self.win != True:
                x, y = pg.mouse.get_pos()

                # get column of mouse click (1-3)
                col = int(x / CELL_WIDTH)
            

                # get row of mouse click (1-3)
                row = int(y / CELL_HIGHT)

                

                posx = col * CELL_WIDTH + 1
                posy = row * CELL_HIGHT + 1
                # print("{} {}".format(col, row))
                if self.luot == 1 and self.map[row, col] == None and self.win != True:
                    self._screen.blit(x_img, (posx, posy))
                    self.map[row, col] = self.luot
                    self.win = checkWin(self.map, self.dk, self.luot, row, col)
                    if self.win:
                        self._screen.blit(x_win, (0, 0))
                        self.who = "x"
                        self._running = False
                    self.luot = 0
                # if self.luot == 0 and self.map[row, col] == None:
                if self.luot == 0 and self.win != True:
                    while True:
                        row = rd.randint(0, self.hang - 1)
                        cot = rd.randint(0, self.cot - 1)
                        if self.map[row, col] == None:
                            break
                    posx = col * CELL_WIDTH + 1
                    posy = row * CELL_HIGHT + 1
                    self._screen.blit(o_img, (posx, posy))
                    self.map[row, col] = self.luot
                    self.win = checkWin(self.map, self.dk, self.luot, row, col)
                    if self.win:
                        self._screen.blit(o_win, (0, 0))
                        self.who = "o"
                        self._running = False
                    self.luot = 1
                # r, c = self.map.shape
                ss = 0
                try:
                    ss = np.sum(self.map)
                except TypeError as e:
                    pass
                if ss > 0:
                    self._screen.blit(hoa, (0, 0))
                # print(self.map)
            pg.display.update()

    # lặp màn hình
    def on_loop(self):
        
        pass

    # kết xuất
    def on_render(self):
        # print(self.map)
        pass

    # khi thoát
    def on_cleanup(self):
        pg.quit()

    # hàm chạy chính
    def on_execute(self):
        # nếu không init thì không chạy
        if self.on_init() == False:
            self._running = False
        # chạy
        game_initiating_window(self._screen, self.weight, self.height, self.cot, self.hang)
        while (self._running):
            # get sự kiện
            for event in pg.event.get():
                self.on_event(event)
            # lặp
            self.on_loop()
            # kết xuất
            self.on_render()
        # dọn dẹp
        self.on_cleanup()
        return self.who


def main():
    while True:
        root = start()
        set_str = json.loads(root.getvar("setting"))
        setting = Setting(int(set_str["hang"]), int(set_str["cot"]), int(set_str["dk"]))

        # dkk = setting.dk
        theApp = App(setting.hang, setting.cot, setting.dk)
        who = theApp.on_execute()
        
        from windows.Window2 import end
        # data["who"] = who
        r2 = end(who)
        choi_lai = r2.getvar("choi_lai")
        if choi_lai != "y":
            break

if __name__ == "__main__":
    main()
