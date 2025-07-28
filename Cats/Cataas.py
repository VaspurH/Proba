from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return None


def open_new_window():
    tag = tag_entry.get()
    url = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"

    new_window = Toplevel(window)  # Добавлен аргумент window как родитель
    new_window.title("Новый котик")
    new_window.geometry("600x520+1000+450")

    label = Label(new_window)
    label.pack()

    img = load_image(url)  # Исправлено: используем url с учетом тега
    if img:
        label.config(image=img)
        label.image = img


def exit_app():
    window.destroy()


# Главное окно
window = Tk()
window.title("Главное окно")
window.geometry("400x250+1000+450")

tag_entry = Entry(window)  # Добавлен родитель window
tag_entry.pack()

load_button = Button(window, text="Загрузить по тегу", command=open_new_window)  # Добавлен родитель window
load_button.pack()

# Меню в главном окне
menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Новый котик", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit_app)

window.mainloop()