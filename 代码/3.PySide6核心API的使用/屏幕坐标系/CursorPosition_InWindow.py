from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("鼠标移动跟踪示例")
        self.setGeometry(100, 100, 800, 600)

    def mouseMoveEvent(self, event):
        # 获取鼠标当前位置
        x = event.position().x()
        y = event.position().y()
        print(f"鼠标当前位置：X = {x}, Y = {y}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
