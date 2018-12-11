import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project_one.ui',self)
        self.text = ''
        self.clr = -1
        self.keybuttons = [self.btn_f,self.btn_g]
    def keyPressEvent(self, event):
        if self.clr != -1:
            self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(230, 230, 250) } """)
        if event.key() == Qt.Key_F:
            self.text += 'f'
            self.answershit.setText(self.text)
            self.btn_f.setStyleSheet("""QPushButton:!hover { background-color: rgb(0, 255, 0); }""")
            self.clr = 0
        elif event.key() == Qt.Key_G:
            self.text += 'g'
            self.answershit.setText(self.text)
            self.btn_g.setStyleSheet("""QPushButton:!hover { background-color: rgb(0, 255, 0); }""")
            self.clr = 1
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
