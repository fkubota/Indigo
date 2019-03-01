import sys
import os
import glob
import pandas as pd
import numpy as np
import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set(style='darkgrid')


class DataBrowserMod(QW.QWidget):
    def __init__(self, parent=None):
        super(DataBrowserMod, self).__init__(parent)
        self.datasets = []
        self.sample_name_list = []
        self.feat_name_list = []

        self.setWindowTitle('Data Browser')
        self.resize(300, 600)
        # self.setStyleSheet('QWidget{background-color: #3E5280}')

        # basic widget
        self.lbl_feat0 = QW.QLabel('feat0')
        self.lbl_feat1 = QW.QLabel('feat1')
        self.lbl_class = QW.QLabel('class')
        self.btn_show_data = QW.QPushButton('Show Data')
        self.cb_feat0 = QW.QComboBox()
        self.cb_feat0.currentIndexChanged.connect(self.plot_sample_data)
        self.cb_feat1 = QW.QComboBox()
        self.cb_feat1.currentIndexChanged.connect(self.plot_sample_data)
        self.cb_class = QW.QComboBox()
        self.cb_class.currentIndexChanged.connect(self.plot_sample_data)

        # listview widget
        self.lv_data = QW.QListView()
        self.lv_data.setFixedHeight(150)
        self.item_model = QG.QStandardItemModel(self.lv_data)
        self.lv_data.setModel(self.item_model)
        self.lv_data.clicked.connect(self.lv_data_clikced)

        # matplotlib widget
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.figure.patch.set_facecolor('#F5F4FA')  # 図全体の背景色
        # self.ax.patch.set_facecolor('#3E5280')
        # self.ax.patch.set_facecolor('gray')
        toolbar = NavigationToolbar(self.canvas, parent=self.canvas)
        # toolbar.resize(1, 1)

        # layout
        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.lv_data)
        vbox0.addWidget(self.btn_show_data)
        vbox0.addWidget(self.lbl_feat0)
        vbox0.addWidget(self.cb_feat0)
        vbox0.addWidget(self.lbl_feat1)
        vbox0.addWidget(self.cb_feat1)
        vbox0.addWidget(self.lbl_class)
        vbox0.addWidget(self.cb_class)
        vbox0.addWidget(toolbar)
        vbox0.addWidget(self.canvas)
        self.setLayout(vbox0)
        self.sample_data_list = []

    def lv_data_clikced(self, selected_idx):
        self.cb_feat0.currentIndexChanged.disconnect(self.plot_sample_data)
        self.cb_feat1.currentIndexChanged.disconnect(self.plot_sample_data)
        self.cb_class.currentIndexChanged.disconnect(self.plot_sample_data)

        idx = selected_idx.row()
        feats = self.feat_name_list[idx]

        self.cb_feat0.clear()
        self.cb_feat1.clear()
        self.cb_class.clear()
        for feat in feats:
            self.cb_feat0.addItem(feat)
            self.cb_feat1.addItem(feat)
            self.cb_class.addItem(feat)
        self.plot_sample_data()

        self.cb_feat0.currentIndexChanged.connect(self.plot_sample_data)
        self.cb_feat1.currentIndexChanged.connect(self.plot_sample_data)
        self.cb_class.currentIndexChanged.connect(self.plot_sample_data)

    def plot_sample_data(self):
        self.ax.clear()
        # self.ax.patch.set_facecolor('#3E5280')
        self.canvas.draw()

        lv_idx = self.lv_data.currentIndex().row()
        feat0_idx = self.cb_feat0.currentIndex()
        feat1_idx = self.cb_feat1.currentIndex()
        class_idx = self.cb_class.currentIndex()

        df_dataset = self.datasets[lv_idx]
        feat0 = df_dataset.iloc[:, feat0_idx]
        feat1 = df_dataset.iloc[:, feat1_idx]
        classes = df_dataset.iloc[:, class_idx]
        if len(classes.unique()) > 10:
            return

        colors = ['r', 'b', 'g', 'o', 'c', 'm', 'y', 'b', 'gray', 'darkred']
        for class_i, class_ in enumerate(classes.unique()):
            self.ax.plot(feat0[classes == class_],
                         feat1[classes == class_],
                         lw=0, marker='o', markersize=5, alpha=0.5,
                         markeredgewidth=0, markerfacecolor=colors[class_i])
        self.canvas.draw()

    def get_sample_datasets(self, dir_sample_datasets):
        path_datasets_list = glob.glob(dir_sample_datasets + '/*.csv')
        for path_i, path in enumerate(path_datasets_list):
            dataset = pd.read_csv(path)
            self.datasets.append(dataset)
            self.feat_name_list.append(dataset.columns)

            sample_name = os.path.basename(path)
            self.sample_name_list.append(sample_name)
            item = QG.QStandardItem(sample_name)
            self.item_model.appendRow(item)

    def get_training_data(self):
        lv_idx = self.lv_data.currentIndex().row()
        feat0_idx = self.cb_feat0.currentIndex()
        feat1_idx = self.cb_feat1.currentIndex()
        label_idx = self.cb_class.currentIndex()

        dataset = self.datasets[lv_idx]
        feat0 = dataset.iloc[:, feat0_idx]
        feat1 = dataset.iloc[:, feat1_idx]
        X = np.array([feat0, feat1]).T
        y = np.array(dataset.iloc[:, label_idx])

        return X, y




def main():

    app = QW.QApplication(sys.argv)

    w = DataBrowserMod()
    dir_sample_datasets = './../../sample_datasets'
    w.get_sample_datasets(dir_sample_datasets=dir_sample_datasets)
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
