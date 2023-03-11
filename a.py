import sys
import subprocess
from random import randint, choice, shuffle
import threading
import os

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
    subprocess.check_call(
        [sys.executable, '-m', 'pip', 'install', 'pyautogui'])


def __():
    from playsound import playsound
    playsound('./a.mp3')


def ___():
    from PIL import Image
    from PIL import GifImagePlugin
    for i in range(randint(1, 8)):
        img_links = ['./images/{}'.format(x)
                     for x in os.listdir("./images") if x != "gifs"]
        rand_img_path = choice(img_links)
        img = Image.open(rand_img_path)
        img.show()


def _____():
    from PIL import Image
    from urllib.request import urlopen
    import webbrowser

    webbrowser.open(choice(gif_links))

    try:
        os.system("open /Applications/Safari.app {}".format(gif_links[0]))
    except Exception:
        pass


def _______():
    name = ["g", "o", "t", "t", "e", "m", '☢', '☸', '★', '⚡', '⛓']
    shuffle(name)
    try:
        os.mkdir("./a")
    except Exception:
        pass
    for i in range(randint(1, 10)):
        with open("./a/{}{}.txt".format(''.join(name), i), "w+") as f:
            f.write("gottem" * (i + randint(1, 100)) * randint(50, 150))


def ________():
    import webbrowser
    for i in range(randint(1, 8)):
        webbrowser.open(
            'https://shattereddisk.github.io/rickroll/rickroll.mp4', new=1, autoraise=True)


def _________():
    import pyautogui
    import math
    R = 400
    (x, y) = pyautogui.size()
    (X, Y) = pyautogui.position(x / 2, y / 2)
    pyautogui.moveTo(X+R, Y)
    for i in range(360):
        if i % 30 == 0:
            pyautogui.moveTo(X + R * math.cos(math.radians(i)),
                             Y + R * math.sin(math.radians(i)))


def __________():
    import pyautogui
    pyautogui.write("Demontime Daniels Strikes again!!", interval=0.05)


def ____________():
    import subprocess
    from random import shuffle
    import time
    import signal
    strs = list(
        '0000000000000000000000000000000000000011111111111111111111111111111111111111111111111111111111111111111111111111111100000000000000000000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111100000000000000000000000000000000000000111111111111111111111111111111111111111111111111111111111111111111111111111111000000000000000000000000000000000000000000000000000000000000000000000000111111111111111111111111111111111111111')
    shuffle(strs)
    subprocess.call(
        'echo {}'.format(''.join(strs) * randint(3, 5)), shell=True)


def _____________():
    from playsound import playsound
    playsound('./b.mp3')
