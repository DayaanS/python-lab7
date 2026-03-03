from PIL import ImageTk
import tkinter as tk
import urllib.request
import requests

def random_img():
    response = requests.get('https://cataas.com/cat?json=true')
    result = response.json()
    url = result['url']
    return url

window = tk.Tk()
window.geometry('800x500')
window.title('Anime Girrrls')


url = random_img()
data = urllib.request.urlopen(url)
image = ImageTk.PhotoImage(data=data.read())
img_lbl = tk.Label(window, image=image)
img_lbl.pack()

# button
# gen_btn = tk.Button(frame,text= 'Random Image',command=lambda:random_img(bg_img))
# gen_btn.pack(side=tk.LEFT)

window.mainloop()


