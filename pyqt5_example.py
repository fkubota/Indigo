import sys
import PyQt5.QtWidgets as QW


class Sample(QW.QMainWindow):
    def __init__(self, parent=None):
        super(Sample, self).__init__(parent)


def main():
    app = QW.QApplication(sys.argv)
    w = Sample()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
