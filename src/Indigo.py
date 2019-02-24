import sys
import os
import PyQt5.QtWidgets as QW
from PyQt5.QtGui import QIcon

class ModelResort(QW.QMainWindow):
    def __init__(self, parent=None):
        super(ModelResort, self).__init__(parent)


def main():
    app = QW.QApplication(sys.argv)
    path = './icon/images/indigo_icon.png'
    path = path.replace('/', str(os.sep))
    app.setWindowIcon(QIcon(path))
    w = ModelResort()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
