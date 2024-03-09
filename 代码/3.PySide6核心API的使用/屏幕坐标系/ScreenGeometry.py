from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QPushButton, QTextEdit)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Print Window Geometry Example")
        self.resize(425, 425)

        button = QPushButton('打印窗口坐标和大小')
        button.clicked.connect(self.print_window_geometry)
        self.text_box = QTextEdit()
        self.text_box.setReadOnly(True)

        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.text_box)
        # 创建中央小部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # 打印窗口坐标和窗口大小
    def print_window_geometry(self):
        geometry = self.geometry()
        x, y, width, height = geometry.getRect()
        info = f"窗口坐标: ({x}, {y})\n窗口大小: 宽度 {width}, 高度 {height}"
        self.text_box.append(info)
        self.text_box.append("\n")

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
