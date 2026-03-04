import tkinter as tk
from PIL import ImageTk
import urllib.request
import requests

URL = 'https://cataas.com/cat'
params = {
    'type': 'square',
    'json': True,
}
window_w = 300
window_h = 300
pad = 20

def random_img():
    response = requests.get(URL, params=params)
    data = response.json()
    img_url = data['url']
    data = urllib.request.urlopen(img_url)
    img = ImageTk.PhotoImage(data=data.read())
    return img


def img_button():
    img = random_img()
    img_lbl.configure(image=img)
    img_lbl.img1 = img #fixes image not updating


window = tk.Tk()
window.geometry(f'{window_w}x{window_h}')
window.title('Cats!')

img1 = random_img()
img_lbl = tk.Label(window, image=img1)
img_lbl.pack(pady=pad)

btn = tk.Button(window, text='Next Cat!', command=img_button)
btn.pack(pady=pad)

window.mainloop()
