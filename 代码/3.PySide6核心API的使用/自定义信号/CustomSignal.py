from PySide6.QtWidgets import ( QApplication, QMainWindow, QWidget,
                                QTextEdit, QPushButton, QVBoxLayout)
from PySide6.QtCore import Signal

class MainWindow(QMainWindow):
    sendSignal = Signal(str)  # 自定义信号
    def __init__(self):
        super().__init__()
        self.setWindowTitle('主窗口')
        self.resize(400, 100)
        # 创建一个文本框
        self.text_box = QTextEdit()
        # 创建按钮，用于发送数据到子窗口
        send_button = QPushButton('发送数据到子窗口')
        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.text_box)
        layout.addWidget(send_button)
        # 设置中心小部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # 显示子窗口
        self.SubWindow = SubWindow(self)  # 传递 self 为 子窗口的 parent
        self.SubWindow.show()

        # 连接自定义信号 到子窗口文本更新 槽
        self.sendSignal.connect(self.SubWindow.receiveValue)
        # 连接按钮 到 发送信号 方法
        send_button.clicked.connect(self.sendValue)

    def sendValue(self):
        text = self.text_box.toPlainText()
        self.sendSignal.emit(text)

    def receiveValue(self, text):
        self.text_box.setText(text)

    def closeEvent(self, event):
        # 在主窗口关闭时，关闭子窗口
        if hasattr(self, 'SubWindow') and self.SubWindow:
            self.SubWindow.close()
        # 继续关闭主窗口
        super().closeEvent(event)

class SubWindow(QWidget):
    sendSignal = Signal(str)  # 自定义信号
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('子窗口')
        self.resize(400, 100)
        # 创建一个文本框
        self.text_box = QTextEdit()
        # 创建按钮，用于发送数据到子窗口
        send_button = QPushButton('发送数据到主窗口')
        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.text_box)
        layout.addWidget(send_button)
        # 设置布局
        self.setLayout(layout)

        # 连接自定义信号 到主窗口文本更新 槽
        self.sendSignal.connect(parent.receiveValue)
        # 连接按钮 到 发送信号 方法
        send_button.clicked.connect(self.sendValue)

    def sendValue(self):
        text = self.text_box.toPlainText()
        self.sendSignal.emit(text)

    def receiveValue(self, text):
        self.text_box.setText(text)

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
