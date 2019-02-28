from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn as sns
sns.set(style='darkgrid')
import numpy as np
import PyQt5.QtWidgets as QW

class MatplotlibMod(QW.QWidget):
    def __init__(self, parent=None):
        super(MatplotlibMod, self).__init__(parent)

        # matplotlib
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        toolbar = NavigationToolbar(self.canvas, self.canvas)
        toolbar.resize(10, 10)

        # layout
        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(toolbar)
        vbox0.addWidget(self.canvas)
        self.setLayout(vbox0)

    def sample_plot(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()

    def plot_decision_regions(self, X, y, classifier, resolution=0.02):
        self.ax.clear()

        # setup marker generator and color map
        markers = ('o', 'x', 's', '^', 'v')
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])

        # plot the decision surface
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                               np.arange(x2_min, x2_max, resolution))
        Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        Z = Z.reshape(xx1.shape)
        self.ax.contourf(xx1, xx2, Z, alpha=0.1, cmap=cmap)
        self.ax.set_xlim(xx1.min(), xx1.max())
        self.ax.set_ylim(xx2.min(), xx2.max())

        for idx, cl in enumerate(np.unique(y)):
            self.ax.scatter(x=X[y == cl, 0],
                            y=X[y == cl, 1],
                            alpha=0.7,
                            c=colors[idx],
                            marker=markers[idx],
                            label=cl,
                            edgecolor='')

        self.canvas.draw()

    def plot_predicted_class(self, X, y, classifier, resolution=0.02):
        self.ax.clear()

        X_pred = classifier.predict(X)

        for class_ in np.unique(X_pred):
            self.ax.scatter(X[X_pred==class_, 0],
                            X[X_pred==class_, 1],
                            alpha=0.7,
                            edgecolor='')



        # # setup marker generator and color map
        # markers = ('o', 'x', 's', '^', 'v')
        # colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        # cmap = ListedColormap(colors[:len(np.unique(y))])
        #
        # # plot the decision surface
        # x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        # x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        # xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
        #                        np.arange(x2_min, x2_max, resolution))
        # Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        # Z = Z.reshape(xx1.shape)
        # self.ax.contourf(xx1, xx2, Z, alpha=0.1, cmap=cmap)
        # self.ax.set_xlim(xx1.min(), xx1.max())
        # self.ax.set_ylim(xx2.min(), xx2.max())
        #
        # for idx, cl in enumerate(np.unique(y)):
        #     self.ax.scatter(x=X[y == cl, 0],
        #                     y=X[y == cl, 1],
        #                     alpha=0.7,
        #                     c=colors[idx],
        #                     marker=markers[idx],
        #                     label=cl,
        #                     edgecolor='')

        self.canvas.draw()


