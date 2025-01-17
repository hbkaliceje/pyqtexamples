import sys, time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, \
    QLabel, QTextBrowser, QComboBox, QListWidget, QProgressBar, QMessageBox, QDialogButtonBox
from PyQt5 import uic
from datetime import datetime

TIME_LIMIT = 100

class My_UI(QMainWindow):

    def __init__(self):

        super(My_UI,self).__init__() # call constrcutor of parent class
        
        uic.loadUi("mainwindow.ui",self)

        self.heading = self.findChild(QLabel,"lbl_heading")
        self.buttonAdd = self.findChild(QPushButton,"add_btn")
        self.buttonDelete = self.findChild(QPushButton,"del_btn")
        self.buttonDelete.setEnabled(False) # disable delete button

        self.comboBox1 = self.findChild(QComboBox,"cmb_one")
        self.listWidget  = self.findChild(QListWidget,"lst_widget")
        self.txtBrowser = self.findChild(QTextBrowser,"txt_browser_one")
        self.progBar = self.findChild(QProgressBar, "progbar_one")

        self.progBar.setMaximum(100)
        self.progBar.setValue(50)

        self.labelProgressComplete = self.findChild(QLabel, "lbl_progress_complete")
        self.labelProgressComplete.setHidden(True)                                     # hide label until progress bar is full

        """ set event handlers """
        self.buttonAdd.clicked.connect(self.add_btn_clicked)
        self.buttonDelete.clicked.connect(self.del_btn_clicked)
        self.listWidget.clicked.connect(self.listwidget_clicked)
        self.lwModel = self.listWidget.model()                             # need to pick up events on the list
        self.lwModel.rowsInserted.connect(self.checkListLength)            # Any time an element is added run function
        self.lwModel.rowsRemoved.connect(self.checkListLength)             # Any time an element is removed run function

        self.show()
    
    #end def


    def listwidget_clicked(self):
    
        print(self.listWidget.currentRow())
        if self.listWidget.count() > 0:
            self.buttonDelete.setEnabled(True) # enable delete button
        else:
            self.buttonDelete.setEnabled(False) # disable delete button
        #end if

    #end def


    def checkListLength(self):

        if self.listWidget.count() > 0:
            self.buttonDelete.setEnabled(True) # disable delete button
        else:
            self.buttonDelete.setEnabled(False)
        # end if

    #end def


    def add_btn_clicked(self):

        """ add item from list and combo box"""

        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y %H:%M:%S")

        # add item to list and combo box
        self.listWidget.addItem(d1)
        self.comboBox1.addItem(d1)

        if self.progBar.value() < self.progBar.maximum():

            self.progBar.setValue(self.progBar.value()+5)

        else:

            self.buttonAdd.setEnabled(False)
            self.labelProgressComplete.setHidden(False)                                 # show full label
            self.progBar.setEnabled(False)                                              # disable prgress bar
            self.showCompleteMessage("Progress Complete")

        #endif

    #end def


    def showCompleteMessage(self, message_text):

        msg = QMessageBox()
        msg.setStyleSheet("background-color: rgb(200, 200, 0); color rgb(255, 200, 0)")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(message_text)
        msg.setText("Have a Nice Day!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    #enddef


    def del_btn_clicked(self):

        """ remove item from list and combo box"""
        if self.listWidget.count() == 0:
            print("Nope")
        #endif

        if self.listWidget.count() > 0:
            self.listWidget.takeItem(self.listWidget.currentRow())
        else:
            print("Nope - not in list")
        #endif

    #enddef

#endclass

# main starts here - init App
app = QApplication(sys.argv)
window = My_UI()
app.exec_()
sys.exit(app.exec_())