import sys
import os
script_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_path + '/../'))

import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
from libs.matplotlib_mod import MatplotlibMod


class Indigo(QW.QMainWindow):
    def __init__(self, parent=None):
        super(Indigo, self).__init__(parent)
        self.setWindowTitle('Indigo')

        self.w_central = QW.QWidget()

        # ----------
        lbl_smple_img = QW.QLabel(self.w_central)
        lbl_smple_img.setPixmap(QG.QPixmap('./../images/sample/pyqt.png'))
        pixmap = QG.QPixmap('./../images/sample/pyqt.png')
        lbl_smple_img.setPixmap(pixmap.scaled(100, 100))
        # ----------

        self.mlp_widget = MatplotlibMod()
        self.mlp_widget.sample_plot()


        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.mlp_widget)
        vbox0.addWidget(lbl_smple_img)

        self.w_central.setLayout(vbox0)

        self.setCentralWidget(self.w_central)





def main():

    app = QW.QApplication(sys.argv)

    path = './../icon/images/indigo_icon.png'
    path = path.replace('/', str(os.sep))
    app.setWindowIcon(QIcon(path))

    w = Indigo()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
