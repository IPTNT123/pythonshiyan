import tkinter as tk
from PIL import Image, ImageTk

import color_identify
import picture_identify

global cut,imgs
global txt
global image_file
global canvas
global c_canvas
global position
window = tk.Tk()
position = 110
txt = '0'

#给窗口的可视化起名字
window.title('车牌检测')

#设定窗口的大小(长 * 宽)
window.geometry('600x800')


#放置各种元素
canvas = tk.Canvas(window, height=500, width=250)
c_canvas = tk.Canvas(window, height=500, width=270)
e_k = tk.Label(window, text='输入照片全称：', font=('Arial', 12), width=27, height=2)
e_k.pack()
e = tk.Entry(window, show=None, font=('Arial', 14))
e.pack()
l = tk.Label(window, text='原图', bg='red' ,font=('Arial', 12), width=27, height=2)
l.pack(anchor="center")
l.place(x=150,y=100)
k = tk.Label(window, text='车牌提取',bg='red',font=('Arial', 12), width=27, height=2)
k.pack(anchor="center")
k.place(x=150,y=500)



# 触发
def check():
    global cut
    global image_file
    global canvas
    global imgs
    global c_canvas
    global position
    txt = e.get()
    list = color_identify.color_identify(txt)
    img = Image.open(txt)
    img = img.resize((300, 300))

    image_file = ImageTk.PhotoImage(img)  # 图片位置
    image = canvas.create_image(150, 110, anchor='n', image=image_file)  # 图片锚定点
    canvas.pack(side='top')

    #判断是否有读取到车牌
    if(len(list) < 3):
        list = picture_identify.picture_identify(txt)

    # 设置截取图片
    imgs = Image.open('pai.jpg')
    imgs = imgs.resize((250, 100))
    cut = ImageTk.PhotoImage(imgs)
    c_image = c_canvas.create_image(140, 0, anchor='n', image=cut)  # 图片锚定点
    c_text = c_canvas.create_text(140, position, text=list)
    position = position + 15
    c_canvas.pack(side='top')

# 定义一个按钮用来移动指定图形的在画布上的位置
b = tk.Button(window, text='运行', bg='red',command=check).pack(side="bottom")

# 主窗口循环显示
window.mainloop()