import sys
import PyQt5.QtWidgets as QW


class MemoMod(QW.QWidget):
    def __init__(self, parent=None):
        super(MemoMod, self).__init__(parent)

        self.setWindowTitle('memo')
        self.resize(400, 600)

        # BasicWidget
        self.te = QW.QTextEdit()

        # layout
        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.te)
        self.setLayout(vbox0)

    def load_text(self, path):
        with open(path) as f:
            text = f.read()

        return text


def main():
    app = QW.QApplication(sys.argv)

    w = MemoMod()

    path = './../../memo.txt'
    text = w.load_text(path)
    w.te.setText(text)

    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
