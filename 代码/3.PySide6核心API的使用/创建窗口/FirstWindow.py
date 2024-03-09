import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog,
                               QMenuBar, QToolBar, QVBoxLayout,
                               QTextEdit, QPushButton, QLabel)
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # 调用父类QMainWindow的构造函数
        self.setWindowTitle('QMainWindow Example')
        self.resize(400, 100)

        # 设置菜单栏
        menu_bar = QMenuBar()  # 创建一个菜单栏
        this_menu = menu_bar.addMenu("这是菜单")  # 创建一个菜单
        exit_action = QAction("退出", self)  # 创建一个动作（菜单项）
        exit_action.triggered.connect(self.close)  # 将动作连接到关闭窗口的槽函数
        this_menu.addAction(exit_action)  # 将动作添加到菜单中
        self.setMenuBar(menu_bar)  # 将菜单栏添加到主窗口中

        # 设置工具栏
        tool_bar = QToolBar("主工具栏")  # 创建一个工具栏
        tool_bar_action = QAction("这是工具栏里的按钮", self)  # 创建一个动作（工具按钮）
        tool_bar.addAction(tool_bar_action)  # 将动作添加到工具栏中
        self.addToolBar(tool_bar)  # 将工具栏添加到主窗口中

        # 设置状态栏，5秒后消失
        self.statusBar().showMessage("这是状态栏，它会在5秒后消失", 5000)

        # 创建一个文本框
        text_box = QTextEdit()
        text_box.setPlainText('这是文本框中的内容')

        # 创建按钮，用于显示子窗口
        show_dialog_button = QPushButton('Show Dialog')
        show_independent_widget_button = QPushButton('Show Independent QWidget')
        show_nonindependent_widget_button = QPushButton('Show Non-Independent QWidget')
        show_dialog_button.clicked.connect(self.show_dialog)
        show_independent_widget_button.clicked.connect(self.show_independent_widget)
        show_nonindependent_widget_button.clicked.connect(self.show_nonindependent_widget)

        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(text_box)
        layout.addWidget(show_dialog_button)
        layout.addWidget(show_independent_widget_button)
        layout.addWidget(show_nonindependent_widget_button)

        # 设置中心小部件
        central_widget = QWidget()  # 创建一个中心小部件
        central_widget.setLayout(layout)  # 设置中心小部件布局
        self.setCentralWidget(central_widget)  # 设置中心小部件

    def show_dialog(self):
        self.dialog = DialogWindow(self)  # 创建一个对话框实例
        self.dialog.exec()  # 显示对话框并阻塞主窗口

    def show_independent_widget(self):
        self.independentsubwindow = IndependentSubWindow()  # 创建一个独立的QWidget子窗口实例
        self.independentsubwindow.show()  # 显示子窗口

    def show_nonindependent_widget(self):
        self.nonindependentsubwindow = NonIndependentSubWindow()
        self.nonindependentsubwindow.show()

    def closeEvent(self, event):
        # 在主窗口关闭时，首先关闭非独立的子窗口
        if hasattr(self, 'nonindependentsubwindow') and self.nonindependentsubwindow:
            # 这里使用hasattr函数来检查child_window属性是否存在，
            # 这是因为子窗口可能在没有被打开的情况下，
            # 主窗口就被关闭了（例如，用户直接点击窗口的关闭按钮）。
            # 如果直接尝试访问不存在的属性，会导致错误。通过使用hasattr，
            # 我们可以安全地检查属性是否存在。
            self.nonindependentsubwindow.close()
        # 继续关闭主窗口
        super().closeEvent(event)

# 对话框类
class DialogWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类QDialog的构造函数
        self.setWindowTitle('QDialog Example')
        self.resize(400, 100)

        # 设置对话框的模态级别
        self.setWindowModality(Qt.ApplicationModal)

        # 创建一个标签
        dialog_label = QLabel('这是一个模态对话框里的标签，在关闭这个窗口之前，你无法操作其他窗口')

        # 创建一个按钮，用于关闭对话框
        close_button = QPushButton('Close Dialog')
        close_button.clicked.connect(self.close)
        
        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(dialog_label)
        layout.addWidget(close_button)
        self.setLayout(layout)

# 独立的QWidget子窗口类
class IndependentSubWindow(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget的构造函数
        self.setWindowTitle('Independent QWidget Sub Window')
        self.resize(400, 100)

        # 创建一个标签
        widget_label = QLabel('你可以继续操作主窗口')

        # 创建一个按钮，用于关闭子窗口
        close_button = QPushButton('Close Sub Window')
        close_button.clicked.connect(self.close)

        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(widget_label)
        layout.addWidget(close_button)
        self.setLayout(layout)

class NonIndependentSubWindow(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类QWidget的构造函数
        self.setWindowTitle('Non-independent QWidget Sub Window')
        self.resize(400, 100)

        # 创建一个标签
        widget_label = QLabel('你可以继续操作主窗口')

        # 创建一个按钮，用于关闭子窗口
        close_button = QPushButton('Close Sub Window')
        close_button.clicked.connect(self.close)

        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(widget_label)
        layout.addWidget(close_button)
        self.setLayout(layout)
# 应用程序入口点
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个QApplication实例
    main_window = MainWindow()  # 创建一个主窗口实例
    main_window.show()  # 显示主窗口
    sys.exit(app.exec())  # 进入应用程序的主循环，并通过返回值退出程序
    