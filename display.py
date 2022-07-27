import time

start = time.time()

import argparse
import cv2

from matplotlib import pyplot as plt
from matplotlib.widgets import Button

import numpy as np

np.set_printoptions(precision=2)

NUM_HUMAN_FACES = 26
NUM_LEGO_MALE = 14
NUM_LEGO_FEMALE = 7
# NUM_ROWS = NUM_FACES-1
NUM_ROWS = 5

parser = argparse.ArgumentParser()
parser.add_argument('imgPath', type=str, nargs='+', help="Input images.")
args = parser.parse_args()

def readImg(imgPath):
    bgrImg = cv2.imread(imgPath)
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))
    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
    return rgbImg

path = args.imgPath[0]

def display(humanFace, legoFace1, legoFace2):
    fig = plt.figure()
    # plot target human face
    fig.add_subplot(2,2,1)
    plt.imshow(humanFace, interpolation="nearest")

    # plot the two lego faces available for selection
    fig.add_subplot(2,2,2)
    plt.imshow(legoFace1, interpolation="nearest")
    fig.add_subplot(2,2,4)
    plt.imshow(legoFace2, interpolation="nearest")
    plt.show()


display(humanFace=readImg(path+"human1.png"), legoFace1=readImg(path+"face0.png"),legoFace2=readImg(path+"face1.png"))