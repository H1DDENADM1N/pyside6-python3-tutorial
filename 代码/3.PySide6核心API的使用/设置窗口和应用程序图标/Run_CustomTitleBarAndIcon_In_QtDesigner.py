from Ui_CustomTitleBarAndIcon_In_QtDesigner import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt

class CustomDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.maximize_botton.clicked.connect(self.toggle_maximize_window)
    # 最大化窗口的槽函数
    def toggle_maximize_window(self):
        if self.windowState() & Qt.WindowMaximized:
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == '__main__':
    app = QApplication([])
    mainWindow = CustomDialog()
    mainWindow.show()
    app.exec()
