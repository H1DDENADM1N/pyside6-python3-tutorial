from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QPushButton, QLabel, QVBoxLayout,
                               QErrorMessage, QProgressDialog, QWizard, QWizardPage)
from PySide6.QtCore import Qt, QTimer

# 定义主窗口类 MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("对话框示例")
        self.resize(400, 100)

        # 创建一个垂直布局
        layout = QVBoxLayout()
        
        self.error_button = QPushButton("显示错误消息", self)
        self.error_button.clicked.connect(self.show_error_message)
        layout.addWidget(self.error_button)

        self.progress_button = QPushButton("显示进度对话框", self)
        self.progress_button.clicked.connect(self.show_progress_dialog)
        layout.addWidget(self.progress_button)

        self.wizard_button = QPushButton("显示向导对话框", self)
        self.wizard_button.clicked.connect(self.show_wizard)
        layout.addWidget(self.wizard_button)

        # 创建一个中央小部件并设置布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # 定义错误消息对话框
    def show_error_message(self):
        error_dialog = QErrorMessage(self)
        error_dialog.showMessage("这是一个错误消息。你可以选择不再显示此类消息。")

    # 定义进度条对话框
    def show_progress_dialog(self):
        self.progress_dialog = QProgressDialog("处理中...", "取消", 0, 100, self)
        self.progress_dialog.setWindowTitle("进度对话框")
        self.progress_dialog.setWindowModality(Qt.WindowModal)  # 设置进度对话框为模态对话框，阻止用户与其他窗口交互
        
        self.progress_dialog.canceled.connect(self.cancel_progress)
        
        # 创建一个定时器，模拟执行任务
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start()
        self.steps = 0  # 初始化步数

    # 定义更新进度的函数
    def update_progress(self):
        self.progress_dialog.setValue(self.steps)  # 更新步数
        self.steps += 1  # 增加步数
        if self.steps > self.progress_dialog.maximum():  # 如果步数超过最大值
            self.timer.stop()  # 停止定时器
    
    # 定义取消进度的函数
    def cancel_progress(self):
        self.timer.stop()  # 停止定时器
        self.progress_dialog.close()  # 关闭进度对话框

    # 定义向导对话框
    def show_wizard(self):
        wizard_dialog = QWizard(self)  # 创建一个向导对话框
        wizard_dialog.setWindowTitle("向导对话框")
        wizard_dialog.addPage(Page1())  # 添加页
        wizard_dialog.addPage(Page2())

        wizard_dialog.exec()  # 执行向导对话框

# 定义向导对话框的第一页
class Page1(QWizardPage):
    def __init__(self):
        super().__init__()

        self.setTitle("第一页")  # 设置页面标题
        label = QLabel("这是第一页")  # 创建标签
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

# 定义向导对话框的第二页
class Page2(QWizardPage):
    def __init__(self):
        super().__init__()

        self.setTitle("第二页")  # 设置页面标题
        label = QLabel("这是第二页")  # 创建标签
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
