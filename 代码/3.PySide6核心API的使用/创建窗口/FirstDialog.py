from PySide6.QtWidgets import (QApplication, QDialog,
                               QPushButton, QLabel, QVBoxLayout)
from PySide6.QtCore import Qt

# 创建应用程序实例
app = QApplication([])
# 创建模态对话框实例
dialog = QDialog()
# 设置对话框的标题
dialog.setWindowTitle('QDialog Example')
# 设置窗口大小
dialog.resize(400, 100)

# 设置对话框的模态级别
dialog.setWindowModality(Qt.ApplicationModal)

# 创建一个标签
dialog_label = QLabel('这是一个模态对话框里的标签', dialog)

# 创建一个按钮，用于关闭对话框
close_button = QPushButton('退出', dialog)
# 将按钮的点击信号连接到close方法
close_button.clicked.connect(dialog.close)

# 创建一个垂直布局
layout = QVBoxLayout()
# 将 QLabel 添加到布局
layout.addWidget(dialog_label)
# 将按钮添加到布局
layout.addWidget(close_button)
# 设置对话框的布局
dialog.setLayout(layout)

# 显示对话框
dialog.show()
# 启动应用程序的事件循环，等待用户操作
app.exec()
