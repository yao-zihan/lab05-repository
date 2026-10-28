# -*- coding: utf-8 -*-
"""
满屏爱心弹窗 · 升级版（去漂浮 + 大爱心）

运行方式：在终端里执行
    python 满屏爱心弹窗升级版.py

改动说明：
- 去掉"从随机位置飘进来"的动画，小窗口直接凭空出现在爱心位置上。
- 爱心加大（scale 调大），且每个窗口以爱心点为中心对齐，形状更准、更对称。
"""
import tkinter as tk
import random
import math
import time

# ========== 可修改区域 ==========
name = input("这位小可爱，你的名字是：")
tips = [
    "多喝温水哦~", "保持开心", "好好爱自己", "万事顺意",
    "不许熬夜", "今天也要加油", "平安喜乐", "我在想你",
    "吃点好吃的", "一切都会越来越好"
]
main_text = f"{name}我喜欢你"
# 点我不轮换的提示文案
warn_text_list = [
    "不准选这个！",
    "再选一次试试？",
    "别闹，快点收到！"
]

colors = [
    "pink", "lightblue", "lavender",
    "lightgreen", "lightyellow", "hotpink"
]

scale = 24              # 爱心大小，越大爱心越大（原来是 14）
num_points = 100        # 组成爱心的小窗口数量，越多轮廓越密
win_w, win_h = 220, 80  # 每个小窗口的宽、高
appear_interval = 0.05  # 窗口依次出现的间隔（秒），设成 0 则全部同时出现
stay_time = 3.0
fade_steps = 60
# ================================

warn_index = 0  # 记录当前警告文字下标

def get_heart_points(center_x, center_y, scale=14, num_points=100):
    pts = []
    for i in range(num_points):
        t = 2 * math.pi * i / num_points
        x = 16 * (math.sin(t) ** 3)
        y = 13 * math.cos(t) - 5 * math.cos(2*t) \
            - 2 * math.cos(3*t) - math.cos(4*t)
        px = center_x + x * scale
        py = center_y - y * scale
        pts.append((px, py))
    pts.sort(key=lambda p: (-p[0], p[1]))
    return pts

def fade_out_all(windows, main_win=None, step=0, max_step=60):
    if step >= max_step:
        for w in windows:
            try:
                w.destroy()
            except:
                pass
        if main_win is not None:
            try:
                main_win.destroy()
            except:
                pass
        root.destroy()
        return
    alpha = max(0.0, 1.0 - step / max_step)
    for w in windows:
        try:
            w.attributes("-alpha", alpha)
        except:
            pass
    if main_win is not None:
        try:
            main_win.attributes("-alpha", alpha)
        except:
            pass
    root.after(30, fade_out_all, windows, main_win, step + 1, max_step)

def on_close(win, tx, ty):
    win.destroy()
    new_win = tk.Toplevel(root)
    new_win.title("温馨提示")
    new_win.wm_attributes("-topmost", True)
    new_win.attributes("-alpha", 1.0)
    bgc = random.choice(colors)
    tk.Label(new_win, text=random.choice(tips),
             bg=bgc, font=("微软雅黑", 13)).pack(expand=True)
    # 直接出现在爱心点位上（居中）
    new_win.geometry(f"{win_w}x{win_h}+{int(tx - win_w / 2)}+{int(ty - win_h / 2)}")
    new_win.protocol("WM_DELETE_WINDOW",
                     lambda ww=new_win, xx=tx, yy=ty: on_close(ww, xx, yy))
    win_list.append(new_win)

def start_heart():
    confirm_win.destroy()
    for target_x, target_y in heart_points:
        w = tk.Toplevel(root)
        w.title("温馨提示")
        w.wm_attributes("-topmost", True)
        w.attributes("-alpha", 1.0)
        bgc = random.choice(colors)
        tk.Label(w, text=random.choice(tips),
                 bg=bgc, font=("微软雅黑", 13)).pack(expand=True)
        # 直接凭空出现在爱心点位上（居中）
        w.geometry(f"{win_w}x{win_h}+{int(target_x - win_w / 2)}+{int(target_y - win_h / 2)}")
        w.protocol("WM_DELETE_WINDOW",
                   lambda ww=w, xx=target_x, yy=target_y: on_close(ww, xx, yy))
        win_list.append(w)
        root.update()
        time.sleep(appear_interval)
    time.sleep(stay_time)
    main_win = tk.Toplevel(root)
    main_win.wm_attributes("-topmost", True)
    main_win.attributes("-alpha", 1.0)
    main_win.geometry(f"400x180+{int(cx - 200)}+{int(cy - 90)}")
    main_win.title("❤")
    tk.Label(main_win, text=main_text,
             bg="#ff6699", fg="white",
             font=("微软雅黑", 22, "bold")).pack(expand=True)
    root.after(100, fade_out_all, win_list, main_win, 0, fade_steps)

def show_warn():
    global warn_index
    confirm_win.destroy()
    warn_win = tk.Toplevel(root)
    warn_win.title("提示")
    warn_win.wm_attributes("-topmost", True)
    warn_win.geometry("280x120+{}+{}".format(int(cx - 140), int(cy - 60)))
    warn_win.resizable(False, False)
    tk.Label(warn_win, text=warn_text_list[warn_index],
             font=("微软雅黑", 14), pady=20).pack()
    # 下标循环，到最后回到0
    warn_index = (warn_index + 1) % len(warn_text_list)
    def back():
        warn_win.destroy()
        show_confirm()
    tk.Button(warn_win, text="好吧", width=10,
              bg="#ff6699", fg="white",
              command=back).pack(pady=5)

def show_confirm():
    global confirm_win
    confirm_win = tk.Toplevel(root)
    confirm_win.title("每日提醒")
    confirm_win.wm_attributes("-topmost", True)
    confirm_win.geometry("320x140+{}+{}".format(int(cx - 160), int(cy - 70)))
    confirm_win.resizable(False, False)
    tk.Label(confirm_win, text="每天都要保持好心情！",
             font=("微软雅黑", 14), pady=20).pack()
    btn_frame = tk.Frame(confirm_win)
    btn_frame.pack(pady=5)
    tk.Button(btn_frame, text="我不", width=10, bg="#cccccc",
              command=show_warn).grid(row=0, column=0, padx=15)
    tk.Button(btn_frame, text="收到", width=10, bg="#ff6699", fg="white",
              command=start_heart).grid(row=0, column=1, padx=15)

root = tk.Tk()
root.withdraw()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
cx, cy = screen_w / 2, screen_h / 2 - 60
heart_points = get_heart_points(cx, cy, scale, num_points)
win_list = []

show_confirm()
root.mainloop()
