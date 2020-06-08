import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("BTN", self)
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50)
        btn1.clicked.connect(QCoreApplication.instance().quit)

        self.resize(500, 500)
        self.setWindowTitle("Test2")
        self.show()

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "close Confirm", "Do you want Close????", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv)
w = Test()
sys.exit(app.exec_()) # 이벤트 처리를 위한 루프 실행 부분