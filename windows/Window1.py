import time
from tkinter import *
from models.Setting import Setting
import json


# xử lý sự kiện nút



# khởi tạo màn hình
def start():
    def vao_game():
        s = Setting(hang.get(), cot.get(), dkt.get())
        j = json.dumps(s.__dict__)
        # f = open("setting.json", "w")
        # f.write(j)
        # f.close()
        root.setvar("setting", j)
        root.destroy()
        return s
    root = Tk()
    root.geometry("250x250")
    # tạo số mặc định
    hang = StringVar(root)
    cot = StringVar(root)
    dkt = StringVar(root)
    hang.set("3")
    cot.set("3")
    dkt.set("3")
    # tên chính
    l = Label(root, text="Cài đặt chung")
    # label cho chọn
    lb_chon_hang = Label(root, text="Chọn số hàng")
    lb_chon_cot = Label(root, text="Chọn số cột")
    lb_chon_win = Label(root, text="Chọn luật thắng")
    # chọn số hàng và cột luật thắng
    chon_so_hang = Spinbox(root, from_=3, to=10, textvariable=hang)
    chon_so_cot = Spinbox(root, from_=3, to=10, textvariable=cot)
    chon_so_win = Spinbox(root, from_=3, to=10, textvariable=dkt)

    # vào game
    b1 = Button(root, text="Vào game", command=vao_game)

    # thoát game
    b2 = Button(root, text="Thoát",
                command=root.destroy)

    # hiển thị trên màn hình
    l.pack()
    lb_chon_hang.pack()
    chon_so_hang.pack()
    lb_chon_cot.pack()
    chon_so_cot.pack()
    lb_chon_win.pack()
    chon_so_win.pack()
    b1.pack()
    b2.pack()


    root.mainloop()
    return root
