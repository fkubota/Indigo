import sys
import PyQt5.QtWidgets as QW
import PyQt5.QtGui as QG
import PyQt5.QtCore as QC
import glob


class SampleImagesMod(QW.QWidget):
    def __init__(self, parent=None):
        super(SampleImagesMod, self).__init__(parent)
        self.pixmap_list = []
        self.image_idx = 0
        self.n_image = 0

        self.setWindowTitle('Sample Images')
        self.resize(1200, 840)

        # BasicWidget
        self.btn_prev = QW.QPushButton('Prev')
        self.btn_prev.name = 'prev'
        self.btn_prev.setFixedWidth(100)
        self.btn_prev.clicked.connect(self.change_image)
        self.btn_next = QW.QPushButton('Next')
        self.btn_next.name = 'next'
        self.btn_next.setFixedWidth(100)
        self.btn_next.clicked.connect(self.change_image)
        self.spacer = QW.QWidget()
        self.spacer.setSizePolicy(QW.QSizePolicy.Expanding, QW.QSizePolicy.Fixed)

        # self.label = QW.QLabel()
        # self.label.setAlignment(QC.Qt.AlignLeft | QC.Qt.AlignTop)
        # self.label.setStyleSheet("background:violet;")
        self.view = QW.QGraphicsView()
        self.scene = QW.QGraphicsScene()
        self.view.setScene(self.scene)
        self.item = QW.QGraphicsPixmapItem()
        self.scene.addItem(self.item)

        # layout
        hbox_button = QW.QHBoxLayout()
        hbox_button.addWidget(self.spacer)
        hbox_button.addWidget(self.btn_prev)
        hbox_button.addWidget(self.btn_next)
        vbox0 = QW.QVBoxLayout()
        vbox0.addWidget(self.view)
        vbox0.addLayout(hbox_button)

        self.setLayout(vbox0)

    def load_images(self, images_dir):
        image_path_list = glob.glob(images_dir + '/*')
        print(image_path_list)
        self.n_image = len(image_path_list)
        for image_path in image_path_list:
            self.pixmap_list.append(QG.QPixmap(image_path))
        self.item.setPixmap(self.pixmap_list[0].scaledToWidth(1180))

    def change_image(self):
        btn = self.sender()
        name = btn.name

        if name == 'prev':
            self.image_idx -= 1
        if name == 'next':
            self.image_idx += 1

        # 0 < image_idx < n_image-1
        self.image_idx = min(self.n_image-1, self.image_idx)
        self.image_idx = max(0,            self.image_idx)

        # pixmap = self.pixmap_list[self.image_idx]
        # height = pixmap.height()
        # width  = pixmap.width()
        # if width > height:
        #     self.item.setPixmap(pixmap.scaledToWidth(1180))
        # else:
        #     self.item.setPixmap(pixmap.scaledToHeight(800))
        self.resizeEvent('')

    def resizeEvent(self, QResizeEvent):
        if len(self.pixmap_list) == 0:
            return

        pixmap = self.pixmap_list[self.image_idx]
        pixmap_width  = pixmap.width()
        pixmap_height = pixmap.height()

        view_width  = self.view.width()
        view_height = self.view.height()

        self.view.setSceneRect(0, 0, view_width, view_height)

        pixmap_aspect_ratio = pixmap_height / pixmap_width
        view_aspect_ratio   = view_height / view_width

        if pixmap_aspect_ratio > view_aspect_ratio:
            self.item.setPixmap(pixmap.scaledToHeight(view_height))
        else:
            self.item.setPixmap(pixmap.scaledToWidth(view_width))

        # if pixmap_width > pixmap_width:
        #     self.item.setPixmap(pixmap.scaledToWidth(view_width))
        # else:
        #     self.item.setPixmap(pixmap.scaledToHeight(view_height))




def main():
    app = QW.QApplication(sys.argv)

    w = SampleImagesMod()

    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
