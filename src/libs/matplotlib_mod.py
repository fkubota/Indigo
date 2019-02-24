from matplotlib.backends.backend_qt4agg import (FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
import matplotlib.pyplot as plt
import numpy as np
import PyQt5.QtWidgets as QW

class Matplotlib_mod(QW.QWidget):
    def __init__(self, parent=None):
        super(Matplotlib_mod, self).__init__(parent)

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



