import pygame as pg
import sys
import time
from pygame.locals import *

# khởi tạo biến toàn cầu

# lưu x hoặc o 
XO = 'x'

# người thắng
winner = None

# kiểm tra khi vẽ
draw = None

# chiều rộng màn hình
width = 400

# chiều cao màn hình
height = 400

# màu nền
white = (255, 255, 255)

# màu đường kẻ
line_color = (0, 0, 0)

# bảng 3x3 ô trông
board = [[None] * 3, [None] * 3, [None] * 3]

