import os

from tkinter import *
from tkinter import ttk

import keyboard as keyboard

from pystray import MenuItem as item
import pystray

from PIL import Image


def closeWinCC():
    os.system("taskkill /f /im  win32calc.exe")


def restartWin():
    os.system("shutdown /r /t 0 /f")


def shutdownWin():
    os.system("shutdown /s /t 0")


def quitWindow():
    icon.stop()
    root.destroy()


def showWindow():
    icon.stop()
    root.after(0, root.deiconify)


def withdraw_window():
    global icon
    root.withdraw()
    image = Image.open("ico.png")
    menu = (item('Показать', showWindow, default=True), item('Выход', quitWindow))
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()


if __name__ == '__main__':
    root = Tk()
    root.title("OSRestarter")
    root.geometry("120x100")
    icon: pystray.Icon = None
    keyboard.add_hotkey('Ctrl + 1', showWindow)

    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    frame.pack(fill=BOTH)

    buttons = (ttk.Button(frame, text="Закрыть WinCC", command=closeWinCC),
               ttk.Button(frame, text="Перезагрузить ПК", command=restartWin),
               ttk.Button(frame, text="Выключить ПК", command=shutdownWin))
    for button in buttons:
        button.pack(fill=X)

    root.protocol('WM_DELETE_WINDOW', withdraw_window)

    root.attributes('-toolwindow', True)
    root.attributes("-topmost", True)
    root.resizable(False, False)
    root.mainloop()
