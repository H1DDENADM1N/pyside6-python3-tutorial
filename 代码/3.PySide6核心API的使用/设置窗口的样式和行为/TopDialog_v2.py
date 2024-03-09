from PySide6.QtWidgets import (QApplication, QDialog,
                               QVBoxLayout, QHBoxLayout,
                               QPushButton, QSizeGrip)
from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 500)
        # 设置窗口标志
        self.setWindowFlags(
            self.windowFlags()
            | Qt.FramelessWindowHint  # 隐藏标题栏
            | Qt.Tool  # 隐藏Windows任务栏上的图标
            | Qt.WindowStaysOnTopHint  # 置顶
        )
        # 添加一个按钮，用于关闭对话框
        close_button = QPushButton("关闭")
        close_button.clicked.connect(lambda: app.quit())
        # 添加可调整大小的角落小部件
        self.size_grip_top_left = QSizeGrip(self)
        self.size_grip_top_right = QSizeGrip(self)
        self.size_grip_bottom_left = QSizeGrip(self)
        self.size_grip_bottom_right = QSizeGrip(self)
        # 设置窗口布局
        layout_top = QHBoxLayout()
        layout_middle = QVBoxLayout()
        layout_bottom = QHBoxLayout()
        layout_top.addWidget(self.size_grip_top_left, 0, Qt.AlignTop | Qt.AlignLeft)
        layout_top.addWidget(self.size_grip_top_right, 0, Qt.AlignTop | Qt.AlignRight)
        layout_middle.addWidget(close_button, 0, Qt.AlignCenter)
        layout_bottom.addWidget(self.size_grip_bottom_left, 0, Qt.AlignBottom | Qt.AlignLeft)
        layout_bottom.addWidget(self.size_grip_bottom_right, 0, Qt.AlignBottom | Qt.AlignRight)
        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_top)
        layout_main.addLayout(layout_middle)
        layout_main.addLayout(layout_bottom)
        self.setLayout(layout_main)

    # 实现窗口的拖动功能
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.position().toPoint()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.draggable:
            self.move(event.globalPosition().toPoint() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.draggable = False

    # 失去焦点时隐藏角部小部件
    def enterEvent(self, event):
        super().enterEvent(event)
        self.size_grip_top_left.show()
        self.size_grip_top_right.show()
        self.size_grip_bottom_left.show()
        self.size_grip_bottom_right.show()

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.size_grip_top_left.hide()
        self.size_grip_top_right.hide()
        self.size_grip_bottom_left.hide()
        self.size_grip_bottom_right.hide()

if __name__ == '__main__':
    app = QApplication([])
    dialog = CustomDialog()
    dialog.show()
    app.exec()
