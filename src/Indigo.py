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
        self.DIR_ICON_IMAGES = './../icon'

        # valiable
        self.model = 0

        # Mainwindow
        self.resize(1000, 700)
        self.setWindowTitle('Indigo')
        f = open("./../myStyle_BlackBlue.css", "r")
        style = f.read()
        self.setStyleSheet(style)

        # Basic Widget @central widget
        self.space_boundary_plot = QW.QWidget()
        self.space_boundary_plot.setSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Fixed)
        self.w_central = QW.QWidget()
        self.lbl_from = QW.QLabel('from')
        self.lbl_import = QW.QLabel('import')
        self.lbl_args = QW.QLabel('args = ')
        self.lbl_format = QW.QLabel('.format')
        self.lbl_format_step = QW.QLabel('step')
        self.lbl_arrow_r0 = QW.QLabel('==>')
        self.lbl_arrow_r1 = QW.QLabel('==>')
        self.lbl_state_import = QW.QLabel('not yet')
        self.lbl_state_fit = QW.QLabel('not yet')
        self.lbl_boundary_plot = QW.QLabel('plot boundary')
        self.le_from = QW.QLineEdit('sklearn.svm')
        self.le_import = QW.QLineEdit('SVC')
        self.le_args = QW.QLineEdit('gamma=0.2, C={}')
        self.le_format_step = QW.QLineEdit('0.1')
        self.le_format_step.editingFinished.connect(self.edited_le_format_stel)
        self.btn_import_model = QW.QPushButton('import model')
        self.btn_import_model.clicked.connect(self.exec_import_model)
        self.btn_fit_model = QW.QPushButton('fit model')
        self.btn_fit_model.clicked.connect(self.exec_fit_model)
        self.spinbox_format = QW.QDoubleSpinBox()
        self.spinbox_format.setFixedWidth(70)
        self.spinbox_format.setValue(1)
        self.spinbox_format.setSingleStep(0.1)
        self.spinbox_format.setDecimals(3)
        self.spinbox_format.valueChanged.connect(self.exec_import_model)
        self.check_boundary_plot = QW.QCheckBox()
        self.check_boundary_plot.setChecked(True)

        # matplotlib_mod
        self.plt_widget = MatplotlibMod()

        # layout
        hbox_plot = QW.QHBoxLayout()
        hbox_plot.addWidget(self.check_boundary_plot)
        hbox_plot.addWidget(self.lbl_boundary_plot)
        hbox_plot.addWidget(self.space_boundary_plot)
        hbox_model = QW.QHBoxLayout()
        hbox_model.addWidget(self.lbl_from)
        hbox_model.addWidget(self.le_from)
        hbox_model.addWidget(self.lbl_import)
        hbox_model.addWidget(self.le_import)
        hbox_args = QW.QHBoxLayout()
        hbox_args.addWidget(self.lbl_args)
        hbox_args.addWidget(self.le_args)
        hbox_args.addWidget(self.lbl_format)
        hbox_args.addWidget(self.spinbox_format)
        hbox_args.addWidget(self.lbl_format_step)
        hbox_args.addWidget(self.le_format_step)
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
        vbox0.addLayout(hbox_plot)
        vbox0.addLayout(hbox_model)
        vbox0.addLayout(hbox_args)
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

        # toolbar
        self.add_region_wav = QW.QAction(QG.QIcon(self.DIR_ICON_IMAGES + '/indigo_icon.png'),
                                         'region', self)
        # self.add_region_wav.triggered.connect(self.show_region)
        self.toolber = self.addToolBar('')
        self.toolber.setStyleSheet('background-color: #3E5280')
        self.toolber.addAction(self.add_region_wav)

        # statusbar
        self.statusBar().showMessage('hello')
        # self.status.setStyleSheet('background-color: #3E5280')


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
        str_args_val = self.spinbox_format.value()
        str_exec_import_model = 'from {} import {}'.format(str_from, str_import)
        str_exec_create_model = 'self.model = {}({})'.format(str_import, str_args)
        if '{}' in str_exec_create_model:
            str_exec_create_model = str_exec_create_model.format(str_args_val)

        try:
            # import model
            exec(str_exec_import_model)

            # create instanse
            exec(str_exec_create_model)

        except:
            import traceback
            traceback.print_exc()
            print('error')
            return

        self.lbl_state_import.setText(str_import)

        self.exec_fit_model()

    def exec_fit_model(self):
        print('---')
        print('exec fit model')

        X, y = self.data_browser_mod.get_training_data()

        str_fit = 'self.model.fit(X, y)'
        try:
            exec(str_fit)
        except:
            print('error')
            return

        if self.check_boundary_plot.checkState():
            self.plt_widget.plot_decision_regions(X, y, self.model, resolution=0.02)
        else:
            self.plt_widget.plot_predicted_class(X, y, self.model, resolution=0.02)

        self.lbl_state_fit.setText(self.le_import.text())

    def edited_le_format_stel(self):
        step_val = float(self.le_format_step.text())
        self.spinbox_format.setSingleStep(float(step_val))


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
