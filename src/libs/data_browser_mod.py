import sys
import os
import glob
import pandas as pd
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
        self.sample_name_list = []
        self.sample_data_list = []
        self.sample_dict = []
        self.datasets = []
        self.sample_name_list = []
        self.feat_name_list = []

        self.setWindowTitle('Data Browser')
        self.resize(300, 600)

        # basic widget
        self.lbl_selected_data = QW.QLabel()
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
        self.item_model = QG.QStandardItemModel(self.lv_data)
        self.lv_data.setModel(self.item_model)
        self.lv_data.clicked.connect(self.lv_data_clikced)
        sample_dict = self.get_sample_dict()
        # self.set_sample_dict2item_model(self.item_model, sample_dict)

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

        self.get_sample_datasets('./../../sample_datasets')

    def lv_data_clikced(self, selected_idx):
        idx = selected_idx.row()
        feats = self.feat_name_list[idx]
        for feat in feats:
            self.cb_feat0.clear()
            self.cb_feat1.clear()
            self.cb_class.clear()

            self.cb_feat0.addItem(feat)
            self.cb_feat1.addItem(feat)
            self.cb_class.addItem(feat)
        self.plot_sample_data()

    def get_sample_dict(self):
        # self.sample_name_list = ['sample1', 'sample2', 'sample3']
        # self.sample_data_list = [[1,2,3], [2,6,9], [5,1,8]]
        # self.sample_dict = {'sample_name_list': self.sample_name_list,
        #                     'sample_data_list': self.sample_data_list}
        # return self.sample_dict
        pass

    # def set_sample_names2item_model(self):
    #     for data_name in sample_dict['sample_name_list']:
    #         item = QG.QStandardItem(data_name)
    #         item_model.appendRow(item)

    def plot_sample_data(self):
        lv_idx = self.lv_data.currentIndex().row()
        feat0_idx = self.cb_feat0.currentIndex()
        feat1_idx = self.cb_feat1.currentIndex()
        class_idx = self.cb_class.currentIndex()

        df_dataset = self.datasets[lv_idx]
        feat0 = df_dataset.iloc[:, feat0_idx]
        feat1 = df_dataset.iloc[:, feat1_idx]
        classes = df_dataset.iloc[:, class_idx]
        print(len(classes.unique()))
        print(len(classes.unique())>10)
        if len(classes.unique()) > 10:
            print('plot shinaiyo')
            return
        print('plot suruyo')

        self.ax.clear()
        for class_ in classes:
            self.ax.plot(feat0[classes == class_],
                         feat1[classes == class_],
                         lw=0, marker='.', markersize=5, alpha=0.5)
        self.canvas.draw()
        # selected_idx = index.row()
        # sample_data0 = self.sample_data_list[0]
        # sample_data = self.sample_data_list[selected_idx]
        # self.ax.clear()
        # self.ax.plot(sample_data0, sample_data)
        # self.canvas.draw()

    # def show_sample_name(self, index):
    #     selected_idx = index.row()
    #     sample_name = self.sample_name_list[selected_idx]
    #     self.lbl_selected_data.setText(sample_name)

    def get_sample_datasets(self, dir_sample_datasets):
        path_datasets_list = glob.glob(dir_sample_datasets + '/*.csv')
        for path_i, path in enumerate(path_datasets_list):
            dataset = pd.read_csv(path)
            self.datasets.append(dataset)
            self.feat_name_list.append(dataset.columns)

            # listview にサンプル名を表示
            item = QG.QStandardItem(os.path.basename(path))
            self.item_model.appendRow(item)





















def main():

    app = QW.QApplication(sys.argv)

    w = DataBrowserMod()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
