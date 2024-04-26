import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import random
import time

def show_image_popup():
    '''
    popup = tk.Toplevel(root)
    popup.title("Всплывающее окно с картинкой")
    # Загрузка изображения
    image = Image.open("/home/student/Рабочий стол/caniiiiiii.gif")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(popup, image=photo)
    label.image = photo  # сохранение ссылки на изображение
    label.pack()
    открытие окна посредине экрана
    '''


    # Загрузка изображения
    image = Image.open("/home/student/Рабочий стол/caniiiiiii.gif")
    photo = ImageTk.PhotoImage(image)

    # Создание всплывающего окна
    popup = tk.Toplevel(root)
    popup.title("Всплывающее окно с картинкой")
    label = tk.Label(popup, image=photo)
    label.image = photo  # сохранение ссылки на изображение
    label.pack()

    # Размещение окна в случайном месте на экране
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = random.randint(0, screen_width-1520)  # Измените размеры окна, если нужно
    x1 = random.randint(1125, screen_width)

    y = random.randint(0, screen_height)  # Измените размеры окна, если нужно

    #
    #   400 окно 1125
    #

    x2 = [x,x1]
    xv = random.choice(x2)

    #popup.geometry(f"+{random.choice(x2)}+{random.choice(y2)}")
    popup.geometry(f"+{xv}+{y}")
    print(xv,y)

def asd():
    import tkinter as tkimport
    random
    from PIL import Image, ImageTk

    # Создание главного окна
    root = tk.Tk()
    root.title("Плавное появление окон")
    root.geometry('1x1+1+1')

    # Загрузка изображения
    image = Image.open("/home/student/Рабочий стол/caniiiiiii.gif")
    photo = ImageTk.PhotoImage(image)

    # Список для хранения окон
    windows = []

    # Функция для постепенного появления окон на экране
    def gradual_open():
        if windows:
            window = windows.pop(0)
            window.deiconify()
            root.after(100, gradual_open)  # Измените задержку, если нужно

    # Функция для создания окна с изображением в случайном месте экрана
    def create_window():
        window = tk.Toplevel(root)
        window.title("Окно с изображением")
        label = tk.Label(window, image=photo)
        label.pack()
        window.withdraw()  # Скрывает окно, чтобы оно появилось плавно
        windows.append(window)
        # Размещение окна в случайном месте на экране
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = random.randint(0, screen_width)  # Измените размеры окна, если нужно
        y = random.randint(0, screen_height)  # Измените размеры окна, если нужно
        window.geometry(f"+{x}+{y}")


    # Создание окон с изображением
    for _ in range(100):   # Измените количество окон, если нужно
        create_window()


    # Запуск постепенного появления окон
    gradual_open()

    # Запуск основного цикла обработки событий
    root.mainloop()

def show_popup():
    root.attributes("-topmost", True)  # Окно всегда наверху
    result = messagebox.askquestion("Всплывающее окно", "Привет, это всплывающее окно!", icon='info')
    if result == 'yes':
        root.destroy()  # Закрыть окно

        asd()
    else:
        show_image_popup()
        time.sleep(0.02)
        root.after(0, show_popup)# Моментальное открытие после закрытия

root = tk.Tk()
root.withdraw()  # Скрыть основное окно

# Создание кнопки
button = tk.Button(root, text="Закрыть окно", command=root.destroy)
button.pack()

# Запуск функции отображения всплывающего окна
root.after(0, show_popup)

root.mainloop()
