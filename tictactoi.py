from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton,QGridLayout
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("tictactoi.ui",self)

        self.counter = 0
        self.setWindowTitle("TIc Tac Toi")
        self.setWindowIcon(QtGui.QIcon('image/logo.ico'))
        self.button1 = self.findChild(QPushButton,"pushButton_2")
        self.button2 = self.findChild(QPushButton,"pushButton_3")
        self.button3 = self.findChild(QPushButton,"pushButton_4")
        self.button4 = self.findChild(QPushButton,"pushButton_5")
        self.button5 = self.findChild(QPushButton,"pushButton_6")
        self.button6 = self.findChild(QPushButton,"pushButton_7")
        self.button7 = self.findChild(QPushButton,"pushButton_8")
        self.button8 = self.findChild(QPushButton,"pushButton_9")
        self.button9 = self.findChild(QPushButton,"pushButton_10")
        # start over button
        self.button10 = self.findChild(QPushButton,"pushButton")
        # label
        self.label = self.findChild(QLabel,"label")
        self.label.setText("X's first Turn")
        # button click event
        self.button1.clicked.connect(lambda:self.clicker(self.button1))
        self.button2.clicked.connect(lambda:self.clicker(self.button2))
        self.button3.clicked.connect(lambda:self.clicker(self.button3))
        self.button4.clicked.connect(lambda:self.clicker(self.button4))
        self.button5.clicked.connect(lambda:self.clicker(self.button5))
        self.button6.clicked.connect(lambda:self.clicker(self.button6))
        self.button7.clicked.connect(lambda:self.clicker(self.button7))
        self.button8.clicked.connect(lambda:self.clicker(self.button8))
        self.button9.clicked.connect(lambda:self.clicker(self.button9))
        # start over button
        self.button10.clicked.connect(lambda:self.reset())

        # show the app
        self.show()




    # check win on ever click
    def checkWin(self):
        # horizontal check
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.win(self.button1,self.button2,self.button3)
        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.win(self.button4,self.button5,self.button6)
        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.win(self.button7,self.button8,self.button9)
        # vertical check
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.win(self.button1,self.button4,self.button7)
        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.win(self.button2,self.button5,self.button8)
        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            self.win(self.button3,self.button6,self.button9)
        # diagonal
        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.win(self.button1,self.button5,self.button9)
        if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            self.win(self.button3,self.button5,self.button7)

        if self.counter == 9:
            self.label.setText(f"Game Tie!")
            

    # win condition here
    def win(self,a,b,c):
        a.setStyleSheet('QPushButton {color:red;}')
        b.setStyleSheet('QPushButton {color:red;}')
        c.setStyleSheet('QPushButton {color:red;}')
        self.counter = 0
        self.label.setText(f"{a.text()}'s Wins!")
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]

        for b in button_list:
            b.setEnabled(False)


    def clicker(self,b):
        if self.counter % 2 == 0:
            mark = "X"
            text = "O"
        else:
            text = "X"
            mark = "O"
        b.setText(mark)
        b.setEnabled(False) 
        # counter increment
        self.counter += 1
        self.label.setText(f"{text}'s turn")
        self.checkWin()
    
    # start over
    def reset(self):
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]
        self.counter = 0
        self.label.setText(f"X's Turn")

        for b in button_list:
            b.setText("")
            b.setStyleSheet('QPushButton {color:#797979;}')
            b.setEnabled(True)

        


app = QApplication(sys.argv)
UIWindow= UI()
app.exec_()

