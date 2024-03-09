from PySide6.QtWidgets import (QApplication, QWidget,
                               QTextEdit, QPushButton, QVBoxLayout)

# 创建应用程序实例
app = QApplication([])
# 创建主窗口实例
main_window = QWidget()
main_window.setWindowTitle('QWidget Example')

# 创建一个文本框
text_box = QTextEdit(main_window)
text_box.setPlainText('这是文本框中的内容')

# 创建一个按钮，点击时会关闭主窗口
close_button = QPushButton('退出', main_window)
# 将按钮的点击信号连接到事件处理函数
# 使用 lambda 函数来传递参数，确保在事件循环中调用 quit() 时，app 实例仍然有效
close_button.clicked.connect(lambda: app.quit())

# 创建一个垂直布局，并添加按钮
layout = QVBoxLayout(main_window)
layout.addWidget(text_box)
layout.addWidget(close_button)
# 设置widget的布局
main_window.setLayout(layout)

# 显示主窗口
main_window.show()
# 启动应用程序的事件循环
app.exec()
