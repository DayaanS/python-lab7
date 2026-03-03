import tkinter as tk
from PIL import ImageTk
import urllib.request
import requests


def random_img():
    response = requests.get('https://cataas.com/cat?type=square&json=true')
    result = response.json()
    url = result['url']
    data = urllib.request.urlopen(url)
    img = ImageTk.PhotoImage(data=data.read())
    return img


def img_button():
    img = random_img()
    img_lbl.configure(image=img)
    img_lbl.img1 = img #fixes image not updating


window = tk.Tk()
window.geometry('960x640')
window.title('Cats!')

img1 = random_img()
img_lbl = tk.Label(window, image=img1)
img_lbl.pack(fill=tk.BOTH, expand=True,)

btn = tk.Button(window, text='Next Cat!', command=img_button)
btn.pack(side ='bottom', pady=20)

window.mainloop()
