import time
from tkinter import *
from models.Setting import Setting
import json





# khởi tạo màn hình
def end(who):
    root = Tk()
    
    def vao_game():
        root.setvar("choi_lai", "y")
        root.destroy()
    def no():
        root.setvar("choi_lai", "n")
        root.destroy()


    root.geometry("250x250")
    lb_win = None
    # who = root.getvar("who")
    if who == "x":
        lb_win = Label(root, text="Bạn đã thắng")
    else:
        lb_win = Label(root, text="Bạn hãy cố lên")

    btn_choi_lai = Button(root, text="Chơi lại", command=vao_game)
    btn_thoat = Button(root, text="Thoát", command=no)

    lb_win.pack()   
    btn_choi_lai.pack()
    btn_thoat.pack()
    root.mainloop()
    return root