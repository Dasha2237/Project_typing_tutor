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
        self.lng = 'RU'
        self.capslock = 0
        self.keybuttons = [self.btn_io, self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5,
                           self.btn_6, self.btn_7, self.btn_8, self.btn_9, self.btn_0, self.btn_minus,
                           self.btn_plus, self.btn_backspace, self.btn_q, self.btn_w, self.btn_e, self.btn_r,
                           self.btn_t, self.btn_y, self.btn_u, self.btn_i, self.btn_o, self.btn_p,
                           self.btn_xa, self.btn_tv_zn, self.btn_capslock, self.btn_a, self.btn_s, self.btn_d,
                           self.btn_f, self.btn_g, self.btn_h, self.btn_j, self.btn_k, self.btn_l,
                           self.btn_gh, self.btn_ei, self.btn_slash, self.btn_enter, self.btn_shift, self.btn_z,
                           self.btn_x, self.btn_c, self.btn_v, self.btn_b, self.btn_n, self.btn_m,
                           self.btn_be, self.btn_iu, self.btn_dot, self.btn_ctrl, self.btn_alt, self.btn_space]
        self.rus = ['ё','1 !','2 "','3 №','4 ;','5 %','6 :','7 ?','8 *','9 (','0 )','- _','= +','<- Backspace','й','ц','у','к','е','н','г','ш',
                    'щ','з','х','ъ','Caps Lock','ф','ы','в','а','п','р','о','л','д','ж','э','\ /','Enter','Shift','я','ч','с',
                    'м','и','т','ь','б','ю','. ,','Ctrl','Alt','                                     ']
        self.eng = ['` ~','1 !','2 @','3 #','4 $','5 %','6 ^','7 &','8 *','9 (','0 )','- _','= +','<- Backspace','q','w','e','r','t','y','u','i',
                    'o','p','[ {',']}','Caps Lock','a','s','d','f','g','h','j','k','l','; :',' '""'','\ |','Enter','Shift','z','x','c',
                    'v','b','n','m',', <','. >','/ ?','Ctrl','Alt','                                     ']
    def keyPressEvent(self, event):
        if self.clr != -1:
            if self.clr in [10,14,26,27,40,51,11,12,13,23,24,25,36,37,38,39,50]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(255, 255, 127) } """)
            elif self.clr in [1,2,15,28,41,10,22,35,49]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(0, 170, 255) } """)
            elif self.clr in [3,4,16,29,42,8,9,21,34,48]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(170, 255, 127) } """)
            elif self.clr in [5,6,17,18,30,31,43,44,45]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(253, 116, 141) } """)
            elif self.clr in [7,19,20,32,33,46,47]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(170, 170, 255) } """)
            elif self.clr in [52]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(184, 184, 184) } """)
            elif self.clr in [53]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(85, 170, 127) } """)
        if len(self.text) % 151 == 0:
            self.text = self.text + '\n'
            self.answershit.setText(self.text)
        if event.key() == Qt.Key_1:
            self.text += '1'
            self.answershit.setText(self.text)
            self.btn_1.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 1
        elif event.key() == Qt.Key_2:
            self.text += '2'
            self.answershit.setText(self.text)
            self.btn_2.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 2
        elif event.key() == Qt.Key_3:
            self.text += '3'
            self.answershit.setText(self.text)
            self.btn_3.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 3
        elif event.key() == Qt.Key_4:
            self.text += '4'
            self.answershit.setText(self.text)
            self.btn_4.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 4
        elif event.key() == Qt.Key_5:
            self.text += '5'
            self.answershit.setText(self.text)
            self.btn_5.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 5
        elif event.key() == Qt.Key_6:
            self.text += '6'
            self.answershit.setText(self.text)
            self.btn_6.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 6
        elif event.key() == Qt.Key_7:
            self.text += '7'
            self.answershit.setText(self.text)
            self.btn_7.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 7
        elif event.key() == Qt.Key_8:
            self.text += '8'
            self.answershit.setText(self.text)
            self.btn_8.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 8
        elif event.key() == Qt.Key_9:
            self.text += '9'
            self.answershit.setText(self.text)
            self.btn_9.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 9
        elif event.key() == Qt.Key_0:
            self.text += '0'
            self.answershit.setText(self.text)
            self.btn_0.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 10
        elif event.key() == Qt.Key_Q:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'й'
                else:
                    self.text += 'Й'
            else:
                if self.capslock == 0:
                    self.text += 'q'
                else:
                    self.text += 'Q'
            self.answershit.setText(self.text)
            self.btn_q.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 14
        elif event.key() == Qt.Key_W:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ц'
                else:
                    self.text += 'Ц'
            else:
                if self.capslock == 0:
                    self.text += 'w'
                else:
                    self.text += 'W'
            self.answershit.setText(self.text)
            self.btn_w.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 15
        elif event.key() == Qt.Key_E:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'у'
                else:
                    self.text += 'У'
            else:
                if self.capslock == 0:
                    self.text += 'e'
                else:
                    self.text += 'E'
            self.answershit.setText(self.text)
            self.btn_e.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 16
        elif event.key() == Qt.Key_R:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'к'
                else:
                    self.text += 'К'
            else:
                if self.capslock == 0:
                    self.text += 'r'
                else:
                    self.text += 'R'
            self.answershit.setText(self.text)
            self.btn_r.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 17
        elif event.key() == Qt.Key_T:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'е'
                else:
                    self.text += 'Е'
            else:
                if self.capslock == 0:
                    self.text += 't'
                else:
                    self.text += 'T'
            self.answershit.setText(self.text)
            self.btn_t.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 18
        elif event.key() == Qt.Key_Y:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'н'
                else:
                    self.text += 'Н'
            else:
                if self.capslock == 0:
                    self.text += 'y'
                else:
                    self.text += 'Y'
            self.answershit.setText(self.text)
            self.btn_y.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 19
        elif event.key() == Qt.Key_U:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'г'
                else:
                    self.text += 'Г'
            else:
                if self.capslock == 0:
                    self.text += 'u'
                else:
                    self.text += 'U'
            self.answershit.setText(self.text)
            self.btn_u.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 20
        elif event.key() == Qt.Key_I:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ш'
                else:
                    self.text += 'Ш'
            else:
                if self.capslock == 0:
                    self.text += 'i'
                else:
                    self.text += 'I'
            self.answershit.setText(self.text)
            self.btn_i.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 21
        elif event.key() == Qt.Key_O:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'щ'
                else:
                    self.text += 'Щ'
            else:
                if self.capslock == 0:
                    self.text += 'o'
                else:
                    self.text += 'O'
            self.answershit.setText(self.text)
            self.btn_o.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 22
        elif event.key() == Qt.Key_P:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'з'
                else:
                    self.text += 'З'
            else:
                if self.capslock == 0:
                    self.text += 'p'
                else:
                    self.text += 'P'
            self.answershit.setText(self.text)
            self.btn_p.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 23
        elif event.key() == Qt.Key_A:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ф'
                else:
                    self.text += 'Ф'
            else:
                if self.capslock == 0:
                    self.text += 'a'
                else:
                    self.text += 'A'
            self.answershit.setText(self.text)
            self.btn_a.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 27
        elif event.key() == Qt.Key_S:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ы'
                else:
                    self.text += 'Ы'
            else:
                if self.capslock == 0:
                    self.text += 's'
                else:
                    self.text += 'S'
            self.answershit.setText(self.text)
            self.btn_s.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 28
        elif event.key() == Qt.Key_D:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'в'
                else:
                    self.text += 'в'
            else:
                if self.capslock == 0:
                    self.text += 'd'
                else:
                    self.text += 'D'
            self.answershit.setText(self.text)
            self.btn_d.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 29
        elif event.key() == Qt.Key_F:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'а'
                else:
                    self.text += 'А'
            else:
                if self.capslock == 0:
                    self.text += 'f'
                else:
                    self.text += 'F'
            self.answershit.setText(self.text)
            self.btn_f.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 30
        elif event.key() == Qt.Key_G:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'п'
                else:
                    self.text += 'П'
            else:
                if self.capslock == 0:
                    self.text += 'g'
                else:
                    self.text += 'G'
            self.answershit.setText(self.text)
            self.btn_g.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 31
        elif event.key() == Qt.Key_H:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'р'
                else:
                    self.text += 'Р'
            else:
                if self.capslock == 0:
                    self.text += 'h'
                else:
                    self.text += 'H'
            self.answershit.setText(self.text)
            self.btn_h.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 32
        elif event.key() == Qt.Key_J:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'о'
                else:
                    self.text += 'О'
            else:
                if self.capslock == 0:
                    self.text += 'j'
                else:
                    self.text += 'J'
            self.answershit.setText(self.text)
            self.btn_j.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 33
        elif event.key() == Qt.Key_K:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'л'
                else:
                    self.text += 'Л'
            else:
                if self.capslock == 0:
                    self.text += 'k'
                else:
                    self.text += 'K'
            self.answershit.setText(self.text)
            self.btn_k.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 34
        elif event.key() == Qt.Key_L:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'д'
                else:
                    self.text += 'Д'
            else:
                if self.capslock == 0:
                    self.text += 'l'
                else:
                    self.text += 'L'
            self.answershit.setText(self.text)
            self.btn_l.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 35
        elif event.key() == Qt.Key_Z:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'я'
                else:
                    self.text += 'Я'
            else:
                if self.capslock == 0:
                    self.text += 'z'
                else:
                    self.text += 'Z'
            self.answershit.setText(self.text)
            self.btn_z.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 41
        elif event.key() == Qt.Key_X:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ч'
                else:
                    self.text += 'Ч'
            else:
                if self.capslock == 0:
                    self.text += 'x'
                else:
                    self.text += 'X'
            self.answershit.setText(self.text)
            self.btn_x.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 42
        elif event.key() == Qt.Key_C:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'с'
                else:
                    self.text += 'С'
            else:
                if self.capslock == 0:
                    self.text += 'c'
                else:
                    self.text += 'C'
            self.answershit.setText(self.text)
            self.btn_c.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 43
        elif event.key() == Qt.Key_V:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'м'
                else:
                    self.text += 'М'
            else:
                if self.capslock == 0:
                    self.text += 'v'
                else:
                    self.text += 'V'
            self.answershit.setText(self.text)
            self.btn_v.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 44
        elif event.key() == Qt.Key_B:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'и'
                else:
                    self.text += 'И'
            else:
                if self.capslock == 0:
                    self.text += 'b'
                else:
                    self.text += 'B'
            self.answershit.setText(self.text)
            self.btn_b.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 45
        elif event.key() == Qt.Key_N:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'т'
                else:
                    self.text += 'Т'
            else:
                if self.capslock == 0:
                    self.text += 'n'
                else:
                    self.text += 'N'
            self.answershit.setText(self.text)
            self.btn_n.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 46
        elif event.key() == Qt.Key_M:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ь'
                else:
                    self.text += 'Ь'
            else:
                if self.capslock == 0:
                    self.text += 'm'
                else:
                    self.text += 'M'
            self.answershit.setText(self.text)
            self.btn_m.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 47

        
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
Qt.Key_Underscore
