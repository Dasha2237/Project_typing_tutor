import sys
from random import choice, randrange
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from project_one import Ui_MainWindow


class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = ''
        self.data = ''
        self.clr = -1
        self.lng = 'RU'
        self.b = -1
        self.capslock = 0
        self.button_group.buttonClicked.connect(self.Language)
        self.texts = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']
        self.chb = [self.text1, self.symbol]
        self.go.clicked.connect(self.Exersize)
        self.restart.clicked.connect(self.Restart)
        self.t = 'qwertyuiopasdfghjkl;\][zxcvbnm,./1234567890-=+_)(*&^%$}{|:?><йцукенгшщзхъфывапролджэячсмитьбю'
        self.keybuttons = [self.btn_io, self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5,
                           self.btn_6, self.btn_7, self.btn_8, self.btn_9, self.btn_0, self.btn_minus,
                           self.btn_plus, self.btn_backspace, self.btn_q, self.btn_w, self.btn_e, self.btn_r,
                           self.btn_t, self.btn_y, self.btn_u, self.btn_i, self.btn_o, self.btn_p,
                           self.btn_xa, self.btn_tv_zn, self.btn_capslock, self.btn_a, self.btn_s, self.btn_d,
                           self.btn_f, self.btn_g, self.btn_h, self.btn_j, self.btn_k, self.btn_l,
                           self.btn_gh, self.btn_ei,'c', self.btn_enter, self.btn_shift, self.btn_z,
                           self.btn_x, self.btn_c, self.btn_v, self.btn_b, self.btn_n, self.btn_m,
                           self.btn_be, self.btn_iu, self.btn_dot, self.btn_ctrl, self.btn_alt, self.btn_space]
        self.rus = ['ё','1 !','2 "','3 №','4 ;','5 %','6 :','7 ?','8 *','9 (','0 )','- _','= +','<- Backspace','й','ц','у','к','е','н','г','ш',
                    'щ','з','х','ъ','Caps Lock','ф','ы','в','а','п','р','о','л','д','ж','э','g','Enter','Shift','я','ч','с',
                    'м','и','т','ь','б','ю','. ,','Ctrl','Alt','                                     ']
        self.eng = ['` ~','1 !','2 @','3 #','4 $','5 %','6 ^','7 &','8 *','9 (','0 )','- _','= +','<- Backspace','q','w','e','r','t','y','u','i',
                    'o','p','[ {',']}','Caps Lock','a','s','d','f','g','h','j','k','l','; :','""','g','Enter','Shift','z','x','c',
                    'v','b','n','m',', <','. >','/ ?','Ctrl','Alt','                                     ']
        self.check.clicked.connect(self.Result)
        '''for i in range(len(self.keybuttons)):
            self.keybuttons[i].setText(str(self.eng[i]))'''
    def Exersize(self):
        if self.text1.isChecked() and self.symbol.isChecked() :
            self.testplace.setHtml('Выберите что-то одно!')
        elif self.symbol.isChecked():
            self.data = ''
            for i in range(randrange(50, 150, 1)):
                self.data += self.t[randrange(0, 93, 1)]
            self.testplace.setHtml(self.data)
        elif self.text1.isChecked():
            a = choice(self.texts)
            self.data = open(a, mode="r").read()
            self.testplace.setHtml(self.data)
        else:
            self.testplace.setHtml('Нужно выбрать задание!')
    def Result(self):
        ideal = ''
        reality = ''
        ideal = ''.join(self.data.split(' ')).strip()
        err = 0
        k = 0
        reality = ''.join(self.text.split(' ')).strip()
        for i in range(len(''.join(self.data.split(' ')))):
            if i != len(reality):
                if ideal[i] != reality[i]:
                    k += 1
            else:
                break
        if k == 0:
            self.result.setText('Результат: Все правильно, молодец!')
        else:
            self.result.setText('Результат: Есть ошибки: {} '.format(k))
    def Language(self,b):
        if b.text() == "EN":
            if b.isChecked() == True:
                for i in range(len(self.keybuttons)):
                    if i!= 38:
                        self.keybuttons[i].setText(str(self.eng[i]))
                self.lng = 'EN'
        if b.text() == "RU":
            if b.isChecked() == True:
                for i in range(len(self.keybuttons)):
                    if i!= 38:
                        self.keybuttons[i].setText(str(self.rus[i]))
                self.lng = 'RU'
    def Restart(self):
        if self.clr != -1:
            if self.clr in [0,14,26,27,40,51,11,12,13,23,24,25,36,37,38,39,50]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(255, 255, 127) } """)
            if self.clr in [1,2,15,28,41,10,22,35,49]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(0, 170, 255) } """)
            if self.clr in [3,4,16,29,42,8,9,21,34,48]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(170, 255, 127) } """)
            if self.clr in [5,6,17,18,30,31,43,44,45]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(253, 116, 141) } """)
            if self.clr in [7,19,20,32,33,46,47]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(170, 170, 255) } """)
            if self.clr in [52]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(184, 184, 184) } """)
            if self.clr in [53]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(85, 170, 127) } """)
        if self.b != -1:
            self.keybuttons[40].setStyleSheet("""  QPushButton:!hover { background-color: rgb(255, 255, 127) } """)
        self.answershit.setText('')
        self.testplace.setHtml('')
        for i in range(len(self.keybuttons)):
                    if i!= 38:
                        self.keybuttons[i].setText(str(self.rus[i]))
        self.RU.setChecked(True)
        self.text = ''
        self.data = ''
        self.clr = -1
        self.lng = 'RU'
        self.b = -1
        self.capslock = 0
        self.result.setText('Результат:')
    '''def event(self, event):
        if (event.type() == QEvent.KeyPress) and (event.key() == Qt.Key_Space):
            print(foo)'''
    def keyPressEvent(self, event):
        if self.clr != -1:
            if self.clr in [0,14,26,27,40,51,11,12,13,23,24,25,36,37,38,39,50]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(255, 255, 127) } """)
            if self.clr in [1,2,15,28,41,10,22,35,49]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(0, 170, 255) } """)
            if self.clr in [3,4,16,29,42,8,9,21,34,48]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(170, 255, 127) } """)
            if self.clr in [5,6,17,18,30,31,43,44,45]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(253, 116, 141) } """)
            if self.clr in [7,19,20,32,33,46,47]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(170, 170, 255) } """)
            if self.clr in [52]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(184, 184, 184) } """)
            if self.clr in [53]:
                self.keybuttons[self.clr].setStyleSheet("""  QPushButton:!hover { background-color: rgb(85, 170, 127) } """)
        if self.b != -1:
            self.keybuttons[40].setStyleSheet("""  QPushButton:!hover { background-color: rgb(255, 255, 127) } """)
        if len(self.text) % 151 == 0:
            self.text = self.text + '\n'
            self.answershit.setText(self.text)
        if int(event.modifiers()) == (QtCore.Qt.ShiftModifier + QtCore.Qt.ControlModifier):
            self.b = 1
            self.clr = 51
            if self.lng == 'RU':
                self.lng = 'EN'
                self.EN.setChecked(True)
            else:
                self.lng = 'RU'
                self.RU.setChecked(True)
        elif int(event.modifiers()) == (QtCore.Qt.ShiftModifier):
            self.b = 1
            if event.nativeScanCode() == 2:
                self.text += '!'
                self.answershit.setText(self.text)
                self.btn_1.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 1
            elif event.nativeScanCode() == 3:
                if self.lng == 'RU':
                    self.text += '"'
                else:
                    self.text += '@'
                self.answershit.setText(self.text)
                self.btn_2.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 2
            elif event.nativeScanCode() == 4:
                if self.lng == 'RU':
                    self.text += '№'
                else:
                    self.text += '#'
                self.answershit.setText(self.text)
                self.btn_3.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 3
            elif event.nativeScanCode() == 5:
                if self.lng == 'RU':
                    self.text += ';'
                else:
                    self.text += '$'
                self.answershit.setText(self.text)
                self.btn_4.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 4
            elif event.nativeScanCode() == 6:
                if self.lng == 'RU':
                    self.text += '%'
                else:
                    self.text += '%'
                self.answershit.setText(self.text)
                self.btn_5.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 5
            elif event.nativeScanCode() == 7:
                if self.lng == 'RU':
                    self.text += ':'
                else:
                    self.text += '^'
                self.answershit.setText(self.text)
                self.btn_6.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 6
            elif event.nativeScanCode() == 8:
                if self.lng == 'RU':
                    self.text += '?'
                else:
                    self.text += '&'
                self.answershit.setText(self.text)
                self.btn_7.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 7
            elif event.nativeScanCode() == 9:
                if self.lng == 'RU':
                    self.text += '*'
                else:
                    self.text += '*'
                self.answershit.setText(self.text)
                self.btn_8.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 8
            elif event.nativeScanCode() == 10:
                if self.lng == 'RU':
                    self.text += '('
                else:
                    self.text += '('
                self.answershit.setText(self.text)
                self.btn_9.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 9
            elif event.nativeScanCode() == 11:
                if self.lng == 'RU':
                    self.text += ')'
                else:
                    self.text += ')'
                self.answershit.setText(self.text)
                self.btn_0.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 10
            elif event.nativeScanCode() == 12:
                if self.lng == 'RU':
                    self.text += '_'
                else:
                    self.text += '_'
                self.answershit.setText(self.text)
                self.btn_minus.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 11
            elif event.nativeScanCode() == 13:
                if self.lng == 'RU':
                    self.text += '+'
                else:
                    self.text += '+'
                self.answershit.setText(self.text)
                self.btn_plus.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 12
                
            elif event.nativeScanCode() == 16:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'й'
                    else:
                        self.text += 'Й'
                else:
                    if self.capslock == 1:
                        self.text += 'q'
                    else:
                        self.text += 'Q'
                self.answershit.setText(self.text)
                self.btn_q.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 14
            elif event.nativeScanCode() == 17:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ц'
                    else:
                        self.text += 'Ц'
                else:
                    if self.capslock == 1:
                        self.text += 'w'
                    else:
                        self.text += 'W'
                self.answershit.setText(self.text)
                self.btn_w.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 15
            elif event.nativeScanCode() == 18:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'у'
                    else:
                        self.text += 'У'
                else:
                    if self.capslock == 1:
                        self.text += 'e'
                    else:
                        self.text += 'E'
                self.answershit.setText(self.text)
                self.btn_e.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 16
            elif event.nativeScanCode() == 19:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'к'
                    else:
                        self.text += 'К'
                else:
                    if self.capslock == 1:
                        self.text += 'r'
                    else:
                        self.text += 'R'
                self.answershit.setText(self.text)
                self.btn_r.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 17
            elif event.nativeScanCode() == 20:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'е'
                    else:
                        self.text += 'Е'
                else:
                    if self.capslock == 1:
                        self.text += 't'
                    else:
                        self.text += 'T'
                self.answershit.setText(self.text)
                self.btn_t.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 18
            elif event.nativeScanCode() == 21:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'н'
                    else:
                        self.text += 'Н'
                else:
                    if self.capslock == 1:
                        self.text += 'y'
                    else:
                        self.text += 'Y'
                self.answershit.setText(self.text)
                self.btn_y.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 19
            elif event.nativeScanCode() == 22:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'г'
                    else:
                        self.text += 'Г'
                else:
                    if self.capslock == 1:
                        self.text += 'u'
                    else:
                        self.text += 'U'
                self.answershit.setText(self.text)
                self.btn_u.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 20
            elif event.nativeScanCode() == 23:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ш'
                    else:
                        self.text += 'Ш'
                else:
                    if self.capslock == 1:
                        self.text += 'i'
                    else:
                        self.text += 'I'
                self.answershit.setText(self.text)
                self.btn_i.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 21
            elif event.nativeScanCode() == 24:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'щ'
                    else:
                        self.text += 'Щ'
                else:
                    if self.capslock == 1:
                        self.text += 'o'
                    else:
                        self.text += 'O'
                self.answershit.setText(self.text)
                self.btn_o.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 22
            elif event.nativeScanCode() == 25:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'з'
                    else:
                        self.text += 'З'
                else:
                    if self.capslock == 1:
                        self.text += 'p'
                    else:
                        self.text += 'P'
                self.answershit.setText(self.text)
                self.btn_p.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 23
            elif event.nativeScanCode() == 30:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ф'
                    else:
                        self.text += 'Ф'
                else:
                    if self.capslock == 1:
                        self.text += 'a'
                    else:
                        self.text += 'A'
                self.answershit.setText(self.text)
                self.btn_a.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 27
            elif event.nativeScanCode() == 31:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ы'
                    else:
                        self.text += 'Ы'
                else:
                    if self.capslock == 1:
                        self.text += 's'
                    else:
                        self.text += 'S'
                self.answershit.setText(self.text)
                self.btn_s.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 28
            elif event.nativeScanCode() == 32:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'в'
                    else:
                        self.text += 'В'
                else:
                    if self.capslock == 1:
                        self.text += 'd'
                    else:
                        self.text += 'D'
                self.answershit.setText(self.text)
                self.btn_d.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 29
            elif event.nativeScanCode() == 33:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'а'
                    else:
                        self.text += 'А'
                else:
                    if self.capslock == 1:
                        self.text += 'f'
                    else:
                        self.text += 'F'
                self.answershit.setText(self.text)
                self.btn_f.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 30
            elif event.nativeScanCode() == 34:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'п'
                    else:
                        self.text += 'П'
                else:
                    if self.capslock == 1:
                        self.text += 'g'
                    else:
                        self.text += 'G'
                self.answershit.setText(self.text)
                self.btn_g.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 31
            elif event.nativeScanCode() == 35:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'р'
                    else:
                        self.text += 'Р'
                else:
                    if self.capslock == 1:
                        self.text += 'h'
                    else:
                        self.text += 'H'
                self.answershit.setText(self.text)
                self.btn_h.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 32
            elif event.nativeScanCode() == 36:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'о'
                    else:
                        self.text += 'О'
                else:
                    if self.capslock == 1:
                        self.text += 'j'
                    else:
                        self.text += 'J'
                self.answershit.setText(self.text)
                self.btn_j.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 33
            elif event.nativeScanCode() == 37:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'л'
                    else:
                        self.text += 'Л'
                else:
                    if self.capslock == 1:
                        self.text += 'k'
                    else:
                        self.text += 'K'
                self.answershit.setText(self.text)
                self.btn_k.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 34
            elif event.nativeScanCode() == 38:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'д'
                    else:
                        self.text += 'Д'
                else:
                    if self.capslock == 1:
                        self.text += 'l'
                    else:
                        self.text += 'L'
                self.answershit.setText(self.text)
                self.btn_l.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 35
            elif event.nativeScanCode() == 44:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'я'
                    else:
                        self.text += 'Я'
                else:
                    if self.capslock == 1:
                        self.text += 'z'
                    else:
                        self.text += 'Z'
                self.answershit.setText(self.text)
                self.btn_z.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 41
            elif event.nativeScanCode() == 45:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ч'
                    else:
                        self.text += 'Ч'
                else:
                    if self.capslock == 1:
                        self.text += 'x'
                    else:
                        self.text += 'X'
                self.answershit.setText(self.text)
                self.btn_x.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 42
            elif event.nativeScanCode() == 46:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'с'
                    else:
                        self.text += 'С'
                else:
                    if self.capslock == 1:
                        self.text += 'c'
                    else:
                        self.text += 'C'
                self.answershit.setText(self.text)
                self.btn_c.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 43
            elif event.nativeScanCode() == 47:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'м'
                    else:
                        self.text += 'М'
                else:
                    if self.capslock == 1:
                        self.text += 'v'
                    else:
                        self.text += 'V'
                self.answershit.setText(self.text)
                self.btn_v.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 44
            elif event.nativeScanCode() == 48:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'и'
                    else:
                        self.text += 'И'
                else:
                    if self.capslock == 1:
                        self.text += 'b'
                    else:
                        self.text += 'B'
                self.answershit.setText(self.text)
                self.btn_b.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 45
            elif event.nativeScanCode() == 49:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'т'
                    else:
                        self.text += 'Т'
                else:
                    if self.capslock == 1:
                        self.text += 'n'
                    else:
                        self.text += 'N'
                self.answershit.setText(self.text)
                self.btn_n.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 46
            elif event.nativeScanCode() == 50:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ь'
                    else:
                        self.text += 'Ь' 
                else:
                    if self.capslock == 1:
                        self.text += 'm'
                    else:
                        self.text += 'M'
                self.answershit.setText(self.text)
                self.btn_m.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 47
            elif event.key() == Qt.Key_CapsLock:
                pass
            elif event.key() == Qt.Key_Backspace:
                self.btn_backspace.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 13
            elif event.nativeScanCode() == 41:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ё'
                    else:
                        self.text += 'Ё' 
                else:
                    if self.capslock == 1:
                        self.text += '~'
                    else:
                        self.text += '~'
                self.answershit.setText(self.text)
                self.btn_io.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 0
            elif event.nativeScanCode() == 26:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'х'
                    else:
                        self.text += 'Х' 
                else:
                    if self.capslock == 0:
                        self.text += '{'
                    else:
                        self.text += '{'
                self.answershit.setText(self.text)
                self.btn_xa.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 24
            elif event.nativeScanCode() == 27:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ъ'
                    else:
                        self.text += 'Ъ' 
                else:
                    if self.capslock == 0:
                        self.text += '}'
                    else:
                        self.text += '}'
                self.answershit.setText(self.text)
                self.btn_tv_zn.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 25
            elif event.nativeScanCode() == 39:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ж'
                    else:
                        self.text += 'Ж' 
                else:
                    if self.capslock == 1: 
                        self.text += ':'
                    else:
                        self.text += ':'
                self.answershit.setText(self.text)
                self.btn_gh.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 36
            elif event.nativeScanCode() == 40:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'э'
                    else:
                        self.text += 'Э' 
                else:
                    if self.capslock == 1:
                        self.text += '"'
                    else:
                        self.text += '"'
                self.answershit.setText(self.text)
                self.btn_ei.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 37
            elif event.nativeScanCode() == 51:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'б'
                    else:
                        self.text += 'Б' 
                else:
                    if self.capslock == 0:
                        self.text += '<'
                    else:
                        self.text += '<'
                self.answershit.setText(self.text)
                self.btn_be.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 48
            elif event.nativeScanCode() == 52:
                if self.lng == 'RU':
                    if self.capslock == 1:
                        self.text += 'ю' 
                    else:
                        self.text += 'Ю' 
                else:
                    if self.capslock == 0:
                        self.text += '>'
                    else:
                        self.text += '>'
                self.answershit.setText(self.text)
                self.btn_iu.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 49
            elif event.nativeScanCode() == 53:
                if self.lng == 'RU':
                    self.text += ',' 
                else:
                    self.text += "?"
                self.answershit.setText(self.text)
                self.btn_dot.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 50
            elif event.nativeScanCode() == 28:
                self.btn_enter.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 39
            elif event.nativeScanCode() == 42:
                self.btn_shift.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 40
            elif event.nativeScanCode() == 29:
                self.btn_ctrl.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 51
            elif event.nativeScanCode() == 56:
                self.btn_alt.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
                self.clr = 52
            
        elif event.key() == Qt.Key_1:
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
        elif event.nativeScanCode() == 16:
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
        elif event.nativeScanCode() == 17:
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
        elif event.nativeScanCode() == 18:
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
        elif event.nativeScanCode() == 19:
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
        elif event.nativeScanCode() == 20:
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
        elif event.nativeScanCode() == 21:
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
        elif event.nativeScanCode() == 22:
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
        elif event.nativeScanCode() == 23:
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
        elif event.nativeScanCode() == 24:
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
        elif event.nativeScanCode() == 25:
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
        elif event.nativeScanCode() == 30:
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
        elif event.nativeScanCode() == 31:
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
        elif event.nativeScanCode() == 32:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'в'
                else:
                    self.text += 'В'
            else:
                if self.capslock == 0:
                    self.text += 'd'
                else:
                    self.text += 'D'
            self.answershit.setText(self.text)
            self.btn_d.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 29
        elif event.nativeScanCode() == 33:
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
        elif event.nativeScanCode() == 34:
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
        elif event.nativeScanCode() == 35:
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
        elif event.nativeScanCode() == 36:
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
        elif event.nativeScanCode() == 37:
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
        elif event.nativeScanCode() == 38:
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
        elif event.nativeScanCode() == 44:
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
        elif event.nativeScanCode() == 45:
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
        elif event.nativeScanCode() == 46:
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
        elif event.nativeScanCode() == 47:
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
        elif event.nativeScanCode() == 48:
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
        elif event.nativeScanCode() == 49:
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
        elif event.nativeScanCode() == 50:
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
        elif event.key() == Qt.Key_CapsLock:
            if self.capslock == 0:
                self.capslock = 1
                self.btn_capslock.setStyleSheet("""QPushButton:!hover { color: rgb(255, 0, 0); }""")
            else:
                self.capslock = 0
                self.btn_capslock.setStyleSheet("""QPushButton:!hover { color: rgb(255, 0, 0); }""")
            self.clr = 26
        elif event.key() == Qt.Key_Backspace:
            self.text = self.text[:-1]
            self.answershit.setText(self.text)
            self.btn_backspace.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 13 
        elif event.nativeScanCode() == 41:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ё'
                else:
                    self.text += 'Ё' 
            else:
                if self.capslock == 0:
                    self.text += '`'
                else:
                    self.text += '`'
            self.answershit.setText(self.text)
            self.btn_io.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 0
        elif event.nativeScanCode() == 12:
            self.text += '-'
            self.answershit.setText(self.text)
            self.btn_minus.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 11
        elif event.nativeScanCode() == 13:
            self.text += '='
            self.answershit.setText(self.text)
            self.btn_plus.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 12
        elif event.nativeScanCode() == 26:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'х'
                else:
                    self.text += 'Х' 
            else:
                if self.capslock == 0:
                    self.text += '['
                else:
                    self.text += '['
            self.answershit.setText(self.text)
            self.btn_xa.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 24
        elif event.nativeScanCode() == 27:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ъ'
                else:
                    self.text += 'Ъ' 
            else:
                if self.capslock == 0:
                    self.text += ']'
                else:
                    self.text += ']'
            self.answershit.setText(self.text)
            self.btn_tv_zn.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 25
        elif event.nativeScanCode() == 39:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ж'
                else:
                    self.text += 'Ж' 
            else:
                if self.capslock == 0:
                    self.text += ';'
                else:
                    self.text += ';'
            self.answershit.setText(self.text)
            self.btn_gh.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 36
        elif event.nativeScanCode() == 40:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'э'
                else:
                    self.text += 'Э' 
            else:
                if self.capslock == 0:
                    self.text += "'"
                else:
                    self.text += "'"
            self.answershit.setText(self.text)
            self.btn_ei.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 37
        elif event.nativeScanCode() == 51:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'б'
                else:
                    self.text += 'Б' 
            else:
                if self.capslock == 0:
                    self.text += ','
                else:
                    self.text += ','
            self.answershit.setText(self.text)
            self.btn_be.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 48
        elif event.nativeScanCode() == 52:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += 'ю'
                else:
                    self.text += 'Ю' 
            else:
                if self.capslock == 0:
                    self.text += '.'
                else:
                    self.text += '.'
            self.answershit.setText(self.text)
            self.btn_iu.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 49
        elif event.nativeScanCode() == 53:
            if self.lng == 'RU':
                if self.capslock == 0:
                    self.text += '.'
                else:
                    self.text += '.' 
            else:
                if self.capslock == 0:
                    self.text += "/"
                else:
                    self.text += '/'
            self.answershit.setText(self.text)
            self.btn_dot.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 50
        elif event.nativeScanCode() == 28:
            self.text += '\n'
            self.answershit.setText(self.text)
            self.btn_enter.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 39
        elif event.nativeScanCode() == 42:
            self.btn_shift.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 40
        elif event.nativeScanCode() == 29:
            self.btn_ctrl.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 51
        elif event.nativeScanCode() == 56:
            self.btn_alt.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 52
        else:
            self.text+=' '
            self.answershit.setText(self.text)
            self.btn_space.setStyleSheet("""QPushButton:!hover { background-color: rgb(255, 255, 255); }""")
            self.clr = 53

            
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
Qt.Key_Underscore
