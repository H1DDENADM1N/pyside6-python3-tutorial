from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QPushButton, QFileDialog)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件对话框示例")
        
        # 创建按钮并连接到相应的槽函数
        new_file_button = QPushButton("新建文件", self)
        new_file_button.clicked.connect(self.new_file)
        
        open_file_button = QPushButton("打开文件", self)
        open_file_button.clicked.connect(self.open_file)
        
        open_files_button = QPushButton("打开多个文件", self)
        open_files_button.clicked.connect(self.open_files)
        
        save_file_button = QPushButton("保存文件", self)
        save_file_button.clicked.connect(self.save_file)
        
        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(new_file_button)
        layout.addWidget(open_file_button)
        layout.addWidget(open_files_button)
        layout.addWidget(save_file_button)

        # 设置中心小部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def new_file(self):
        # 设置默认目录（可选）
        # self.file_name, _ = QFileDialog.getOpenFileName(self, "新建文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options)
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getSaveFileName(self, "新建文件", "", "Text Files (*.txt);;All Files (*)", options=options)
        if self.file_name:
            print("新建文件:", self.file_name)
            with open(self.file_name, "w") as file:
                pass # 新建文件，不需要往文件中写入任何内容

    def open_file(self):
        options = QFileDialog.Options()
        # 设置默认目录（可选）
        # self.file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options)
        self.file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)")
        if self.file_name:
            print("打开文件：", self.file_name)
            with open(self.file_name, "r") as file:
                content = file.read()
            print("文件内容：", content)

    def open_files(self):
        options = QFileDialog.Options()
        # 设置默认目录（可选）
        # self.file_name, _ = QFileDialog.getOpenFileNames(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options)
        self.file_names, _ = QFileDialog.getOpenFileNames(self, "打开多个文件", "", "所有文件 (*);;文本文件 (*.txt)")
        if self.file_names:
            for file_name in self.file_names:
                print("选择的文件：", file_name)

    def save_file(self):
        options = QFileDialog.Options()
        # 设置默认文件名或目录（可选）
        # self.file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options)
        self.file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "所有文件 (*);;文本文件 (*.txt)")
        if self.file_name:
            print("保存文件：", self.file_name)
            with open(self.file_name, "w") as file:
                file.write("要保存的内容")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
