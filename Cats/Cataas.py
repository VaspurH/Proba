from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

window = TK()
window.title("Cats!")
window.geometr("600x480")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.img = img

window.mainloop()