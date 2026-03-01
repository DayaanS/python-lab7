from PIL import ImageTk, Image
import tkinter as tk
import urllib.request
import requests

def random_img():
    response = requests.get("https://nekos.best/api/v2/neko")
    result = response.json()
    return result["results"][0]["url"]


def url_to_img():
   url = random_img()
   with urllib.request.urlopen(url) as u:
      raw_data = u.read()

   image = Image.open(io.BytesIO(raw_data))
   photo = ImageTk.PhotoImage(image)
   return photo 


   # Create a label widget to display the image
#    label = tk.Label(root, image=photo)
#    label.pack()

def init_gui():
    window = tk.Tk()
    window.geometry('800x500')
    window.title('Anime Girrrls')

    # background image
    url = random_img()
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    image = Image.open(io.BytesIO(raw_data))
    photo = ImageTk.PhotoImage(image)
    bg_lbl = tk.Label(window, image=photo)
    bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

    # frame
    frame = tk.Frame(window)
    frame.place(relx=0.5, rely=0.5, anchor='center')

    # button
    # gen_btn = tk.Button(frame,text= 'Random Image',command=lambda:random_img(bg_img))
    # gen_btn.pack(side=tk.LEFT)

    window.mainloop()


if __name__ == '__main__':
    init_gui()

