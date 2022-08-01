import sys
import csv
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

NUM_SEQUENCES = 50

def getSequence(path):
    seq = []
    with open(path+"seq.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            seq.append((int(row[0]), int(row[1])))
    return seq


class AssessmentWindow(QWidget):
    def __init__(self, imgPath, humanNo, seq, seqNum):
        super().__init__()
        self.imgPath = imgPath
        self.humanNo = humanNo
        self.leftBtn = None
        self.rightBtn = None
        self.seq = seq
        self.seqNum = seqNum
        self.leftLegoNo, self.rightLegoNo = seq[seqNum]
        self.go()


    def go(self):
        self.setGeometry(400, 0, 500, 800)
        self.setWindowTitle("Preference")

        vOuter = QVBoxLayout()
        vOuter.addStretch(1)
        vOuter.addLayout(self.display_human(imgPath))
        vOuter.addLayout(self.display_lego(imgPath))
        vOuter.addStretch(1)

        self.setLayout(vOuter)
        self.show()


    def writeResult(self, result):
        with open(self.imgPath+"result.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(result)


    def next(self):
        if self.seqNum < NUM_SEQUENCES - 1:
            newWindow = AssessmentWindow(self.imgPath, humanNo=self.humanNo,
                                         seq=self.seq, seqNum=self.seqNum+1)


    def register(self, leftClicked):
        if leftClicked:
            print("left")
            self.writeResult((self.leftLegoNo, self.rightLegoNo))
            self.next()
            self.close()
            pass
        else:
            print("right")
            self.writeResult((self.rightLegoNo, self.leftLegoNo))
            self.next()
            self.close()
            pass


    def display_lego(self, imgPath):
        self.leftBtn = QPushButton("left", self)
        self.rightBtn = QPushButton("right", self)

        self.leftBtn.clicked.connect(lambda : self.register(True))
        self.rightBtn.clicked.connect(lambda : self.register(False))

        vBox1 = QVBoxLayout()
        label = QLabel(self)
        png = QPixmap(imgPath + "lego_male/face" + str(self.leftLegoNo) + ".png")
        label.setPixmap(png)
        vBox1.addStretch(1)
        vBox1.addWidget(label)
        vBox1.addWidget(self.leftBtn)
        vBox1.addStretch(1)

        vBox2 = QVBoxLayout()
        label = QLabel(self)
        png = QPixmap(imgPath + "lego_male/face" + str(self.rightLegoNo) + ".png")
        label.setPixmap(png)
        vBox2.addStretch(1)
        vBox2.addWidget(label)
        vBox2.addWidget(self.rightBtn)
        vBox2.addStretch(1)

        hBoxFaces = QHBoxLayout()
        hBoxFaces.addStretch(1)
        hBoxFaces.addLayout(vBox1)
        hBoxFaces.addLayout(vBox2)
        hBoxFaces.addStretch(1)

        hBoxLabel = QHBoxLayout()
        hBoxLabel.addStretch(1)
        label = QLabel(self)
        label.setText("Session " + str(self.seqNum) + ": Choose the one you think is the best match!")
        hBoxLabel.addWidget(label)
        hBoxLabel.addStretch(1)

        vOuter = QVBoxLayout()
        vOuter.addStretch(1)
        vOuter.addLayout(hBoxLabel)
        vOuter.addLayout(hBoxFaces)
        vOuter.addStretch(1)

        return vOuter


    def display_human(self, imgPath):
        vBox = QVBoxLayout()
        img = QLabel(self)
        png = QPixmap(imgPath+"human"+ str(self.humanNo) +".png", "1")
        img.setPixmap(png.scaledToHeight(400))

        label = QLabel(self)
        label.setText("Target Face:")

        vBox.addStretch(1)
        vBox.addWidget(label)
        vBox.addWidget(img)
        vBox.addStretch(1)

        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addLayout(vBox)
        hBox.addStretch(1)

        return hBox


if __name__ == "__main__":
    app = QApplication(sys.argv)
    imgPath = sys.argv[1]
    # print(imgPath)

    window = AssessmentWindow(imgPath, humanNo=0, seq=getSequence(imgPath), seqNum=0)

    sys.exit(app.exec_())