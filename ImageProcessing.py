##Object Oriented Programming 2 Final Assignment
#
# Author: Öznur Çalışkan
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QKeySequence, QImage
from PyQt5.QtWidgets import QUndoStack, QMessageBox, QFileDialog, QMainWindow, QAction, qApp, QApplication, QDesktopWidget, QDateTimeEdit

from skimage.color import rgb2gray
from skimage.color import rgb2hsv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
#from skimage.filters import threshold_multiotsu
from skimage import img_as_float
from skimage.segmentation import (morphological_chan_vese,
                                  morphological_geodesic_active_contour,
                                  inverse_gaussian_gradient,
                                  checkerboard_level_set)
from skimage.segmentation import chan_vese 
from skimage import filters

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 500)
        MainWindow.setMinimumSize(QtCore.QSize(850, 500))
        MainWindow.setMaximumSize(QtCore.QSize(868, 500))
        
        self.Central_Widget = QtWidgets.QWidget(MainWindow)
        self.Central_Widget.setObjectName("Central_Widget")
        self.gridLayout = QtWidgets.QGridLayout(self.Central_Widget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.SourceImage_GroupBox = QtWidgets.QGroupBox(self.Central_Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SourceImage_GroupBox.sizePolicy().hasHeightForWidth())
        self.SourceImage_GroupBox.setSizePolicy(sizePolicy)
        self.SourceImage_GroupBox.setMinimumSize(QtCore.QSize(425, 250))
        self.SourceImage_GroupBox.setMaximumSize(QtCore.QSize(425, 250))
        self.SourceImage_GroupBox.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.SourceImage_GroupBox.setObjectName("SourceImage_GroupBox")
        self.SourceImage_GridLayout = QtWidgets.QGridLayout(self.SourceImage_GroupBox)
        self.SourceImage_GridLayout.setObjectName("SourceImage_GridLayout")
        self.SourceImage = QtWidgets.QLabel(self.SourceImage_GroupBox)
        self.SourceImage.setText("")
        self.SourceImage.setObjectName("SourceImage")
        self.SourceImage_GridLayout.addWidget(self.SourceImage, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.SourceImage_GroupBox)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Conversion_GroupBox = QtWidgets.QGroupBox(self.Central_Widget)
        self.Conversion_GroupBox.setMinimumSize(QtCore.QSize(101, 42))
        self.Conversion_GroupBox.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.Conversion_GroupBox.setObjectName("Conversion_GroupBox")
        
        self.Conversion_GridLayout = QtWidgets.QGridLayout(self.Conversion_GroupBox)
        self.Conversion_GridLayout.setObjectName("Conversion_GridLayout")
        
        self.RGBtoHSV_PushButton = QtWidgets.QPushButton(self.Conversion_GroupBox)
        self.RGBtoHSV_PushButton.setText("")
        self.RGBtoHSV_PushButton.setEnabled(False)
        self.RGBtoHSV_PushButton.clicked.connect(self.RGBtoHSV)
        self.RGBtoHSV_PushButton.setShortcut("Ctrl+H")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("rgb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RGBtoHSV_PushButton.setIcon(icon)
        self.RGBtoHSV_PushButton.setObjectName("RGBtoHSV_PushButton")
        self.Conversion_GridLayout.addWidget(self.RGBtoHSV_PushButton, 0, 1, 1, 1)
        
        self.RGBtoGrayscale_PushButton = QtWidgets.QPushButton(self.Conversion_GroupBox)
        self.RGBtoGrayscale_PushButton.setText("")
        self.RGBtoGrayscale_PushButton.setEnabled(False)
        self.RGBtoGrayscale_PushButton.clicked.connect(self.RGBtoGray)
        self.RGBtoGrayscale_PushButton.setShortcut("Ctrl+R")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("rgb-to-grayscale-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RGBtoGrayscale_PushButton.setIcon(icon1)
        self.RGBtoGrayscale_PushButton.setObjectName("RGBtoGrayscale_PushButton")
        self.Conversion_GridLayout.addWidget(self.RGBtoGrayscale_PushButton, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.Conversion_GroupBox)
        
        self.Segmentation_GroupBox = QtWidgets.QGroupBox(self.Central_Widget)
        self.Segmentation_GroupBox.setMinimumSize(QtCore.QSize(190, 42))
        self.Segmentation_GroupBox.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.Segmentation_GroupBox.setObjectName("Segmentation_GroupBox")
        self.Segmentation_GridLayout = QtWidgets.QGridLayout(self.Segmentation_GroupBox)
        self.Segmentation_GridLayout.setObjectName("Segmentation_GridLayout")
        
        self.MOT_PushButton = QtWidgets.QPushButton(self.Segmentation_GroupBox)
        self.MOT_PushButton.setObjectName("MOT_PushButton")
        self.Segmentation_GridLayout.addWidget(self.MOT_PushButton, 0, 0, 1, 1)
        self.MOT_PushButton.setEnabled(False)
        self.MOT_PushButton.setShortcut("Ctrl+M")
#        self.MOT_PushButton.clicked.connect(self.MOT)
        
        self.CVS_PushButton = QtWidgets.QPushButton(self.Segmentation_GroupBox)
        self.CVS_PushButton.setObjectName("CVS_PushButton")
        self.Segmentation_GridLayout.addWidget(self.CVS_PushButton, 0, 1, 1, 1)
        self.CVS_PushButton.setEnabled(False)
        self.CVS_PushButton.setShortcut("Ctrl+V")
        self.CVS_PushButton.clicked.connect(self.CVS)
        
        self.MS_PushButton = QtWidgets.QPushButton(self.Segmentation_GroupBox)
        self.MS_PushButton.setObjectName("MS_PushButton")
        self.Segmentation_GridLayout.addWidget(self.MS_PushButton, 0, 2, 1, 1)
        self.MS_PushButton.setEnabled(False)
        self.MS_PushButton.setShortcut("Ctrl+M+S")
        self.MS_PushButton.clicked.connect(self.MS)
        
        self.horizontalLayout_4.addWidget(self.Segmentation_GroupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.EdgeDetection_GroupBox = QtWidgets.QGroupBox(self.Central_Widget)
        self.EdgeDetection_GroupBox.setMinimumSize(QtCore.QSize(251, 41))
        self.EdgeDetection_GroupBox.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.EdgeDetection_GroupBox.setObjectName("EdgeDetection_GroupBox")
        self.EdgeDetection_GridLayout = QtWidgets.QGridLayout(self.EdgeDetection_GroupBox)

        self.Roberts_PushButton = QtWidgets.QPushButton(self.EdgeDetection_GroupBox)
        self.Roberts_PushButton.setObjectName("Roberts_PushButton")
        self.EdgeDetection_GridLayout.addWidget(self.Roberts_PushButton, 0, 0, 1, 1)
        self.Roberts_PushButton.clicked.connect(self.Roberts)
        self.Roberts_PushButton.setShortcut("Ctrl+F1")
        self.Roberts_PushButton.setEnabled(False)
        
        self.Sobel_PushButton = QtWidgets.QPushButton(self.EdgeDetection_GroupBox)
        self.Sobel_PushButton.setObjectName("Sobel_PushButton")
        self.EdgeDetection_GridLayout.addWidget(self.Sobel_PushButton, 0, 1, 1, 1)
        self.Sobel_PushButton.clicked.connect(self.Sobel)
        self.Sobel_PushButton.setShortcut("Ctrl+F2")
        self.Sobel_PushButton.setEnabled(False)
        
        self.Scharr_PushButton = QtWidgets.QPushButton(self.EdgeDetection_GroupBox)
        self.Scharr_PushButton.setObjectName("Scharr_PushButton")
        self.EdgeDetection_GridLayout.addWidget(self.Scharr_PushButton, 0, 2, 1, 1)
        self.Scharr_PushButton.clicked.connect(self.Scharr)
        self.Scharr_PushButton.setShortcut("Ctrl+F3")
        self.Scharr_PushButton.setEnabled(False)
        
        self.Prewitt_PushButton = QtWidgets.QPushButton(self.EdgeDetection_GroupBox)
        self.Prewitt_PushButton.setObjectName("Prewitt_PushButton")
        self.EdgeDetection_GridLayout.addWidget(self.Prewitt_PushButton, 0, 3, 1, 1)
        self.Prewitt_PushButton.clicked.connect(self.Prewitt)
        self.Prewitt_PushButton.setShortcut("Ctrl+F4")
        self.Prewitt_PushButton.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.EdgeDetection_GroupBox, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 2, 1)
        
        self.OutputImage_GroupBox = QtWidgets.QGroupBox(self.Central_Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputImage_GroupBox.sizePolicy().hasHeightForWidth())
        self.OutputImage_GroupBox.setSizePolicy(sizePolicy)
        self.OutputImage_GroupBox.setMinimumSize(QtCore.QSize(425, 250))
        self.OutputImage_GroupBox.setMaximumSize(QtCore.QSize(425, 250))
        self.OutputImage_GroupBox.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.OutputImage_GroupBox.setObjectName("OutputImage_GroupBox")
        self.OutputImage_GridLayout = QtWidgets.QGridLayout(self.OutputImage_GroupBox)
        self.OutputImage_GridLayout.setObjectName("OutputImage_GridLayout")
        self.OutputImage = QtWidgets.QLabel(self.OutputImage_GroupBox)
        self.OutputImage.setText("")
        self.OutputImage.setObjectName("OutputImage")
        self.OutputImage_GridLayout.addWidget(self.OutputImage, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.OutputImage_GroupBox, 0, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        self.Source_GroupBox = QtWidgets.QGroupBox(self.Central_Widget)
        self.Source_GroupBox.setMinimumSize(QtCore.QSize(161, 42))
        self.Source_GroupBox.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.Source_GroupBox.setObjectName("Source_GroupBox")
        self.Source_GridLayout = QtWidgets.QGridLayout(self.Source_GroupBox)
        self.Source_GridLayout.setObjectName("Source_GridLayout")
        
        self.OpenSource_PushButton = QtWidgets.QPushButton(self.Source_GroupBox)
        self.OpenSource_PushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("source-file-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenSource_PushButton.setIcon(icon2)
        self.OpenSource_PushButton.setObjectName("OpenSource_PushButton")
        self.OpenSource_PushButton.setShortcut("Ctrl+O")
        self.OpenSource_PushButton.clicked.connect(self.OpenSource)
        self.Source_GridLayout.addWidget(self.OpenSource_PushButton, 0, 0, 1, 1)
        
        self.ExportAsSource_PushButton = QtWidgets.QPushButton(self.Source_GroupBox)
        self.ExportAsSource_PushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExportAsSource_PushButton.setIcon(icon3)
        self.ExportAsSource_PushButton.setObjectName("ExportAsSource_PushButton")
        self.ExportAsSource_PushButton.setShortcut("Ctrl+E+S")
        self.Source_GridLayout.addWidget(self.ExportAsSource_PushButton, 0, 1, 1, 1)
        self.ExportAsSource_PushButton.clicked.connect(self.ExportAsSource)
        self.ExportAsSource_PushButton.setEnabled(False)
        
        self.ClearSource_PushButton = QtWidgets.QPushButton(self.Source_GroupBox)
        self.ClearSource_PushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Clear-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearSource_PushButton.setIcon(icon4)
        self.ClearSource_PushButton.setObjectName("ClearSource_PushButton")
        self.ClearSource_PushButton.setShortcut("Ctrl+L")
        self.Source_GridLayout.addWidget(self.ClearSource_PushButton, 0, 2, 1, 1)
        self.ClearSource_PushButton.clicked.connect(self.ClearSource)
        self.ClearSource_PushButton.setEnabled(False)
        self.horizontalLayout_6.addWidget(self.Source_GroupBox, 0, QtCore.Qt.AlignBottom)
        
        self.Output_GroupBox = QtWidgets.QGroupBox(self.Central_Widget)
        self.Output_GroupBox.setMinimumSize(QtCore.QSize(166, 42))
        self.Output_GroupBox.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.Output_GroupBox.setObjectName("Output_GroupBox")
        self.Output_GridLayout = QtWidgets.QGridLayout(self.Output_GroupBox)
        self.Output_GridLayout.setObjectName("Output_GridLayout")
        
        self.SaveOutput_PushButton = QtWidgets.QPushButton(self.Output_GroupBox)
        self.SaveOutput_PushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveOutput_PushButton.setIcon(icon5)
        self.SaveOutput_PushButton.setObjectName("SaveOutput_PushButton")
        self.SaveOutput_PushButton.setShortcut("Ctrl+S")
        self.SaveOutput_PushButton.clicked.connect(self.SaveOutput)
        self.Output_GridLayout.addWidget(self.SaveOutput_PushButton, 0, 0, 1, 1)
        self.SaveOutput_PushButton.setEnabled(False)
        
        self.SaveAsOutput_PushButton = QtWidgets.QPushButton(self.Output_GroupBox)
        self.SaveAsOutput_PushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Save-as-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveAsOutput_PushButton.setIcon(icon6)
        self.SaveAsOutput_PushButton.setObjectName("SaveAsOutput_PushButton")
        self.SaveAsOutput_PushButton.setShortcut("Ctrl+S+1")
        self.SaveAsOutput_PushButton.clicked.connect(self.SaveAsOutput)
        self.Output_GridLayout.addWidget(self.SaveAsOutput_PushButton, 0, 1, 1, 1)
        self.SaveAsOutput_PushButton.setEnabled(False)
        
        self.ExportAsOutput_PushButton = QtWidgets.QPushButton(self.Output_GroupBox)
        self.ExportAsOutput_PushButton.setText("")
        self.ExportAsOutput_PushButton.setIcon(icon3)
        self.ExportAsOutput_PushButton.setObjectName("ExportAsOutput_PushButton")
        self.ExportAsOutput_PushButton.setShortcut("Ctrl+E+O")
        self.Output_GridLayout.addWidget(self.ExportAsOutput_PushButton, 0, 2, 1, 1)
        self.ExportAsOutput_PushButton.clicked.connect(self.ExportAsOutput)
        self.ExportAsOutput_PushButton.setEnabled(False)
        
        self.ClearOutput_PushButton = QtWidgets.QPushButton(self.Output_GroupBox)
        self.ClearOutput_PushButton.setText("")
        self.ClearOutput_PushButton.setIcon(icon4)
        self.ClearOutput_PushButton.setObjectName("ClearOutput_PushButton")
        self.ClearOutput_PushButton.setShortcut("Ctrl+Shift+L")
        self.Output_GridLayout.addWidget(self.ClearOutput_PushButton, 0, 3, 1, 1)
        self.ClearOutput_PushButton.clicked.connect(self.ClearOutput)
        self.ClearOutput_PushButton.setEnabled(False)
  
        self.UndoOutput_PushButton = QtWidgets.QPushButton(self.Output_GroupBox)
        self.UndoOutput_PushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Undo-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UndoOutput_PushButton.setIcon(icon7)
        self.UndoOutput_PushButton.setObjectName("UndoOutput_PushButton")
        self.UndoOutput_PushButton.setShortcut("Ctrl+Shift+Z")
        self.Output_GridLayout.addWidget(self.UndoOutput_PushButton, 0, 4, 1, 1)
        self.UndoOutput_PushButton.clicked.connect(self.undoAction)
        self.UndoOutput_PushButton.setEnabled(False)
        
        self.RedoOutput_PushButton = QtWidgets.QPushButton(self.Output_GroupBox)
        self.RedoOutput_PushButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Redo-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RedoOutput_PushButton.setIcon(icon8)
        self.RedoOutput_PushButton.setObjectName("RedoOutput_PushButton")
        self.RedoOutput_PushButton.setShortcut("Ctrl+Y")
        self.Output_GridLayout.addWidget(self.RedoOutput_PushButton, 0, 5, 1, 1)
        self.RedoOutput_PushButton.clicked.connect(self.redoAction)
        self.horizontalLayout_6.addWidget(self.Output_GroupBox, 0, QtCore.Qt.AlignBottom)
        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)
        self.RedoOutput_PushButton.setEnabled(False)
        
        MainWindow.setCentralWidget(self.Central_Widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 18))
        self.menubar.setObjectName("menubar")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut('Shift+F4')
        self.actionExit.triggered.connect(qApp.quit)
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def OpenSource(self):
        self.RGBtoGrayscale_PushButton.setEnabled(True)
        self.RGBtoHSV_PushButton.setEnabled(True)
        self.MOT_PushButton.setEnabled(True)
        self.MS_PushButton.setEnabled(True)
        self.CVS_PushButton.setEnabled(True)
        self.Prewitt_PushButton.setEnabled(True)
        self.Roberts_PushButton.setEnabled(True)
        self.Scharr_PushButton.setEnabled(True)
        self.Sobel_PushButton.setEnabled(True)
        self.ExportAsSource_PushButton.setEnabled(True)
        self.imageName,imgType = QFileDialog.getOpenFileName(self.Central_Widget, "openImage", "", "*.jpg;;*.png;;All Files(*)")  
        jpg = QtGui.QPixmap(self.imageName).scaled(self.SourceImage.width(),self.SourceImage.height())  
        if self.imageName != "":
            self.SourceImage.setPixmap(jpg)
        self.SaveOutput_PushButton.setEnabled(True)
        self.SaveAsOutput_PushButton.setEnabled(True)
        self.ExportAsOutput_PushButton.setEnabled(True)
        self.ClearOutput_PushButton.setEnabled(True)
        self.ClearSource_PushButton.setEnabled(True)
        self.UndoOutput_PushButton.setEnabled(True)
        self.RedoOutput_PushButton.setEnabled(True)
        
    def SaveOutput(self):
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.OutputImage.winId())
        fd,type= QFileDialog.getSaveFileName(self.Central_Widget, "saveOutput","", "Images (*.jpg;;*.png;;All Files(*))")
        pix.save(fd)
    
    def SaveAsOutput(self):
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.OutputImage.winId())
        fd,type= QFileDialog.getSaveFileName(self.Central_Widget, "saveAsOutput", "", "*.jpg;;*.png;;All Files(*)")
        pix.save(fd)
    
    def ClearSource(self):
        self.SourceImage.clear()
        
    def ClearOutput(self):
        self.OutputImage.clear()
        
    def ExportAsSource(self):
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.SourceImage.winId())        
        fd,type= QFileDialog.getSaveFileName(self.Central_Widget, "ExportAsSource", "", "*.png")
        pix.save(fd)
        
    def ExportAsOutput(self):
        screen = QApplication.primaryScreen()
        pix = screen.grabWindow(self.OutputImage.winId())         
        fd,type= QFileDialog.getSaveFileName(self.Central_Widget, "ExportAsOutput", "", "*.png")
        pix.save(fd)
        
    def undoAction(self):
        self.undoAction = QAction()
        self.undoStack = QUndoStack()
        self.undoAction = self.undoStack.createUndoAction(self.Central_Widget, "&Undo")
        self.undoAction.setShortcut(QKeySequence.Undo)
        
    def redoAction(self):
        self.redoAction = QAction()
        self.undoStack = QUndoStack()
        self.redoAction = self.undoStack.createRedoAction(self.Central_Widget, "&Redo")
        self.redoAction.setShortcut(QKeySequence.Redo)
                
    def RGBtoGray(self):
        original = data.coffee()
        grayscale = rgb2gray(original)
        fig, axes = plt.subplots(1, 2, figsize=(8, 4))
        ax = axes.ravel()
        ax[0].imshow(original)
        ax[0].set_title("Original")
        ax[1].imshow(grayscale, cmap=plt.cm.gray)
        ax[1].set_title("Grayscale")
        fig.tight_layout()
        plt.show()
        
    def RGBtoHSV(self):
        rgb_img = data.coffee()
        hsv_img = rgb2hsv(rgb_img)
        hue_img = hsv_img[:, :, 0]
        value_img = hsv_img[:, :, 2]
        fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 2))
        ax0.imshow(rgb_img)
        ax0.set_title("RGB image")
        ax0.axis('off')
        ax1.imshow(hue_img, cmap='hsv')
        ax1.set_title("Hue channel")
        ax1.axis('off')
        ax2.imshow(value_img)
        ax2.set_title("Value channel")
        ax2.axis('off')
        fig.tight_layout()
        hue_threshold = 0.04
        binary_img = hue_img > hue_threshold
        fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 3))
        ax0.hist(hue_img.ravel(), 512)
        ax0.set_title("Histogram of the Hue channel with threshold")
        ax0.axvline(x=hue_threshold, color='r', linestyle='dashed', linewidth=2)
        ax0.set_xbound(0, 0.12)
        ax1.imshow(binary_img)
        ax1.set_title("Hue-thresholded image")
        ax1.axis('off')
        fig.tight_layout()
        fig, ax0 = plt.subplots(figsize=(4, 3))
        value_threshold = 0.10
        binary_img = (hue_img > hue_threshold) | (value_img < value_threshold)
        ax0.imshow(binary_img)
        ax0.set_title("Hue and value thresholded image")
        ax0.axis('off')
        fig.tight_layout()
        plt.show()
                
#    def MOT(self):
#        matplotlib.rcParams['font.size'] = 9
#        image = data.camera()
#        thresholds = threshold_multiotsu(image)
#        regions = np.digitize(image, bins=thresholds)
#        fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(10, 3.5))
#        ax[0].imshow(image, cmap='gray')
#        ax[0].set_title('Original')
#        ax[0].axis('off')
#        ax[1].hist(image.ravel(), bins=255)
#        ax[1].set_title('Histogram')
#        for thresh in thresholds:
#            ax[1].axvline(thresh, color='r')
#        ax[2].imshow(regions, cmap='jet')
#        ax[2].set_title('Multi-Otsu result')
#        ax[2].axis('off')
#        plt.subplots_adjust()
#        plt.show()
    
    def CVS(self):
        image = img_as_float(data.camera())
        cv = chan_vese(image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3, max_iter=200,
                       dt=0.5, init_level_set="checkerboard", extended_output=True)
        fig, axes = plt.subplots(2, 2, figsize=(8, 8))
        ax = axes.flatten()
        ax[0].imshow(image, cmap="gray")
        ax[0].set_axis_off()
        ax[0].set_title("Original Image", fontsize=12)
        ax[1].imshow(cv[0], cmap="gray")
        ax[1].set_axis_off()
        title = "Chan-Vese segmentation - {} iterations".format(len(cv[2]))
        ax[1].set_title(title, fontsize=12)
        ax[2].imshow(cv[1], cmap="gray")
        ax[2].set_axis_off()
        ax[2].set_title("Final Level Set", fontsize=12)
        ax[3].plot(cv[2])
        ax[3].set_title("Evolution of energy over iterations", fontsize=12)
        fig.tight_layout()
        plt.show()
    
    def MS(self):
        def store_evolution_in(lst):
            """Returns a callback function to store the evolution of the level sets in
            the given list.
            """
            def _store(x):
                lst.append(np.copy(x))
            return _store
        image = img_as_float(data.camera())
        init_ls = checkerboard_level_set(image.shape, 6)
        evolution = []
        callback = store_evolution_in(evolution)
        ls = morphological_chan_vese(image, 35, init_level_set=init_ls, smoothing=3,
                                     iter_callback=callback)
        fig, axes = plt.subplots(2, 2, figsize=(8, 8))
        ax = axes.flatten()
        ax[0].imshow(image, cmap="gray")
        ax[0].set_axis_off()
        ax[0].contour(ls, [0.5], colors='r')
        ax[0].set_title("Morphological ACWE segmentation", fontsize=12)
        ax[1].imshow(ls, cmap="gray")
        ax[1].set_axis_off()
        contour = ax[1].contour(evolution[2], [0.5], colors='g')
        contour.collections[0].set_label("Iteration 2")
        contour = ax[1].contour(evolution[7], [0.5], colors='y')
        contour.collections[0].set_label("Iteration 7")
        contour = ax[1].contour(evolution[-1], [0.5], colors='r')
        contour.collections[0].set_label("Iteration 35")
        ax[1].legend(loc="upper right")
        title = "Morphological ACWE evolution"
        ax[1].set_title(title, fontsize=12)
        image = img_as_float(data.coins())
        gimage = inverse_gaussian_gradient(image)
        init_ls = np.zeros(image.shape, dtype=np.int8)
        init_ls[10:-10, 10:-10] = 1
        evolution = []
        callback = store_evolution_in(evolution)
        ls = morphological_geodesic_active_contour(gimage, 230, init_ls,
                                                   smoothing=1, balloon=-1,
                                                   threshold=0.69,
                                                   iter_callback=callback)
        ax[2].imshow(image, cmap="gray")
        ax[2].set_axis_off()
        ax[2].contour(ls, [0.5], colors='r')
        ax[2].set_title("Morphological GAC segmentation", fontsize=12)
        ax[3].imshow(ls, cmap="gray")
        ax[3].set_axis_off()
        contour = ax[3].contour(evolution[0], [0.5], colors='g')
        contour.collections[0].set_label("Iteration 0")
        contour = ax[3].contour(evolution[100], [0.5], colors='y')
        contour.collections[0].set_label("Iteration 100")
        contour = ax[3].contour(evolution[-1], [0.5], colors='r')
        contour.collections[0].set_label("Iteration 230")
        ax[3].legend(loc="upper right")
        title = "Morphological GAC evolution"
        ax[3].set_title(title, fontsize=12)
        fig.tight_layout()
        plt.show()
        
    def Roberts(self):
        camera = data.camera()
        edges = filters.roberts(camera)
        print(edges)
        
    def Sobel(self):
        camera = data.camera()
        edges = filters.sobel(camera)
        print(edges)
        
    def Scharr(self):
        camera = data.camera()
        edges = filters.scharr(camera)
        print(edges)
        
    def Prewitt(self):
        camera = data.camera()
        edges = filters.prewitt(camera)
        print(edges)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SourceImage_GroupBox.setTitle(_translate("MainWindow", "Source"))
        self.Conversion_GroupBox.setTitle(_translate("MainWindow", "Conversion"))
        self.RGBtoHSV_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>RGB to HSV</p></body></html>"))
        self.RGBtoGrayscale_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>RGB to Grayscale</p></body></html>"))
        self.Segmentation_GroupBox.setTitle(_translate("MainWindow", "Segmentation"))
        self.MOT_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Multi Otsu Thresholding</p></body></html>"))
        self.MOT_PushButton.setText(_translate("MainWindow", "MOT"))
        self.CVS_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Chan Vese Segmentation</p></body></html>"))
        self.CVS_PushButton.setText(_translate("MainWindow", "CVS"))
        self.MS_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Morphological Snakes</p></body></html>"))
        self.MS_PushButton.setText(_translate("MainWindow", "MS"))
        self.EdgeDetection_GroupBox.setTitle(_translate("MainWindow", "Edge Detection"))
        self.Roberts_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Roberts</p></body></html>"))
        self.Roberts_PushButton.setText(_translate("MainWindow", "R"))
        self.Sobel_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Sobel</p></body></html>"))
        self.Sobel_PushButton.setText(_translate("MainWindow", "So"))
        self.Scharr_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Scharr</p></body></html>"))
        self.Scharr_PushButton.setText(_translate("MainWindow", "Sc"))
        self.Prewitt_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Prewitt</p></body></html>"))
        self.Prewitt_PushButton.setText(_translate("MainWindow", "P"))
        self.OutputImage_GroupBox.setTitle(_translate("MainWindow", "Output"))
        self.Source_GroupBox.setTitle(_translate("MainWindow", "Source"))
        self.OpenSource_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Open Source</p></body></html>"))
        self.ExportAsSource_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Export As Source</p></body></html>"))
        self.ClearSource_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clear Source</p></body></html>"))
        self.Output_GroupBox.setTitle(_translate("MainWindow", "Output"))
        self.SaveOutput_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save Output</p></body></html>"))
        self.SaveAsOutput_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Save As Output</p></body></html>"))
        self.ExportAsOutput_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Export As Output</p></body></html>"))
        self.ClearOutput_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clear Output</p></body></html>"))
        self.UndoOutput_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Undo Output</p></body></html>"))
        self.RedoOutput_PushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Redo Output</p></body></html>"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

