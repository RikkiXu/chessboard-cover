import tkinter as tk
import numpy as np
import math
import tkinter.messagebox

def START():
    global order
    start_x=int(var_x.get())
    start_y=int(var_y.get())
    start_size=pow(2,int(var_size.get()))
    window_chessboard = tk.Toplevel(window)
    window_chessboard.attributes("-topmost", True)
    window_chessboard.title('Chessboard')
    canvas1=tk.Canvas(window_chessboard,bg="white",height=200+start_size*50, width=200+start_size*50)
    canvas1.pack()
    for i in range(start_size):
        for j in range(start_size):
            canvas1.create_rectangle(50 + i * 50, 50 + j * 50, 100 + i * 50, 100 + j * 50, fill='white', outline="black")
    canvas1.update()
    size=start_size
    order=np.zeros((int(((start_size)**2-1)/3)+1,3),dtype=tuple)
    chess(0,0,start_x,start_y,size)
    drawboard(canvas1,order,start_size,start_x,start_y)


def drawboard(canvas1,order,start_size,start_x,start_y,startx=50,starty=50,cellwidth=50):
    global flag
    flag =0
    for i in range((order.shape)[0]):
        if i==0:
            canvas1.create_rectangle(50+start_x*50, 50+start_y*50, 100+start_x*50, 100+start_y*50,fill='black', outline="black")
            continue
        for j in range(3):
            color = hsv2rgb((i-1)*(360/order.shape[0]),0.6, 1-(i-1)*(0.3/order.shape[0]))
            cellx=startx+order[i][j][0]*50
            celly=starty+order[i][j][1]*50
            canvas1.create_rectangle(cellx,celly,cellx+cellwidth,celly+cellwidth,
                fill=color_rgb(color),outline="black")
            canvas1.create_text(cellx+cellwidth/2, celly+cellwidth/2, text=i)
        b=tkinter.messagebox.askyesno("askyesno","Next?")
        if (b):
            pass
        else:
            window.destroy()
    window.destroy()

def chess(tr, tc, pr, pc, size):
    global tile
    global order
    if size == 1:
        return  #递归终止条件
    tile += 1   #表示直角骨牌号
    count = tile
    half = size // 2  # 当size不等于1时，棋盘格规模减半，变为4个
    if (pr < tr + half) and (pc < tc + half):
        chess(tr, tc, pr, pc, half)
    else:
        for i in range(3):
            if (order[count][i] == 0):
                order[count][i] = (tr + half-1, tc + half - 1)
                break
        chess(tr, tc, tr + half - 1, tc + half - 1, half)
    if (pr < tr + half) and (pc >= tc + half):
        chess(tr, tc + half, pr, pc, half)
    else:
        for i in range(3):
            if (order[count][i] == 0):
                order[count][i] = (tr + half-1, tc + half )
                break
        chess(tr, tc + half, tr + half - 1, tc + half, half)

    if (pr >= tr + half) and (pc < tc + half):
        chess(tr + half, tc, pr, pc, half)
    else:
        for i in range(3):
            if(order[count][i]==0):
                order[count][i]=(tr + half,tc + half-1)
                break
        chess(tr + half, tc, tr + half, tc + half - 1, half)
    if (pr >= tr + half) and (pc >= tc + half):
        chess(tr + half, tc + half, pr, pc, half)
    else:
        for i in range(3):
            if(order[count][i]==0):
                order[count][i]=(tr+half,tc+half)
                break
        chess(tr + half, tc + half, tr + half, tc + half, half)

def color_rgb(value):
  digit = list(map(str, range(10))) + list("ABCDEF")
  if isinstance(value, tuple):
    string = '#'
    for i in value:
      a1 = i // 16
      a2 = i % 16
      string += digit[a1] + digit[a2]
    return string
  elif isinstance(value, str):
    a1 = digit.index(value[1]) * 16 + digit.index(value[2])
    a2 = digit.index(value[3]) * 16 + digit.index(value[4])
    a3 = digit.index(value[5]) * 16 + digit.index(value[6])
    return (a1, a2, a3)

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return (r, g, b)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Chessboard cover')
    window.geometry('500x400')
    canvas = tk.Canvas(window, height=100, width=500)
    canvas.place(x=10, y=20, anchor='nw')  # 放置画布（为上端）

    special_label_x = tk.Label(window,
                               text=r'x of the first piece:',  # 标签的文字
                               font=('Arial', 10),  # 字体和字体大小
                               width=20, height=2  # 标签长宽
                               ).place(x=100, y=100, anchor='nw')

    special_label_y = tk.Label(window,
                               text=r'y of the first piece:',  # 标签的文字
                               font=('Arial', 10),  # 字体和字体大小
                               width=20, height=2  # 标签长宽
                               ).place(x=100, y=160, anchor='nw')

    special_label_size = tk.Label(window,
                                  text=r'The board size:',  # 标签的文字
                                  font=('Arial', 10),  # 字体和字体大小
                                  width=20, height=2  # 标签长宽
                                  ).place(x=110, y=210, anchor='nw')
    var_x=tk.StringVar()
    var_y=tk.StringVar()
    var_size=tk.StringVar()
    entry_x=tk.Entry(window,textvariable=var_x,width=8).place(x=250,y=110,anchor='nw')
    entry_y=tk.Entry(window,textvariable=var_y,width=8).place(x=250,y=170,anchor='nw')
    entry_size=tk.Entry(window,textvariable=var_size,width=8).place(x=250,y=220,anchor='nw')
    tile=0
    tk.Button(window, font=('Arial', 10),width=15, height=2, bg='#FFD700', text='START',command=START).place(x=180,y=280,anchor='nw')
    window.mainloop()

