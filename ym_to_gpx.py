import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow
from convert_to_gpx import main


def open_base_folder():
    path = os.getcwd()
    os.startfile(path)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.download_gpx)
        self.ui.pushButton_2.clicked.connect(open_base_folder)

    def test(self):
        test = self.ui.lineEdit.text()
        self.ui.pushButton_2.setText(test)

    def download_gpx(self):
        url = self.ui.lineEdit.text()

        self.ui.textLabel_2.setText("Downloading GPX")

        result = main(url)
        self.ui.textLabel_2.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
