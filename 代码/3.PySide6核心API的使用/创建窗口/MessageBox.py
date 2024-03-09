from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                                QMessageBox, QPushButton, QVBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MessageBox Example")
        self.resize(400, 100)

        # 创建一个垂直布局
        layout = QVBoxLayout()

        # 创建四个按钮，每个按钮对应一种 QMessageBox 类型
        self.info_button = QPushButton("信息框")
        self.info_button.clicked.connect(self.show_info_message)
        layout.addWidget(self.info_button)

        self.warning_button = QPushButton("警告框")
        self.warning_button.clicked.connect(self.show_warning_message)
        layout.addWidget(self.warning_button)

        self.critical_button = QPushButton("错误框")
        self.critical_button.clicked.connect(self.show_critical_message)
        layout.addWidget(self.critical_button)

        self.question_button = QPushButton("询问框")
        self.question_button.clicked.connect(self.show_question_message)
        layout.addWidget(self.question_button)

        # 创建一个中央小部件并设置布局
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_info_message(self):
        info_box = QMessageBox()
        reply = info_box.information(self, "信息", "这是一个信息框。", QMessageBox.Ok)
        info_box.setDetailedText("这是详细信息。")
        if reply == QMessageBox.Ok:
            self.on_info_accepted()
        elif reply == QMessageBox.Cancel:
            self.on_info_rejected()

    def show_warning_message(self):
        warning_box = QMessageBox()
        reply = warning_box.warning(self, "警告", "这是一个警告框。", QMessageBox.Ok)
        warning_box.setDetailedText("这是详细信息。")
        if reply == QMessageBox.Ok:
            self.on_warning_accepted()
        elif reply == QMessageBox.Cancel:
            self.on_warning_rejected()

    def show_critical_message(self):
        critical_box = QMessageBox()
        reply = critical_box.critical(self, "错误", "这是一个错误框。", QMessageBox.Ok)
        critical_box.setDetailedText("这是详细信息。")
        if reply == QMessageBox.Ok:
            self.on_critical_accepted()
        elif reply == QMessageBox.Cancel:
            self.on_critical_rejected()

    def show_question_message(self):
        question_box = QMessageBox()
        reply = question_box.question(self, "询问", "这是一个询问框。", QMessageBox.Ok | QMessageBox.Cancel)
        question_box.setDetailedText("这是详细信息。")
        question_box.setDefaultButton(QMessageBox.Ok)
        question_box.setEscapeButton(QMessageBox.Cancel)
        if reply == QMessageBox.Ok:
            self.on_question_accepted()
        elif reply == QMessageBox.Cancel:
            self.on_question_rejected()

    def on_info_accepted(self):
        print("信息框的确定按钮被点击")

    def on_info_rejected(self):
        print("信息框的取消按钮被点击")

    def on_warning_accepted(self):
        print("警告框的确定按钮被点击")

    def on_warning_rejected(self):
        print("警告框的取消按钮被点击")

    def on_critical_accepted(self):
        print("错误框的确定按钮被点击")
    
    def on_critical_rejected(self):
        print("错误框的取消按钮被点击")

    def on_question_accepted(self):
        print("询问框的确定按钮被点击")
        
    def on_question_rejected(self):
        print("询问框的取消按钮被点击")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
