import sys
import os
script_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_path + '/../'))
import time

import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from PyQt5.QtGui import QIcon
import matplotlib.pyplot as plt
from libs.matplotlib_mod import MatplotlibMod
from libs.data_browser_mod import DataBrowserMod


class Indigo(QW.QMainWindow):
    def __init__(self, parent=None):
        super(Indigo, self).__init__(parent)

        # constants
        self.DIR_SAMPLE_DATASETS = './../sample_datasets'

        # valiable
        self.model = 0

        # Mainwindow
        self.setWindowTitle('Indigo')
        f = open("./../myStyle_BlackBlue.css", "r")
        style = f.read()
        self.setStyleSheet(style)

        # Basic Widget @central widget
        self.w_central = QW.QWidget()
        self.lbl_from = QW.QLabel('from')
        self.lbl_import = QW.QLabel('import')
        self.lbl_args = QW.QLabel('args = ')
        self.lbl_arrow_r0 = QW.QLabel('==>')
        self.lbl_arrow_r1 = QW.QLabel('==>')
        self.lbl_state_import = QW.QLabel('not yet')
        self.lbl_state_fit = QW.QLabel('not yet')
        self.le_from = QW.QLineEdit('sklearn.svm')
        self.le_import = QW.QLineEdit('SVC')
        self.le_args = QW.QLineEdit('gamma=0.2, C=1.0')
        self.btn_import_model = QW.QPushButton('import model')
        self.btn_import_model.clicked.connect(self.exec_import_model)
        self.btn_fit_model = QW.QPushButton('fit model')
        self.btn_fit_model.clicked.connect(self.exec_fit_model)

        # matplotlib_mod
        self.plt_widget = MatplotlibMod()

        # layout
        hbox_model = QW.QHBoxLayout()
        hbox_model.addWidget(self.lbl_from)
        hbox_model.addWidget(self.le_from)
        hbox_model.addWidget(self.lbl_import)
        hbox_model.addWidget(self.le_import)
        hbox_model.addWidget(self.lbl_args)
        hbox_model.addWidget(self.le_args)
        hbox_model_status = QW.QHBoxLayout()
        hbox_model_status.addWidget(self.btn_import_model)
        hbox_model_status.addWidget(self.lbl_arrow_r0)
        hbox_model_status.addWidget(self.lbl_state_import)
        hbox_fit_status = QW.QHBoxLayout()
        hbox_fit_status.addWidget(self.btn_fit_model)
        hbox_fit_status.addWidget(self.lbl_arrow_r1)
        hbox_fit_status.addWidget(self.lbl_state_fit)

        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.plt_widget)
        vbox0.addLayout(hbox_model)
        vbox0.addLayout(hbox_model_status)
        vbox0.addLayout(hbox_fit_status)
        self.w_central.setLayout(vbox0)


        # data browser mod
        self.data_browser_mod = DataBrowserMod()
        self.data_browser_mod.get_sample_datasets(dir_sample_datasets=self.DIR_SAMPLE_DATASETS)

        # LeftDockWidget
        # dock_left = QW.QDockWidget()
        # dock_left.setWidget(data_browser_mod)
        # self.addDockWidget(QC.Qt.LeftDockWidgetArea, dock_left)

        # splitter0
        # self.w_hsplitter0 = QW.QWidget()
        self.hsplitter0 = QW.QSplitter(QC.Qt.Horizontal)
        self.hsplitter0.addWidget(self.data_browser_mod)
        self.hsplitter0.addWidget(self.w_central)
        self.hsplitter0.setSizes([100, 10])
        self.setCentralWidget(self.hsplitter0)


        # # ----------
        # lbl_smple_img = QW.QLabel(self.w_central)
        # lbl_smple_img.setPixmap(QG.QPixmap('./../images/sample/pyqt.png'))
        # pixmap = QG.QPixmap('./../images/sample/pyqt.png')
        # lbl_smple_img.setPixmap(pixmap.scaled(100, 100))
        # # ----------
        self.timer = QC.QTimer(self)
        self.timer.timeout.connect(self.lbl_state_fit.update)
        self.timer.start(200)#ミリ秒単位

    def exec_import_model(self):
        print('---')
        print('exec_import_model')
        str_from =   self.le_from.text()
        str_import = self.le_import.text()
        str_args =   self.le_args.text()
        str_exec = 'from {} import {}'.format(str_from, str_import)
        try:
            # import model
            exec(str_exec)

            # create instanse
            exec('self.model = {}({})'.format(str_import, str_args))

        except:
            import traceback
            traceback.print_exc()
            print('error')
            return

        self.lbl_state_import.setText(str_import)

    def exec_fit_model(self):
        print('---')
        print('exec fit model')

        self.lbl_state_fit.setText('Calculating')

        X, y = self.data_browser_mod.get_training_data()

        str_fit = 'self.model.fit(X, y)'
        try:
            exec(str_fit)
        except:
            print('error')
            return

        self.plt_widget.plot_decision_regions(X, y, self.model, resolution=0.02)

        self.lbl_state_fit.setText(self.le_import.text())










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
