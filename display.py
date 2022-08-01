import time

start = time.time()

import argparse
import cv2

from matplotlib import pyplot as plt
from matplotlib.widgets import Button, RadioButtons

import numpy as np

np.set_printoptions(precision=2)

NUM_HUMAN_FACES = 26

parser = argparse.ArgumentParser()
parser.add_argument('imgPath', type=str, nargs='+', help="Input images.")
args = parser.parse_args()
path = args.imgPath[0]

class Face:
    def __init__(self, img, num):
        self.img = img
        self.num = num
#
# class Choice:
#     def register(self, event):


def readImg(imgPath):
    bgrImg = cv2.imread(imgPath)
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
    return rgbImg

def register_choice(label):
    # registers the user choice, for now only output the choice
    print("Clicked " + label)

def display(humanFace, legoFace1, legoFace2):
    fig = plt.figure()
    # plot target human face
    fig.add_subplot(2,2,1)
    plt.imshow(humanFace.img, interpolation="nearest")

    # plot the two lego faces available for selection
    fig.add_subplot(2,2,2)
    plt.imshow(legoFace1.img, interpolation="nearest")
    fig.add_subplot(2,2,4)
    plt.imshow(legoFace2.img, interpolation="nearest")
    radio = RadioButtons(plt.axes([0.9,0.3,0.1,0.5]), (str(legoFace1.num), str(legoFace2.num)))
    radio.on_clicked(register_choice)

    plt.show()


display(Face(readImg(path+"human1.png"),1), Face(readImg(path+"face0.png"),0),Face(readImg(path+"face1.png"),1))