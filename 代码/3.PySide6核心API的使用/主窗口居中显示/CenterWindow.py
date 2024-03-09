from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('CenterWindow Example')
        self.resize(1000, 500)
        # 调用center方法将窗口移动到屏幕中央
        self.move_window_to_screen_center()

    # 将窗口移动到屏幕中央
    def move_window_to_screen_center(self):
        screen = QtGui.QGuiApplication.primaryScreen().availableGeometry()  # 获取主屏幕的可用区域  PySide6.QtCore.QRect(0, 0, 2560, 1400)
        size = self.geometry()  # 获取窗口的尺寸  PySide6.QtCore.QRect(0, 0, 1000, 500)
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)  # 移动窗口到屏幕中央

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
