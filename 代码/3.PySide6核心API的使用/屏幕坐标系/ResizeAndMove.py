from PySide6.QtWidgets import (QApplication, QDialog,
                               QVBoxLayout, QPushButton)
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

        self.margin = 10  # 确定鼠标位置是否在边缘或角落
        self.mouse_pressed = False  # 鼠标按下标志
        self.draggable = False  # 窗口可拖动标志

        # 添加一个按钮，用于关闭对话框
        close_button = QPushButton("关闭")
        close_button.clicked.connect(lambda: app.quit())
        # 设置窗口布局
        layout_main = QVBoxLayout()
        layout_main.addWidget(close_button, 0, Qt.AlignCenter)
        self.setLayout(layout_main)

    # 重写鼠标按下事件，处理窗口拖动和边缘调整
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
                    self.mouse_pressed = True  # 设置鼠标按下标志
                    self.offset = event.globalPosition() - self.frameGeometry().topLeft()
                    self.edge = self.get_resize_edge(event.position())  # 获取调整边缘
                    if self.edge is not None:
                        self.setCursor(self.get_resize_cursor(self.edge))  # 设置鼠标光标形状
                    else:
                        self.draggable = True  # 设置窗口可拖动标志
                        self.offset = event.position().toPoint()  # 更新偏移量

    # 重写鼠标移动事件，处理窗口拖动或调整窗口大小
    def mouseMoveEvent(self, event: QMouseEvent):
        if self.draggable:
            self.move(event.globalPosition().toPoint() - self.offset)    # 移动窗口
        if self.mouse_pressed and self.edge is not None:
            self.resize_window(event)    # 调整窗口大小

    # 重写鼠标释放事件，处理拖动结束
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.draggable = False  # 清除窗口可拖动标志
            self.mouse_pressed = False  # 清除鼠标按下标志
            self.edge = None  # 清除调整边缘
            self.setCursor(Qt.ArrowCursor)  # 恢复鼠标光标形状

    # 获取鼠标位置对应的调整边缘
    def get_resize_edge(self, pos):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        if pos.x() < self.margin and pos.y() < self.margin:
            return 'top_left'
        elif pos.x() > width - self.margin and pos.y() < self.margin:
            return 'top_right'
        elif pos.x() < self.margin and pos.y() > height - self.margin:
            return 'bottom_left'
        elif pos.x() > width - self.margin and pos.y() > height - self.margin:
            return 'bottom_right'
        elif pos.x() < self.margin:
            return 'left'
        elif pos.x() > width - self.margin:
            return 'right'
        elif pos.y() < self.margin:
            return 'top'
        elif pos.y() > height - self.margin:
            return 'bottom'
        else:
            return None

    # 设置适当的鼠标光标
    def get_resize_cursor(self, edge):
        if edge in ('top', 'bottom'):
            return Qt.SizeVerCursor
        elif edge in ('left', 'right'):
            return Qt.SizeHorCursor
        elif edge in ('top_left', 'bottom_right'):
            return Qt.SizeFDiagCursor
        elif edge in ('top_right', 'bottom_left'):
            return Qt.SizeBDiagCursor
        else:
            return Qt.ArrowCursor

    def resize_window(self, event):
        if self.edge is not None:
            global_pos = event.globalPosition()  # 全局鼠标位置
            local_pos = event.position()  # 局部（窗口内）鼠标位置
            x, y, w, h = self.x(), self.y(), self.width(), self.height()  # 当前窗口的位置和尺寸

            # 根据不同的边缘调整窗口的尺寸
            if self.edge in ('top', 'top_left', 'top_right'):
                delta_y = local_pos.y() - self.offset.y()
                y += delta_y
                h -= delta_y
            if self.edge in ('bottom', 'bottom_left', 'bottom_right'):
                h = global_pos.y() - y
            if self.edge in ('left', 'top_left', 'bottom_left'):
                delta_x = local_pos.x() - self.offset.x()
                x += delta_x
                w -= delta_x
            if self.edge in ('right', 'top_right', 'bottom_right'):
                w = global_pos.x() - x
            # 设置窗口的新位置和尺寸
            self.setGeometry(x, y, w, h)

if __name__ == '__main__':
    app = QApplication([])
    dialog = CustomDialog()
    dialog.show()
    app.exec()
