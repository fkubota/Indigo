# -*- coding: utf-8 -*-
"""
メソッドを確認

log
2017/08/10 作成開始
2017/08/11 完成
2017/08/19 textedit -> listview　これでクリックでクラスやメソッドを見れるようになった。
"""

import sys
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import PyQt5.QtWidgets as QW

class make_gui(QW.QWidget):
    def __init__(self, parent = None):
        super(make_gui, self).__init__(parent)  #superclassのコンストラクタを使用。
        # self.setWindowIcon(QG.QIcon('icon\Check_Module_icon.png'))
        self.setWindowTitle("Check Module")
        self.resize(350,500)
        self.move(100, 200)
        self.setStyleSheet("background-color: #4F90A8")

        self.lbl = QW.QLabel(".")
        self.lbl.setFont(QG.QFont("Helvetica", 25, QG.QFont.Bold))
        self.lbl.setStyleSheet('color:#D8D8D9')

        self.line0 = QW.QLineEdit()
        self.line0.setFont(QG.QFont("Helvetica", 15, QG.QFont.Bold))
        self.line0.setStyleSheet('color:#D8D8D9; background-color:#356074') #color:rgb(255, 100, 100)でもいける
        self.line0.editingFinished.connect(self.show_dir)
        self.line0.setPlaceholderText('import')

        self.line1 = QW.QLineEdit()
        self.line1.setFont(QG.QFont("Helvetica", 15, QG.QFont.Bold))
        self.line1.setStyleSheet('color:#D8D8D9; background-color:#356074')
        self.line1.editingFinished.connect(self.show_dir)
        self.line1.setPlaceholderText('class,method,...')

        self.lv = QW.QListView()
        self.lv.setStyleSheet('color:#D6CD90; background-color:#356074')
        self.lv.setFont(QG.QFont("Helvetica", 12, QG.QFont.Bold))
        self.model = QG.QStandardItemModel(self.lv)
        self.lv.setModel(self.model)
        self.lv.clicked.connect(self.item_clicked)

        self.btn = QW.QPushButton("help!!")
        self.btn.setFont(QG.QFont("Helvetica", 15, QG.QFont.Bold))
        self.btn.setStyleSheet('color:#D8D8D9; background-color:#356074')
        self.btn.clicked.connect(self.btn_cliked)

        self.status = QW.QStatusBar()
        self.status.showMessage("Hello!!")
        self.status.setStyleSheet('color:#D8D8D9')

        self.hbox = QW.QHBoxLayout()
        self.hbox.addWidget(self.line0)
        self.hbox.addWidget(self.lbl)
        self.hbox.addWidget(self.line1)
        self.hbox2 = QW.QHBoxLayout()
        self.hbox2.addWidget(self.status)
        self.hbox2.addWidget(self.btn)
        self.vbox = QW.QVBoxLayout()
        self.vbox.addLayout(self.hbox)
        #self.vbox.addWidget(self.textbox)
        self.vbox.addWidget(self.lv)
        self.vbox.addLayout(self.hbox2)
        self.setLayout(self.vbox)

        ##### helpwindow #####
        self.w_help = QW.QWidget()
        self.w_help.setWindowTitle("Help")
        self.w_help.move(500,100)
        self.w_help.resize(550,600)
        self.w_help.setWindowIcon(QG.QIcon('icon\Check_Module_icon.png'))
        self.w_help.setStyleSheet("background-color: #4F90A8")

        self.text_edit = QW.QTextEdit()
        self.text_edit.setFont(QG.QFont("Helvetica", 10, QG.QFont.Bold))
        self.text_edit.setStyleSheet('color:#D8D8D9; background-color:#356074')

        self.vbox2 = QW.QVBoxLayout()
        self.vbox2.addWidget(self.text_edit)
        self.w_help.setLayout(self.vbox2)


    def show_dir(self):
        self.model.clear()
        a = self.line0.text()
        b = self.line1.text()  #import "+ a+"   "try:\n   import " +a+ "\n   print(12)\n except:;  print(13)"
        text0 = """
try:
    import """+a+"""
    self.status.showMessage("OK!!")
except:
    self.status.showMessage("Error!!")
"""


        if b == "":
            text1 = "LIST = dir("+a+")"
        else:
            text1 = "LIST =dir("+a+"."+b+")"

        #text2 = "for i in range(len(LIST)):\n"+"    self.textbox.append(str(LIST[i]))"
        text2 = "for i in range(len(LIST)):\n"+"    item = QG.QStandardItem(str(LIST[i]))\n"+"    self.model.appendRow(item)"

        exec(text0)
        exec(text1)
        exec(text2)
        self.lv.verticalScrollBar().triggerAction(QW.QAbstractSlider.SliderToMinimum)  #スライダーを一番上に


    def item_clicked(self, item):
        add_text = item.data()
        if self.line1.text()=="":
            self.line1.setText(add_text)
        else:
            new_text = self.line1.text() +"."+ add_text
            self.line1.setText(new_text)

        self.show_dir()

    def btn_cliked(self):
        txt = self.line0.text() +"."+ self.line1.text() +".__doc__"
        text_exec = "import " +self.line0.text()+ " \nself.text_edit.setText("+txt+")"
        print(text_exec)
        exec(text_exec)
        self.w_help.show()

def main():
    app = QW.QApplication(sys.argv)

    myGUI = make_gui()
    myGUI.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
