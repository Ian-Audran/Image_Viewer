import sys
from random import randint
from PIL import Image

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QDesktopWidget,
    QGridLayout,
    QGroupBox,
)
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtGui, QtWidgets, QtCore
#import menu_widget

image_path = "pictures/4-Wisdom.jpg"
PixelMax = 500
image = Image.open(image_path)
imageW, imageH = image.size
imageW, imageH = imageW // 100, imageH // 100
PSize = 0
for i in range(100):
    PSize += 1
    if imageH * PSize > PixelMax:
        break

imageW, imageH = imageW * PSize, imageH * PSize

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        # <MainWindow Properties>
        self.setFixedSize(imageW, imageH)
        self.setStyleSheet("QFrame{\n" "    background-color: rgb(0, 0, 0);\n" "    color: rgb(0, 0, 0);\n" "}")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()
        self.setAcceptDrops(True)
        # </MainWindow Properties>

        # <Label Properties>
        self.lbl = QLabel(self)
        self.lbl.setText("")
        self.lbl.setPixmap(QtGui.QPixmap(image_path))
        self.lbl.setScaledContents(True)
        #self.lbl.setStyleSheet("QFrame{\n" "    background-color: rgb(0, 0, 0);\n" "    color: rgb(0, 0, 0);\n" "}")
        self.lbl.setGeometry(0, 0, imageW, imageH)
        # </Label Properties>

        self.oldPos = self.pos()

        #self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            #for i in range(len(event.mimeData().urls())):
            #    print(event.mimeData().urls()[i].toLocalFile())
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)

            event.accept()
        else:
            event.ignore()

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def set_image(self, image_path):
        PixelMax = 500
        image = Image.open(image_path)
        imageW, imageH = image.size
        imageW, imageH = imageW // 100, imageH // 100
        PSize = 0
        for i in range(100):
            PSize += 1
            if imageH * PSize > PixelMax:
                break

        imageW, imageH = imageW * PSize, imageH * PSize

        self.setFixedSize(imageW, imageH)
        self.lbl.setPixmap(QtGui.QPixmap(image_path))
        self.lbl.setGeometry(0, 0, imageW, imageH)
        print(imageH, imageW)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()

        # self.MenuWindow = QtWidgets.QWidget()

        self.setObjectName("MenuWindow")
        self.resize(750, 500)
        self.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0.30, y2:0.30, stop:0 rgba(183, 0, 255, 200), stop:1 rgba(255, 255, 255, 255));\n" "\n" "")
        self.setMinimumSize(QtCore.QSize(500, 350))
        self.setAcceptDrops(True)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_frame = QtWidgets.QFrame(self)
        self.main_frame.setStyleSheet("")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_frame)

        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image_select_frame = QtWidgets.QFrame(self.main_frame)
        self.image_select_frame.setStyleSheet("background-color: rgb(200, 200, 200);\n" "border-radius: 15px;")
        self.image_select_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image_select_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_select_frame.setObjectName("image_select_frame")
        self.verticalLayout_2.addWidget(self.image_select_frame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.image_select_frame)
        self.image_select_frame.image_list = []

        self.controls_frame = QtWidgets.QFrame(self.main_frame)
        self.controls_frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.controls_frame.setStyleSheet("background-color: rgb(100, 100, 100);\n" "border-radius: 15px;")
        self.controls_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.controls_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controls_frame.setObjectName("controls_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.controls_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_previous = QtWidgets.QPushButton(self.controls_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_previous.setFont(font)
        self.btn_previous.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.35, x2:0.8, y2:0, stop:0 rgba(183, 0, 255, 200), stop:1 rgba(255, 255, 255, 255));\n" "")
        self.btn_previous.setObjectName("btn_previous")
        self.horizontalLayout.addWidget(self.btn_previous)

        self.btn_play_pause = QtWidgets.QPushButton(self.controls_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_play_pause.setFont(font)
        self.btn_play_pause.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.35, x2:0.8, y2:0, stop:0 rgba(183, 0, 255, 200), stop:1 rgba(255, 255, 255, 255));\n" "")
        self.btn_play_pause.setObjectName("btn_play_pause")
        self.horizontalLayout.addWidget(self.btn_play_pause)

        self.btn_next = QtWidgets.QPushButton(self.controls_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_next.setFont(font)
        self.btn_next.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0.35, x2:0.8, y2:0, stop:0 rgba(183, 0, 255, 200), stop:1 rgba(255, 255, 255, 255));\n" "")
        self.btn_next.setObjectName("btn_next")


        self.horizontalLayout.addWidget(self.btn_next)
        self.verticalLayout_2.addWidget(self.controls_frame)
        self.verticalLayout.addWidget(self.main_frame)

        #self.label1 = QtWidgets.QLabel(self.image_select_frame)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

        self.btn_play_pause.clicked.connect(self.play_pause)
        self.btn_next.clicked.connect(self.next_button)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "LazyInnovations Viewer"))
        self.btn_previous.setText(_translate("MenuWindow", "previous"))
        self.btn_play_pause.setText(_translate("MenuWindow", "play/pause"))
        self.btn_next.setText(_translate("MenuWindow", "next"))

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.window1.close()
        self.close()

    def dropEvent(self, event):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            for i in range(len(event.mimeData().urls())):
                self.image_select_frame.image_list.append(event.mimeData().urls()[i].toLocalFile())

                PixelMax = 125
                image = Image.open(self.image_select_frame.image_list[-1])
                imageW, imageH = image.size
                imageW, imageH = imageW // 100, imageH // 100
                PSize = 0
                for p in range(100):
                    PSize += 1
                    if imageW * PSize > PixelMax:
                        break

                imageW, imageH = imageW * PSize, imageH * PSize
                print(imageH, imageW)
                #image.size = (imageW, imageH)

                self.imagelabel2 = QLabel(self)
                self.imagelabel2.setPixmap(QtGui.QPixmap(event.mimeData().urls()[i].toLocalFile()).scaled(imageW, imageH))
                self.horizontalLayout_2.addWidget(self.imagelabel2)

            print(self.image_select_frame.image_list)



            event.accept()
        else:
            event.ignore()

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def play_pause(self, checked):
        if self.window1.isVisible():
            self.window1.hide()
        else:
            self.window1.show()

    def next_button(self):
        pass
        #self.labeltest = QtWidgets.QLabel(self.image_select_frame)
        #self.labeltest.setText("TEST")

app = QApplication(sys.argv)
w = MainWindow()
#w.show()
app.exec()