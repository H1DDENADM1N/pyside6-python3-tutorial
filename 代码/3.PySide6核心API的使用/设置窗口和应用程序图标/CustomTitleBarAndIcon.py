from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QLabel,
                               QSpacerItem, QSizePolicy)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        icon_label = QLabel()
        icon_label.setPixmap(QIcon('.\\assets\\appicon.ico').pixmap(16, 16))  # 设置图标
        customtitle = QLabel("Custom Title")
        self.minimize_button = QPushButton("-")
        self.minimize_button.setMaximumSize(25, 25)
        self.maximize_button = QPushButton("[]")
        self.maximize_button.setMaximumSize(25, 25)
        self.close_button = QPushButton("X")
        self.close_button.setMaximumSize(25, 25)
        # 创建水平布局
        layout = QHBoxLayout()
        layout.addWidget(icon_label, 0, Qt.AlignCenter | Qt.AlignLeft)
        layout.addWidget(customtitle, 0, Qt.AlignCenter | Qt.AlignLeft)
        layout.addSpacerItem(QSpacerItem(80, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))  #  添加间隔
        layout.addWidget(self.minimize_button, 0, Qt.AlignCenter | Qt.AlignRight)
        layout.addWidget(self.maximize_button, 0, Qt.AlignCenter | Qt.AlignRight)
        layout.addWidget(self.close_button, 0, Qt.AlignCenter | Qt.AlignRight)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Title Bar Example")
        self.resize(400, 100)
        # 创建自定义标题栏实例
        custom_title_bar = CustomTitleBar(self)
        # 连接按钮信号/槽
        custom_title_bar.minimize_button.clicked.connect(self.showMinimized)
        custom_title_bar.maximize_button.clicked.connect(self.toggle_maximize_window)
        custom_title_bar.close_button.clicked.connect(self.close)
        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(custom_title_bar)
        # 创建中央小部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # 最大化窗口的槽函数
    def toggle_maximize_window(self):
        if self.windowState() & Qt.WindowMaximized:
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
