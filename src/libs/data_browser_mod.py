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
        self.setWindowTitle('Data Browser')

        # basic widget
        self.lbl_selected_data = QW.QLabel()
        self.lbl_feat0 = QW.QLabel('feat0')
        self.lbl_feat1 = QW.QLabel('feat1')
        self.lbl_class = QW.QLabel('class')
        self.btn_show_data = QW.QPushButton('Show Data')
        self.cb_feat0 = QW.QComboBox()
        self.cb_feat1 = QW.QComboBox()
        self.cb_class = QW.QComboBox()

        # listview widget
        self.lv_data = QW.QListView()
        self.item_model = QG.QStandardItemModel(self.lv_data)
        self.lv_data.setModel(self.item_model)
        self.lv_data.clicked.connect(self.show_sample_name)
        self.lv_data.clicked.connect(self.plot_sample_data)
        sample_dict = self.get_sample_dict()
        self.set_sample_dict2item_model(self.item_model, sample_dict)

        # matplotlib widget
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        # layout
        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.lbl_selected_data)
        vbox0.addWidget(self.lv_data)
        vbox0.addWidget(self.btn_show_data)
        vbox0.addWidget(self.lbl_feat0)
        vbox0.addWidget(self.cb_feat0)
        vbox0.addWidget(self.lbl_feat1)
        vbox0.addWidget(self.cb_feat1)
        vbox0.addWidget(self.lbl_class)
        vbox0.addWidget(self.cb_class)
        vbox0.addWidget(self.canvas)
        self.setLayout(vbox0)

    def get_sample_dict(self):
        self.sample_name_list = ['sample1', 'sample2', 'sample3']
        self.sample_data_list = [[1,2,3], [2,6,9], [5,1,8]]
        self.sample_dict = {'sample_name_list': self.sample_name_list,
                            'sample_data_list': self.sample_data_list}

        return self.sample_dict

    def set_sample_dict2item_model(self, item_model, sample_dict):
        for data_name in sample_dict['sample_name_list']:
            item = QG.QStandardItem(data_name)
            item_model.appendRow(item)

    def plot_sample_data(self, index):
        selected_idx = index.row()
        sample_data0 = self.sample_data_list[0]
        sample_data = self.sample_data_list[selected_idx]
        self.ax.clear()
        print(sample_data)
        self.ax.plot(sample_data0, sample_data)
        self.canvas.draw()

    def show_sample_name(self, index):
        selected_idx = index.row()
        sample_name = self.sample_name_list[selected_idx]
        self.lbl_selected_data.setText(sample_name)


















def main():

    app = QW.QApplication(sys.argv)

    w = DataBrowserMod()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
