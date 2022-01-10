import tkinter as tk
import os
import glob

def save(event):
    global name
    file_name = name.get()
    name.delete(0, "end")

    global img_label
    img_label.destroy()

    global file_list

    global i

    os.rename(file_list[i], file_name + ".png")

    i += 1

    global image 
    image = tk.PhotoImage(file=file_list[i])
    img_label = tk.Label(window, image=image)
    img_label.pack()

    label["text"] = i

file_list = glob.glob("chatcha*.png")
print(file_list)

window = tk.Tk()

window.title("Hi")
window.geometry("200x150")
window.resizable(False, False)

i=0

label=tk.Label(window, text=str(i))
label.pack()

image = tk.PhotoImage(file=file_list[i])
img_label = tk.Label(window, image=image)
img_label.pack()

name = tk.Entry(window)
name.place(x=30, y=80, width=150, height=25)
name.focus()

window.bind('<Return>', save)

window.mainloop()