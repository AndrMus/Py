from pytube import YouTube
from tkinter import *

def music():
    path = 'C:/Users/Андрей/Music'
    music = YouTube(url.get()).streams[-1]
    music.download(path)
    quest = Label(root, text="Загрузка '" + YouTube(url.get()).title + "' завершена")
    quest.pack()

root = Tk()

url = Entry(root, width=70, borderwidth=4)
url.pack()

download = Button(root, text="ᐅ Download", command=music, font=('Helvetica', 15, 'bold'), fg="white", bg="red")

download.pack()

root.mainloop()
