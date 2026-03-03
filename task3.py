from PIL import ImageTk
import tkinter as tk
import urllib.request
import requests

# def random_img():
#     response = requests.get("https://nekos.best/api/v2/neko")
#     result = response.json()
#     return result["results"][0]["url"]


# def url_to_img():
#    url = random_img()
#    with urllib.request.urlopen(url) as u:
#       raw_data = u.read()

#    image = Image.open(io.BytesIO(raw_data))
#    photo = ImageTk.PhotoImage(image)
#    return photo 


   # Create a label widget to display the image
#    label = tk.Label(root, image=photo)
#    label.pack()

window = tk.Tk()
window.geometry('800x500')
window.title('Anime Girrrls')

# background image

# url = random_img()
url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fstatic.zerochan.net%2FHatsune.Miku.full.4422053.jpg&f=1&nofb=1&ipt=212af65cb04b76c3b10970b2893f56131dd2db29b54d4504b8e5554dfc0daf4b"
data = urllib.request.urlopen(url)
image = ImageTk.PhotoImage(data=data.read())


img_lbl = tk.Label(window, image=image)
img_lbl.pack()



# frame = tk.Frame(window)
# frame.place(relx=0.5, rely=0.5, anchor='center')

# button
# gen_btn = tk.Button(frame,text= 'Random Image',command=lambda:random_img(bg_img))
# gen_btn.pack(side=tk.LEFT)

window.mainloop()


