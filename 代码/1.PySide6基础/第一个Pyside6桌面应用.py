# 从PySide6.QtWidgets模块导入QApplication, QLabel类
from PySide6.QtWidgets import QApplication, QLabel

# 创建QApplication类的实例， QApplication管理GUI应用程序的控制流和主要设置
app = QApplication([])
# 创建一个QLabel部件， QLabel是用来显示文本或图像的部件
label = QLabel("Hello World!")
# 显示标签，使它成为可见的
label.show()
# 启动应用程序的事件循环
app.exec()