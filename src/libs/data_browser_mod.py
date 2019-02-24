import sys
import os
import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt


class DataBrowserMod(QW.QWidget):
    def __init__(self, parent=None):
        super(DataBrowserMod, self).__init__(parent)

        self.ui_main()

    def ui_main(self):
        self.setWindowTitle('Data Browser')

        # widget
        self.lbl_selected_data = QW.QLabel()
        self.lv_data = QW.QListView()
        self.item_model = QG.QStandardItemModel(self.lv_data)
        self.lv_data.setModel(self.item_model)
        self.lv_data.clicked.connect(self.show_sample_name)

        sample_dict = self.get_sample_dict()
        self.set_sample_dict2item_model(self.item_model, sample_dict)

        # layout
        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.lbl_selected_data)
        vbox0.addWidget(self.lv_data)
        self.setLayout(vbox0)

    def get_sample_dict(self):
        self.sample_name_list = ['sample1', 'sample2', 'sample3']
        self.sample_data_list = [1, 2, 3]
        self.sample_dict = {'sample_name_list' : self.sample_name_list,
                       'sample_data_list' : self.sample_data_list}
        return self.sample_dict

    def set_sample_dict2item_model(self, item_model, sample_dict):
        for data_name in sample_dict['sample_name_list']:
            item = QG.QStandardItem(data_name)
            item_model.appendRow(item)

    def show_sample_name(self, index):
        selected_idx = index.row()
        self.lbl_selected_data.setText(self.sample_dict['sample_name_list'][selected_idx])


















def main():

    app = QW.QApplication(sys.argv)

    w = DataBrowserMod()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
