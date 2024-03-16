from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QPushButton, QFileDialog)
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("文件夹对话框示例")

        # 创建按钮并连接到相应的槽函数
        create_folder_button = QPushButton("新建文件夹", self)
        create_folder_button.clicked.connect(self.create_folder)
        
        open_folder_button = QPushButton("打开文件夹", self)
        open_folder_button.clicked.connect(self.open_folder)

        # 创建一个垂直布局
        layout = QVBoxLayout()
        layout.addWidget(create_folder_button)
        layout.addWidget(open_folder_button)

        # 设置中心小部件
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def create_folder(self):
        folder_path, _ = QFileDialog.getSaveFileName(self, "新建文件夹")
        if folder_path:
            # Handle folder creation logic here
            os.makedirs(folder_path, exist_ok=True)
            print("新建文件夹:", folder_path)

    def open_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "打开文件夹")
        if folder_path:
            # Handle folder opening logic here
            os.startfile(folder_path)
            print("打开文件夹:", folder_path)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
