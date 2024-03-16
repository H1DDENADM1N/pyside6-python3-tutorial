from Ui_base64 import Ui_MainWindow_base64_encode_decode
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog)
import base64
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_base64_encode_decode()
        self.ui.setupUi(self)

        self.file_name = None
        self.content = None
        self.setup_signals()

    def setup_signals(self):
        self.ui.pushButton_encode.clicked.connect(self.encode_file)
        self.ui.pushButton_decode.clicked.connect(self.decode_file)
        self.ui.action_new.triggered.connect(self.new_file)
        self.ui.action_open.triggered.connect(self.open_file)
        self.ui.action_save.triggered.connect(self.save_file)
        self.ui.action_save_as.triggered.connect(self.save_file_as)
        self.ui.action_close.triggered.connect(self.close_file)

    def encode_file(self):
        if self.ui.plainTextEdit.toPlainText():
            self.content = self.ui.plainTextEdit.toPlainText()
            try:
                content_encode = str(base64.b64encode(self.content.encode("utf-8")))[2:-1]
                self.ui.plainTextEdit_result.setPlainText(content_encode)
                print(f"{self.content} 编码结果：{content_encode}")
            except Exception as e:
                self.ui.plainTextEdit_result.setPlainText(str(e))
                print(f"编码失败：{e}")

    def decode_file(self):
        if self.ui.plainTextEdit.toPlainText():
            self.content = self.ui.plainTextEdit.toPlainText()
            try:
                content_decode = str(base64.b64decode(self.content).decode("utf-8"))
                self.ui.plainTextEdit_result.setPlainText(content_decode)
                print(f"{self.content} 解码结果：{content_decode}")
            except Exception as e:
                self.ui.plainTextEdit_result.setPlainText(str(e))
                print(f"解码失败：{e}")

    def new_file(self):
        # 设置默认目录（可选）
        # self.file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options)
        options = QFileDialog.Options()
        self.file_name, _ = QFileDialog.getSaveFileName(self, "新建文件", "", "Text Files (*.txt);;All Files (*)", options=options)
        if self.file_name:
            self.ui.tabWidget.setTabText(0, os.path.basename(self.file_name))
            print("新建文件:", self.file_name)
            with open(self.file_name, "w", encoding="utf-8") as file:
                pass # 新建文件，不需要往文件中写入任何内容

    def open_file(self):
        options = QFileDialog.Options()
        # 设置默认目录（可选）
        # self.file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options)
        self.file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "", "所有文件 (*);;文本文件 (*.txt)")
        if self.file_name:
            self.ui.tabWidget.setTabText(0, os.path.basename(self.file_name))
            print("打开文件：", self.file_name)
            with open(self.file_name, "r", encoding="utf-8") as file:
                self.content = file.read()
                self.ui.plainTextEdit.setPlainText(self.content)
            print("文件内容：", self.content)

    def save_file(self):
        if self.file_name:
            result_file_name = self.file_name+"__result.txt"
            print("保存文件：", result_file_name)
            with open(result_file_name, "w", encoding="utf-8") as file:
                file.write(self.ui.plainTextEdit_result.toPlainText())
        else:
            self.save_file_as()

    def save_file_as(self):
        options = QFileDialog.Options()
        # 设置默认文件名或目录（可选）
        # self.file_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "所有文件 (*);;文本文件 (*.txt)", options=options)
        self.file_name, _ = QFileDialog.getSaveFileName(self, "另存为", "", "所有文件 (*);;文本文件 (*.txt)")
        if self.file_name:
            print("另存为：", self.file_name)
            with open(self.file_name, "w", encoding="utf-8") as file:
                file.write(self.ui.plainTextEdit_result.toPlainText())

    def close_file(self):
        self.file_name = None
        self.content = None
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit_result.clear()
        self.ui.tabWidget.setTabText(0, os.path.basename("文件名"))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
