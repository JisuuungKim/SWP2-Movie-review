import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("Mydesign.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Loadcloud.clicked.connect(self.loadImageFromFile_A)
        self.rB_action.clicked.connect(self.radiobuttonclicked_A)
        self.rB_comedy.clicked.connect(self.radiobuttonclicked_C)
        self.rB_fantasy.clicked.connect(self.radiobuttonclicked_F)
        self.rB_mello.clicked.connect(self.radiobuttonclicked_M)

    def loadImageFromFile_A(self) :
        #QPixmap 객체 생성 후 이미지 파일을 이용하여 QPixmap에 사진 데이터 Load하고, Label을 이용하여 화면에 표시

        MV = ["런","800","이웃사촌","그날이 온다","더 프롬","삼진그룹 영어토익반","프리키 데스데이 순한맛","미드나이트 스카이","극장판 바이올렛 에버가든","조제","노트북"]
        for title in MV :
            if self.MovieList.currentText() == title:
                self.ImageGet("./ADproject/"+title+".png")



    def radiobuttonclicked_A(self):
        #각각 버튼들이 눌릴 때 QComboBox에 장르에 따른 영화 리스트가 들어가게끔 함.
        Action_List = ["런", "800"]
        if self.rB_action.isChecked:
            self.MovieList.clear()
            for i in range(1,len(Action_List)+1):
                self.MovieList.addItem(Action_List[i-1])


    def radiobuttonclicked_C(self):
        Comedy_List = ["이웃사촌", "그날이 온다", "더 프롬", "삼진그룹 영어토익반", "프리키 데스데이 순한맛"]
        if self.rB_comedy.isChecked:
            self.MovieList.clear()
            for i in range(1,len(Comedy_List)+1):
                self.MovieList.addItem(Comedy_List[i-1])


    def radiobuttonclicked_F(self):
        Fantasy_List = ["미드나이트 스카이", "극장판 바이올렛 에버가든"]
        if self.rB_fantasy.isChecked:
            self.MovieList.clear()
            for i in range(1,len(Fantasy_List)+1):
                self.MovieList.addItem(Fantasy_List[i-1])


    def radiobuttonclicked_M(self):
        Mello_List = ["조제", "노트북"]
        if self.rB_mello.isChecked:
            self.MovieList.clear()
            for i in range(1,len(Mello_List)+1):
                self.MovieList.addItem(Mello_List[i-1])


    def ImageGet(self,png):
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(png)  # 여기에 사진파일을 넣어야함.
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
        self.Picture.setPixmap(self.qPixmapFileVar)




if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()