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
from libs.memo_mod import MemoMod
from libs.sample_images_mod import SampleImagesMod
from libs.check_module import make_gui

class Indigo(QW.QMainWindow):
    def __init__(self, parent=None):
        super(Indigo, self).__init__(parent)

        # constants
        self.DIR_SAMPLE_DATASETS = './../sample_datasets'
        self.DIR_ICON_IMAGES = './../images/icon'
        self.MEMO_PATH = './../memo.txt'
        self.SAMPLE_IMAGES_PATH = './../images/sample_images'

        # valiable
        self.model = 0

        # Mainwindow
        self.resize(1000, 700)
        self.setWindowTitle('Indigo')
        f = open("./../Indigo_stylesheet.css", "r")
        style = f.read()
        self.setStyleSheet(style)

        # Basic Widget @central widget
        self.space_boundary_plot = QW.QWidget()
        self.space_boundary_plot.setSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Fixed)
        self.spacer_tool0 = QW.QWidget()
        self.spacer_tool0.setSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Fixed)
        self.spacer_tool1 = QW.QWidget()
        self.spacer_tool1.setSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Fixed)
        self.spacer_cal = QW.QWidget()
        self.spacer_cal.setSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Fixed)
        self.w_central = QW.QWidget()
        self.lbl_from = QW.QLabel('from')
        self.lbl_import = QW.QLabel('import')
        self.lbl_args = QW.QLabel('args = ')
        self.lbl_format = QW.QLabel('.format')
        self.lbl_format_step = QW.QLabel('step')
        self.lbl_arrow_r0 = QW.QLabel('==>')
        self.lbl_arrow_r1 = QW.QLabel('==>')
        self.lbl_state_import = QW.QLabel('not yet')
        self.lbl_boundary_plot = QW.QLabel('plot boundary')
        self.le_from = QW.QLineEdit('sklearn.svm')
        self.le_import = QW.QLineEdit('SVC')
        self.le_args = QW.QLineEdit('gamma=0.2, C={}')
        self.le_format_step = QW.QLineEdit('0.1')
        self.le_format_step.setFixedWidth(50)
        self.le_format_step.editingFinished.connect(self.edited_le_format_stel)
        self.btn_calculation = QW.QPushButton('calculation')
        self.btn_calculation.setFixedWidth(120)
        self.btn_calculation.clicked.connect(self.exec_import_model)
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
        hbox_calculation = QW.QHBoxLayout()
        hbox_calculation.addWidget(self.spacer_cal)
        hbox_calculation.addWidget(self.btn_calculation)

        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.plt_widget)
        vbox0.addLayout(hbox_plot)
        vbox0.addLayout(hbox_model)
        vbox0.addLayout(hbox_args)
        vbox0.addLayout(hbox_calculation)
        self.w_central.setLayout(vbox0)


        # data browser mod
        self.data_browser_mod = DataBrowserMod()
        self.data_browser_mod.get_sample_datasets(dir_sample_datasets=self.DIR_SAMPLE_DATASETS)

        # memo_mod
        self.memo_mod = MemoMod()
        self.memo_mod.setStyleSheet(style)
        text = self.memo_mod.load_text(self.MEMO_PATH)
        self.memo_mod.te.setText(text)

        # sample_images_mod
        self.sample_images_mod = SampleImagesMod()
        self.sample_images_mod.setStyleSheet(style)
        self.sample_images_mod.load_images(self.SAMPLE_IMAGES_PATH)

        # check_module
        self.check_module = make_gui()
        self.check_module.setStyleSheet(style)

        # splitter0
        self.hsplitter0 = QW.QSplitter(QC.Qt.Horizontal)
        self.hsplitter0.addWidget(self.data_browser_mod)
        self.hsplitter0.addWidget(self.w_central)
        self.hsplitter0.setSizes([100, 10])
        self.setCentralWidget(self.hsplitter0)

        # toolbar
        self.action_memo = QW.QAction(QG.QIcon(self.DIR_ICON_IMAGES + '/memo.png'), 'memo', self)
        self.action_memo.triggered.connect(self.memo_mod.show)
        self.action_sample_images = QW.QAction(QG.QIcon(self.DIR_ICON_IMAGES + '/image.png'), 'sample_images', self)
        self.action_sample_images.triggered.connect(self.sample_images_mod.show)
        self.action_check_module = QW.QAction(QG.QIcon(self.DIR_ICON_IMAGES + '/check_module.png'), 'check_module', self)
        self.action_check_module.triggered.connect(self.check_module.show)
        self.toolbar = self.addToolBar('')
        self.toolbar.setIconSize(QC.QSize(40, 40))
        self.toolbar.setStyleSheet('background-color: #3E5280')
        self.toolbar.addWidget(self.spacer_tool0)
        self.toolbar.addAction(self.action_memo)
        self.toolbar.addAction(self.action_sample_images)
        self.toolbar.addAction(self.action_check_module)
        self.toolbar.addWidget(self.spacer_tool1)

        # statusbar
        self.statusBar().showMessage('hello')

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

    def edited_le_format_stel(self):
        step_val = float(self.le_format_step.text())
        self.spinbox_format.setSingleStep(float(step_val))


def main():

    app = QW.QApplication(sys.argv)

    path = './../images/images/indigo_icon.png'
    path = path.replace('/', str(os.sep))
    app.setWindowIcon(QIcon(path))

    w = Indigo()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
