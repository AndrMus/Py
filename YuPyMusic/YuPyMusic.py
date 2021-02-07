from pytube import YouTube

#print("Введите путь до директории загрузки:")
#path = input()

path = 'C:/Users/Андрей/Music'

while True:

    print("Введите ссылку:")
    url = input()

    print()
    print("Название:")
    print(YouTube(url).title)
    print()

    print("Желаете скачать данный файл? (y/n)")
    confirm = input()
    if (confirm == 'y'):
        music = YouTube(url).streams[-1]
        music.download(path)
    print("Завершить работу? (y/n)")
    confirm = input()
    if (confirm == 'y'):
       break

