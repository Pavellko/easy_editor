from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap # закидывает картинку в label
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter
from PIL.ImageFilter import *
import glob

app = QApplication([])
ui = uic.loadUi("inter.html")
ui.show()

def open(): # находим файлы и помещаем в список
     dir = QFileDialog.getExistingDirectory( )
     spisok_files = []     
     files_1 = glob.glob(dir + '/*.jpg')
     files_2 = glob.glob(dir + '/*.png')
     files_3 = glob.glob(dir + '/*.bmp')
     spisok_files = files_1 + files_2 + files_3
     ui.listWidget.addItems(spisok_files)

def show(): # показываем оригинальное фото
     global pic
     filename = ui.listWidget.currentItem().text()
     ui.label.hide()
     pic = Image.open(filename)
     pixmapimage = QPixmap(filename)
     w, h = ui.label.width(), ui.label.height()
     pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
     ui.label.setPixmap(pixmapimage)
     ui.label.show()

def bw(): #переводим в черно-белое
     global pic
     pic_bw = pic.convert("L")
     pic_bw.save('gray.jpg')
     pixmapimage = QPixmap('gray.jpg')
     w, h = ui.label.width(), ui.label.height()
     pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
     ui.label.setPixmap(pixmapimage)
     ui.label.show()

def povorot(): #поворачиваем
     global pic
     pic_povorot = pic.transpose(Image.ROTATE_90)
     pic_povorot.save('povorot.jpg')
     pixmapimage = QPixmap('povorot.jpg')
     w, h = ui.label.width(), ui.label.height()
     pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
     ui.label.setPixmap(pixmapimage)
     ui.label.show()

#дописываем функции def на каждую операцию с фото
#def operation():
     ...

ui.pushButton.clicked.connect(open)
ui.pushButton_3.clicked.connect(bw)
ui.pushButton_4.clicked.connect(povorot)
ui.listWidget.currentRowChanged.connect(show)
# привязываем кнопки по аналогии

app.exec_()