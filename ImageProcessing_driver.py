##Object Oriented Programming 2 Final Assignment
#
# Author: Öznur Çalışkan

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox, QDesktopWidget, QApplication
from PyQt5.QtGui import QIcon
from OOP2_Final import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Image Processing Window')
        self.setWindowIcon(QIcon('image-process-icon.png')) 
        self.center()
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())    
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
        
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())