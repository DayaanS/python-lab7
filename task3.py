import tkinter as tk
from PIL import ImageTk
import urllib.request
import requests

url = 'https://cataas.com/cat'
params = {
    'type': 'square',
    'json': True,
}


def random_img():
    response = requests.get(url, params=params)
    result = response.json()
    img_url = result['url']
    data = urllib.request.urlopen(img_url)
    img = ImageTk.PhotoImage(data=data.read())
    return img


def img_button():
    img = random_img()
    img_lbl.configure(image=img)
    img_lbl.img1 = img #fixes image not updating


window = tk.Tk()
window.geometry('300x300')
window.title('Cats!')

img1 = random_img()
img_lbl = tk.Label(window, image=img1)
img_lbl.pack(pady=20)

btn = tk.Button(window, text='Next Cat!', command=img_button)
btn.pack(pady=20)

window.mainloop()
