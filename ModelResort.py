import sys
import PyQt5.QtWidgets as QW


class ModelResort(QW.QMainWindow):
    def __init__(self, parent=None):
        super(ModelResort, self).__init__(parent)


def main():
    app = QW.QApplication(sys.argv)
    w = ModelResort()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
