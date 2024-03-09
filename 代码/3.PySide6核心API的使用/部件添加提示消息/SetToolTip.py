from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
# 创建一个应用程序实例
app = QApplication([])
# 创建一个窗口
window = QWidget()
window.setWindowTitle('Set Tool Tip Example')
window.resize(300, 100)
# 创建一个垂直布局
layout = QVBoxLayout()
# 创建一个按钮，并设置其文本和提示消息
button = QPushButton('button')
button.setToolTip('This is a button tool tip!')
# 将按钮添加到布局中
layout.addWidget(button)
# 设置窗口的布局
window.setLayout(layout)
# 显示窗口
window.show()
# 运行应用程序的主循环
app.exec()