# from audioop import minmax
import json
import random as rd
from turtle import width
import pygame as pg
from pygame.locals import *
# from map.map import *
from models.Setting import Setting
from windows.Window1 import start
from minimax import minimax
import pandas as pd

import numpy as np

CELL_HIGHT = 21
CELL_WIDTH = 21
x_img = pg.image.load("img/x1.png")
x_img = pg.transform.scale(x_img, (19, 19))
o_img = pg.image.load("img/o1.png")
o_img = pg.transform.scale(o_img, (19, 19))

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
        pg.draw.line(screen, line_color, (CELL_WIDTH * (i + 1), 0),
                     (CELL_WIDTH * (i + 1), height), 1)

    # drawing horizontal lines
    for i in range(rows - 1):
        pg.draw.line(screen, line_color, (0, CELL_HIGHT * (i + 1)),
                     (width, CELL_HIGHT * (i + 1)), 1)

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


def rr(x):
    return "".join(x)


def checkWinText(x, z):
    for i in x:
        if z in i:
            print("ok")
            return True
    return False


def checkWin(map1: np.array, dk, luot):
    r, c = map1.shape
    x = np.apply_along_axis(rr, axis=1, arr=map1)

    ll = []
    if luot == 1:
        for i in range(5):
            ll.append("x")
    else:
        for i in range(5):
            ll.append("o")

    z = "".join(ll)

    if checkWinText(x, z):
        return True

    x = np.apply_along_axis(rr, axis=0, arr=map1)

    if checkWinText(x, z):
        return True

    x = list()
    for i in range(20):
        s1 = []
        s2 = []
        u = 0
        for j in range(i, 20):
            if i == 0:
                s1.append(map1[j, j])
            else:
                s1.append(map1[u, j])
                s2.append(map1[j, 0])
                u += 1
        x.append("".join(s1))
        x.append("".join(s2))

    if checkWinText(x, z):
        return True

    x = list()
    u = 0
    v = 0
    d = 0
    while True:
        s1 = []

        i = u
        j = v
        while True:
            s1.append(map1[i, j])
            i += 1
            j -= 1
            if i >= 20 or j <= -1:
                break

        x.append("".join(s1))
        if v != 19:
            v += 1
        if v == 19:
            d += 1
            if d > 1:
                u += 1
        if u >= 20:
            break
    if checkWinText(x, z):
        return True


def isValid(x, y):
    if x < 0 or y < 0 or x >= 20 or y >= 20:
        return False
    else:
        return True


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b


td = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
strdk = {
    "xxxx_": 100,
    "xxx__": 99,
    "_xxx_": 98,
    "__xxx": 97,
    "xxxxo": 100,
    "xxxo_": 90,
    "xx___": 10,
    "oo___": 10,
    "_xx__": 9,
    "_oo__": 9,
    "__xx_": 8,
    "__xxo": 5,
    "_xxo_": 6,
    "xxo__": 7,



    "ooo__":99,
    "_ooo_":98,
    "__ooo":97,
    "oooox":100,
    "oooo_":100,




    "": 0,
    "_": 0,
    "__": 0,
    "___": 0,
    "____": 0,
    "_____": 0,
    "x____": 1,
    "_x___": 1,
    "__x__": 1,
    "___x_": 1,
    "____x": 1,
}
df = pd.read_excel("TinhDiem.xlsx", sheet_name="Sheet1")
strdk1 = dict()


def tinhDiem(map1, luot):
    n = 20 * 20
    mm = np.array([0] * n)
    mm = np.reshape(mm, (20, 20))
    l = ""
    op = ""
    if luot == 1:
        l = "x"
        op = "o"
    else:
        l = "o"
        op = "x"

    for i in range(20):
        for j in range(20):
            # diem = 0
            if map1[i, j] == l:
                mm[i, j] = -1
            if map1[i, j] == op:
                mm[i, j] = -2

            if map1[i, j] == "_":

                for p in td:
                    u = i
                    v = j
                    ss = ""
                    for k in range(5):
                        u += p[0]
                        v += p[1]
                        if isValid(u, v):
                            ss = "".join((ss, map1[u, v]))
                        else:
                            break
                    # if "xxx" not in strdk1.keys():
                    # ss = ss.replace("_", " ").strip()
                    if ss in strdk1.keys():
                        mm[i, j] += strdk1[ss]



    mx = 0
    ind = []

    # for i in range(20):
    #     for j in range(20):
    #         if mm[i, j] == "x":
    #             mm[i, j] = "0"
    #         if mm[i, j] == "o":
    #             mm[i, j] = "0"
    #         # mm[i, j] = "0"

    for i in range(20):
        for j in range(20):
            if mx < mm[i, j]:
                mx = mm[i, j]
                ind.clear()
            if mx == mm[i, j]:
                ind.append((i, j))

    print("cham")
    print(mm)
    rd.shuffle(ind)
    return ind[0]


class App:
    # khởi tạo
    def __init__(self, hang: int, cot: int, dk: int):
        self._running = True  # chạy
        self._screen = None
        self.size = self.weight, self.height = cot * \
                                               CELL_WIDTH, hang * CELL_HIGHT  # kích thước màn hình
        self.dk = dk
        self.hang = hang
        self.cot = cot
        self.luot = 1
        self.win = False
        self.who = None
        m = []

        for i in range(hang):
            m.append(['_'] * cot)
        self.map = np.array(m)
        print(self.map)

    # khởi tạo game

    def on_init(self):
        pg.init()
        self._screen = pg.display.set_mode(
            self.size, pg.HWSURFACE | pg.DOUBLEBUF)
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
                if self.luot == 1 and self.map[row, col] == '_' and self.win != True:
                    self._screen.blit(x_img, (posx, posy))

                    self.map[row, col] = 'x'

                    self.win = checkWin(self.map, self.dk, self.luot)
                    if self.win:
                        self._screen.blit(x_win, (0, 0))
                        self.who = "x"
                        self._running = False
                    self.luot = 0
                # if self.luot == 0 and self.map[row, col] == None:
                if self.luot == 0 and self.win != True:

                    # while True:
                    #     col = rd.randint(0, 20 - 1)
                    #     row = rd.randint(0, 20 - 1)
                    #     if self.map[row, col] == '_':
                    #         break
                    nd = tinhDiem(self.map, 1)
                    col = nd[1]
                    row = nd[0]
                    posx = col * CELL_WIDTH + 1
                    posy = row * CELL_HIGHT + 1
                    self._screen.blit(o_img, (posx, posy))
                    self.map[row, col] = 'o'
                    self.win = checkWin(self.map, self.dk, self.luot)
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
        game_initiating_window(self._screen, self.weight,
                               self.height, self.cot, self.hang)
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
        # root = start()
        # set_str = json.loads(root.getvar("setting"))
        # setting = Setting(int(set_str["hang"]), int(set_str["cot"]))

        # dkk = setting.dk
        theApp = App(20, 20, 5)
        who = theApp.on_execute()

        from windows.Window2 import end
        # data["who"] = who
        r2 = end(who)
        choi_lai = r2.getvar("choi_lai")
        if choi_lai != "y":
            break


if __name__ == "__main__":
    for i in range(len(df["nd"])):
        strdk1[df["nd"][i]] = df["d"][i]
    main()
